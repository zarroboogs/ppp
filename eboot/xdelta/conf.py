games = [
    {
        'name': 'Persona 5 (PS4) EU',
        'title': 'CUSA06638',
        'version': '0100',
        'check': [
            { 'offset': 0x10CAE67, 'value': b'CUSA06638' },
        ],
        'path': 'xdelta/CUSA06638_0100/',
        'patches': [
            { 'id': 'all_dlc', 'name': 'Content Enabler' },
            { 'id': 'intro_skip', 'name': 'Intro Skip' },
            { 'id': 'mod_support', 'name': 'Mod Support' },
            { 'id': 'no_trp', 'name': 'Disable Trophies' },
            { 'id': 'square', 'name': 'Global Square Menu' },

            { 'id': 'env', 'name': 'ENV Test' },
            { 'id': 'zzz', 'name': 'Random Tests' },
        ]
    },
    {
        'name': 'Persona 5 Royal US',
        'title': 'CUSA17416',
        'version': '0102',
        'check': [
            { 'offset': 0x18110E7, 'value': b'CUSA17416' },
        ],
        'path': 'xdelta/CUSA17416_0102',
        'patches': [
            { 'id': '0505', 'name': 'PS4 FW 5.05 Backport'},
            { 'id': 'all_dlc', 'name': 'Content Enabler' },
            { 'id': 'intro_skip', 'name': 'Intro Skip' },
            { 'id': 'mod_support', 'name': 'Mod Support' },
            { 'id': 'no_trp', 'name': 'Disable Trophies' },
            { 'id': 'p5_save', 'name': 'P5 Save Bonus Enabler'},
            { 'id': 'square', 'name': 'Global Square Menu' },

            { 'id': 'env', 'name': 'ENV Test' },
            { 'id': 'zzz', 'name': 'Random Tests' },
        ]
    }
]