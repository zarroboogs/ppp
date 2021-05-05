
games = [
    {
        'name': 'Persona 5 (PS4) EU v1.00',
        'title': 'CUSA06638',
        'version': '0100',
        'check': [
            { 'offset': 0x10CAE97, 'value': b'CUSA06638' },
        ],
    },
    {
        'name': 'Persona 5 Royal US v1.02',
        'title': 'CUSA17416',
        'version': '0102',
        'check': [
            { 'offset': 0x18110E7, 'value': b'CUSA17416' },
        ],
    },
    {
        'name': 'Persona 5 Royal EU v1.02',
        'title': 'CUSA17419',
        'version': '0102',
        'check': [
            { 'offset': 0x18110E7, 'value': b'CUSA17419' },
        ],
    },
]

patches = [
    {
        'path': 'CUSA06638_0100/all_dlc.xdelta',
        'id': 'all_dlc',
        'name': 'Content Enabler',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/intro_skip.xdelta',
        'id': 'intro_skip',
        'name': 'Intro Skip',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/mod_support.xdelta',
        'id': 'mod_support',
        'name': 'Mod Support',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/mod_support2.xdelta',
        'id': 'mod_support2',
        'name': 'Mod Support Alt',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/no_trp.xdelta',
        'id': 'no_trp',
        'name': 'Disable Trophies',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/square.xdelta',
        'id': 'square',
        'name': 'Global Square Menu',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/env.xdelta',
        'id': 'env',
        'name': 'ENV Test',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/zzz.xdelta',
        'id': 'zzz',
        'name': 'Random Tests',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA17416_0102/0505.xdelta',
        'id': '0505',
        'name': 'PS4 FW 5.05 Backport',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/all_dlc.xdelta',
        'id': 'all_dlc',
        'name': 'Content Enabler',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/intro_skip.xdelta',
        'id': 'intro_skip',
        'name': 'Intro Skip',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/mod_support.xdelta',
        'id': 'mod_support',
        'name': 'Mod Support',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/mod_support2.xdelta',
        'id': 'mod_support2',
        'name': 'Mod Support Alt',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/no_trp.xdelta',
        'id': 'no_trp',
        'name': 'Disable Trophies',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/p5_save.xdelta',
        'id': 'p5_save',
        'name': 'P5 Save Bonus Enabler',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/square.xdelta',
        'id': 'square',
        'name': 'Global Square Menu',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/env.xdelta',
        'id': 'env',
        'name': 'ENV Test',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/zzz.xdelta',
        'id': 'zzz',
        'name': 'Random Tests',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
]
