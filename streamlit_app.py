from reactpy import component, html, use_state
from reactpy.backend.starlette import configure

STYLE = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
})

@component
def ChecklistItem(item, checked_items, set_checked_items, open_details, set_open_details):
    is_checked = checked_items.get(item["id"], False)
    is_open = open_details.get(item["id"], False)

    def toggle_check(event):
        set_checked_items({**checked_items, item["id"]: not is_checked})

    def toggle_details(event):
        set_open_details({**open_details, item["id"]: not is_open})

    return html.div(
        {"class_name": "rounded-2xl border border-gray-100 overflow-hidden transition-all mb-2"},
        html.div(
            {
                "class_name": f"flex items-start gap-3 p-3 cursor-pointer transition-all {'bg-red-50' if is_checked else 'bg-white'}",
                "on_click": toggle_check
            },
            html.div(
                {"class_name": "mt-1 flex-shrink-0"},
                html.span({"class_name": f"text-xl {'text-red-600' if is_checked else 'text-gray-200'}"}, "●" if is_checked else "○")
            ),
            html.div(
                {"class_name": "flex-1"},
                html.div(
                    {"class_name": "flex justify-between items-start"},
                    html.div(
                        {"class_name": "flex flex-col"},
                        html.span({"class_name": "text-xs font-black text-red-500 uppercase mb-0.5"}, item["time"]),
                        html.p({"class_name": f"font-bold text-sm leading-tight {'text-red-700' if is_checked else 'text-gray-800'}"}, item["label"])
                    ),
                    html.button(
                        {
                            "class_name": f"p-1.5 rounded-lg transition-all {'bg-red-600 text-white' if is_open else 'bg-gray-50 text-gray-300'}",
                            "on_click": toggle_details
                        },
                        "i" 
                    )
                )
            )
        ),
        html.div(
            {"class_name": f"overflow-hidden bg-white transition-all {'p-4 border-t border-gray-50' if is_open else 'h-0'}"},
            html.div({"class_name": "text-xs text-gray-600 leading-relaxed font-medium"}, item["details"])
        )
    )

@component
def CompetitionApp():
    active_tab, set_active_tab = use_state(0)
    checked_items, set_checked_items = use_state({})
    open_details, set_open_details = use_state({})

    sections = [
        {
            "title": "Phase 1 : J-14 à J-7",
            "subtitle": "L'Affûtage & La Fondation",
            "icon": "⚡",
            "proTip": "Le but ici est la fraîcheur. On ne cherche plus à progresser physiquement.",
            "items": [
                {"id": "taper", "label": "Phase de Taper", "time": "J-14 ou J-7", "details": "Réduction du volume global en maintenant l'intensité"},
                {"id": "sleep", "label": "Sommeil 'Banking'", "time": "J-14 à J-0", "details": "Vise +45 à +90 min/nuit. La régularité > Quantité."}
            ]
        },
        {
            "title": "Phase 2 : J-6 à J-1",
            "subtitle": "La Semaine Critique",
            "icon": "🔥",
            "proTip": "Ceux qui gagnent sont ceux qui optimisent les détails négligés.",
            "items": [
                {"id": "nitrates", "label": "Charge de Jus de Betterave", "time": "J-6 à J-1", "details": "70-140 ml/jour. Améliore l'économie de l'effort."},
                {"id": "carb", "label": "Charge Glucidique", "time": "J-1", "details": "4-5g de glucides / kg de poids de corps."}
            ]
        }
        # ... Ajoutez les autres phases ici sur le même modèle
    ]

    current_phase = sections[active_tab]
    
    total_items = len(current_phase["items"])
    checked_count = sum(1 for item in current_phase["items"] if checked_items.get(item["id"]))
    progress = (checked_count / total_items * 100) if total_items > 0 else 0

    return html.div(
        {"class_name": "min-h-screen bg-gray-50 p-4 font-sans"},
        STYLE,
        html.div(
            {"class_name": "max-w-md mx-auto"},
            html.header(
                {"class_name": "mb-6 text-center"},
                html.h1({"class_name": "text-3xl font-black text-red-600 italic tracking-tighter"}, "COMPETITION READY."),
                html.h2({"class_name": "text-xs font-bold text-gray-400 uppercase tracking-widest"}, "Checklist")
            ),
            html.div(
                {"class_name": "flex justify-between mb-8 bg-white p-1.5 rounded-2xl shadow-sm"},
                [
                    html.button(
                        {
                            "class_name": f"flex-1 py-3 rounded-xl flex flex-col items-center transition-all { 'bg-white shadow text-red-600 scale-105' if active_tab == i else 'text-gray-300'}",
                            "on_click": lambda e, i=i: set_active_tab(i)
                        },
                        html.span({"class_name": "text-lg"}, s["icon"]),
                        html.span({"class_name": "text-[8px] font-black uppercase"}, f"Phase {i+1}")
                    ) for i, s in enumerate(sections)
                ]
            ),
            html.div(
                {"class_name": "mb-6 px-2"},
                html.div(
                    {"class_name": "flex justify-between items-end mb-2"},
                    html.div(
                        html.h3({"class_name": "text-xl font-black text-gray-800"}, current_phase["title"]),
                        html.p({"class_name": "text-red-500 font-bold text-xs uppercase"}, current_phase["subtitle"])
                    ),
                    html.span({"class_name": "text-xs font-black text-gray-300"}, f"{int(progress)}%")
                ),
                html.div(
                    {"class_name": "w-full bg-gray-200 h-1.5 rounded-full overflow-hidden"},
                    html.div({"class_name": "h-full bg-red-600 transition-all", "style": {"width": f"{progress}%"}})
                )
            ),
            html.div(
                {"class_name": "space-y-2"},
                [ChecklistItem(item, checked_items, set_checked_items, open_details, set_open_details) for item in current_phase["items"]]
            ),
            html.div(
                {"class_name": "mt-8 p-5 bg-white rounded-3xl border border-gray-100 shadow-xl flex gap-4"},
                html.div({"class_name": "bg-red-600 p-2 rounded-xl text-white h-10 w-10 flex items-center justify-center"}, "✓"),
                html.div(
                    html.h4({"class_name": "font-black text-[10px] uppercase text-red-600"}, f"Conseil Pro Phase {active_tab + 1}"),
                    html.p({"class_name": "text-xs leading-relaxed mt-1 font-bold text-gray-700 italic"}, f"\"{current_phase['proTip']}\"")
                )
            )
        )
    )

from reactpy.backend.starlette import configure
from starlette.applications import Starlette
import uvicorn

app = Starlette()
configure(app, CompetitionApp)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)