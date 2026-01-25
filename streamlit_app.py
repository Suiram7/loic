import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Competition Ready", layout="centered", initial_sidebar_state="collapsed")

html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body>
    <div id="root"></div>

    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

    <script>
        const { useState, useEffect } = React;

        // Structure des données (exactement comme ton React original)
        const sections = [
            {
                title: "Phase 1 : J-14 à J-7",
                subtitle: "L'Affûtage & La Fondation",
                icon: "⏱️",
                proTip: "Le but ici est la fraîcheur. On ne cherche plus à progresser physiquement, mais à arriver reposé et ultra-performant.",
                categories: [
                    {
                        name: "Entraînement & Physio",
                        items: [{ id: "taper", label: "Phase de Taper", time: "J-14", details: "Réduction du volume global en maintenant l'intensité." }]
                    },
                    {
                        name: "Nutrition & Hygiène",
                        items: [{ id: "sleep", label: "Sommeil 'Banking'", time: "J-14", details: "Vise +45 à +90 min/nuit. La régularité > Quantité." }]
                    }
                ]
            },
            {
                title: "Phase 2 : J-6 à J-1",
                subtitle: "La Semaine Critique",
                icon: "⚡",
                proTip: "Tout le monde est prêt physiquement. Ceux qui gagnent sont ceux qui optimisent les détails.",
                categories: [
                    {
                        name: "Nutrition & Hydratation",
                        items: [
                            { id: "beet", label: "Jus de Betterave", time: "J-6", details: "70-140 ml/jour. Améliore l'économie d'effort. Éviter bains de bouche." },
                            { id: "sodium", label: "Hyperhydratation sodée", time: "J-3", details: "Eau riche en sodium ou électrolytes." },
                            { id: "residues", label: "Régime sans résidus", time: "J-2", details: "Élimine les fibres pour vider le tractus intestinal (gain 500g-1kg)." },
                            { id: "carbs", label: "Charge Glucidique", time: "J-1", details: "Cible : 4-5g de glucides / kg de PDC." }
                        ]
                    },
                    {
                        name: "Suppléments",
                        items: [
                            { id: "caf_reset", label: "Arrêt de la Caféine", time: "J-7", details: "Se sevrer pour resensibiliser les récepteurs." },
                            { id: "gear", label: "Check-up Matériel", time: "J-1", details: "Chaussures, straps, nutrition. Rien de nouveau le jour J." }
                        ]
                    }
                ]
            },
            {
                title: "Phase 3 : Le Jour J",
                subtitle: "Avant l'épreuve",
                icon: "🔥",
                proTip: "L'objectif de l'échauffement est l'excitation neuronale, pas la fatigue.",
                categories: [
                    {
                        name: "Nutrition",
                        items: [
                            { id: "pre_meal", label: "Repas Pré-compé", time: "H-4", details: "Glucides ++, pauvre en lipides/fibres (ex: riz blanc, compote)." },
                            { id: "caf_final", label: "Caféine Elite", time: "H-1", details: "3 mg / kg de poids de corps. Réduit le RPE." }
                        ]
                    },
                    {
                        name: "Warm-up",
                        items: [
                            { id: "pap", label: "PAP Musculaire", time: "H-15m", details: "Contractions max très brèves. Intensité max, volume bas." },
                            { id: "vest", label: "Veste thermique", time: "Dép.", details: "Garder le corps au chaud jusqu'au signal." }
                        ]
                    }
                ]
            },
            {
                title: "Phase 4 : En Course",
                subtitle: "Gestion & Entre-runs",
                icon: "🧠",
                proTip: "La différence entre les bons et les champions se joue dans la gestion entre les runs.",
                categories: [
                    {
                        name: "Protocole",
                        items: [
                            { id: "recov", label: "Récup Active", time: "H+2m", details: "Marche active. Ne t'assois pas. Respire par le nez." },
                            { id: "rinse", label: "Relance (Rinçage)", time: "H-5m", details: "Rinçage de bouche sucré (recracher) pour stimuler le cerveau." }
                        ]
                    }
                ]
            }
        ];

        function App() {
            const [activeTab, setActiveTab] = useState(0);
            const [checkedItems, setCheckedItems] = useState({});
            const [openDetails, setOpenDetails] = useState({});

            const currentPhase = sections[activeTab];
            const allItems = currentPhase.categories.flatMap(c => c.items);
            const progress = (allItems.filter(i => checkedItems[i.id]).length / allItems.length) * 100;

            const toggleCheck = (id) => {
                setCheckedItems(prev => ({ ...prev, [id]: !prev[id] }));
            };

            const toggleInfo = (e, id) => {
                e.stopPropagation();
                setOpenDetails(prev => ({ ...prev, [id]: !prev[id] }));
            };

            return React.createElement('div', { className: 'max-w-md mx-auto p-4 pb-20' },
                // Header
                React.createElement('header', { className: 'mb-6 text-center' },
                    React.createElement('h1', { className: 'text-3xl font-black text-red-600 italic tracking-tighter' }, 'COMPETITION READY.'),
                    React.createElement('p', { className: 'text-[10px] font-bold text-gray-400 uppercase tracking-widest' }, 'Checklist Performance')
                ),

                // Navigation
                React.createElement('div', { className: 'flex justify-between mb-8 bg-white/60 backdrop-blur-xl p-1.5 rounded-2xl border border-white shadow-sm' },
                    sections.map((s, i) => React.createElement('button', {
                        key: i,
                        onClick: () => setActiveTab(i),
                        className: `flex-1 py-3 rounded-xl flex flex-col items-center transition-all ${activeTab === i ? 'bg-white shadow-md text-red-600 scale-[1.05]' : 'text-gray-300'}`
                    }, 
                        React.createElement('span', { className: 'text-lg' }, s.icon),
                        React.createElement('span', { className: 'text-[8px] mt-1 font-black uppercase' }, `Phase ${i+1}`)
                    ))
                ),

                // Progress
                React.createElement('div', { className: 'mb-6 px-2' },
                    React.createElement('div', { className: 'flex justify-between items-end mb-2' },
                        React.createElement('div', null,
                            React.createElement('h2', { className: 'text-2xl font-black text-slate-800' }, currentPhase.title),
                            React.createElement('p', { className: 'text-red-500 font-bold text-[10px] uppercase' }, currentPhase.subtitle)
                        ),
                        React.createElement('span', { className: 'text-xs font-black text-slate-300' }, `${Math.round(progress)}%`)
                    ),
                    React.createElement('div', { className: 'w-full bg-slate-200 h-1.5 rounded-full overflow-hidden' },
                        React.createElement('div', { 
                            className: 'h-full bg-red-600 transition-all duration-700', 
                            style: { width: `${progress}%` } 
                        })
                    )
                ),

                // Content
                currentPhase.categories.map((cat, idx) => React.createElement('div', { key: idx, className: 'mb-6' },
                    React.createElement('h3', { className: 'font-black text-[10px] uppercase tracking-widest text-slate-400 mb-3 px-2' }, cat.name),
                    cat.items.map(item => React.createElement('div', { key: item.id, className: 'mb-2' },
                        React.createElement('div', { 
                            onClick: () => toggleCheck(item.id),
                            className: `flex items-center gap-3 p-4 bg-white rounded-2xl border border-white shadow-sm cursor-pointer transition-all ${checkedItems[item.id] ? 'bg-red-50/50 border-red-100' : ''}`
                        },
                            React.createElement('div', { className: `w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0 ${checkedItems[item.id] ? 'bg-red-600 border-red-600' : 'border-slate-200'}` },
                                checkedItems[item.id] && React.createElement('span', { className: 'text-white text-[10px]' }, '✓')
                            ),
                            React.createElement('div', { className: 'flex-1' },
                                React.createElement('p', { className: 'text-[9px] font-black text-red-500 uppercase' }, item.time),
                                React.createElement('p', { className: `text-sm font-bold ${checkedItems[item.id] ? 'text-red-700' : 'text-slate-800'}` }, item.label)
                            ),
                            React.createElement('button', {
                                onClick: (e) => toggleInfo(e, item.id),
                                className: `p-2 rounded-lg ${openDetails[item.id] ? 'bg-red-600 text-white' : 'bg-slate-50 text-slate-300'}`
                            }, 'i')
                        ),
                        openDetails[item.id] && React.createElement('div', { className: 'mt-1 p-4 bg-white/50 rounded-2xl text-[11px] text-slate-600 leading-relaxed italic border border-white' },
                            item.details
                        )
                    ))
                )),

                // Footer Tip
                React.createElement('div', { className: 'mt-8 p-5 bg-white rounded-3xl border border-slate-100 shadow-xl flex gap-4' },
                    React.createElement('div', { className: 'bg-red-600 p-3 rounded-2xl text-white h-fit' }, '💡'),
                    React.createElement('div', null,
                        React.createElement('h4', { className: 'font-black text-[10px] uppercase text-red-600' }, `Conseil Pro Phase ${activeTab+1}`),
                        React.createElement('p', { className: 'text-[11px] font-bold text-slate-700 italic mt-1' }, `"${currentPhase.proTip}"`)
                    )
                )
            );
        }

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(React.createElement(App));
    </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)

st.caption("Next Athlete Performance System v1.0 • Running on Streamlit Engine")