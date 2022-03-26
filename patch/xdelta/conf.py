
games = [
    {
        'name': 'Persona 5 (PS4) US v1.00',
        'title': 'CUSA05877',
        'version': '0100',
        'check': [
            { 'offset': 0x10CAE67, 'value': b'CUSA05877' },
        ],
    },
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
    {
        'name': 'Persona 5: Dancing in Starlight US v1.00',
        'title': 'CUSA12380',
        'version': '0100',
        'check': [
            { 'offset': 0x4241E0, 'value': b'CUSA12380' },
        ],
    },
    {
        'name': 'Persona 3: Dancing in Moonlight US v1.00',
        'title': 'CUSA12636',
        'version': '0100',
        'check': [
            { 'offset': 0x4211E0, 'value': b'CUSA12636' },
        ],
    },
    {
        'name': 'Persona 4: Dancing All Night EU v1.00',
        'title': 'CUSA12811',
        'version': '0100',
        'check': [
            { 'offset': 0x3BEBE0, 'value': b'CUSA12811' },
        ],
    },
]

patches = [
    {
        'path': 'CUSA05877_0100/intro_skip.xdelta',
        'id': 'intro_skip',
        'name': 'Intro Skip',
        'games': { 'CUSA05877' : '0100' },
    },
    {
        'path': 'CUSA05877_0100/mod_support.xdelta',
        'id': 'mod_support',
        'name': 'Mod Support (PKG)',
        'games': { 'CUSA05877' : '0100' },
    },
    {
        'path': 'CUSA05877_0100/mod_support2.xdelta',
        'id': 'mod_support2',
        'name': 'Mod Support (FTP)',
        'games': { 'CUSA05877' : '0100' },
    },
    {
        'path': 'CUSA05877_0100/no_trp.xdelta',
        'id': 'no_trp',
        'name': 'Disable Trophies',
        'games': { 'CUSA05877' : '0100' },
    },
    {
        'path': 'CUSA05877_0100/share_button.xdelta',
        'id': 'share_button',
        'name': 'Enable Share Button',
        'games': { 'CUSA05877' : '0100' },
    },
    {
        'path': 'CUSA05877_0100/square.xdelta',
        'id': 'square',
        'name': 'Global Square Menu',
        'games': { 'CUSA05877' : '0100' },
    },
    {
        'path': 'CUSA05877_0100/env.xdelta',
        'id': 'env',
        'name': 'ENV Test',
        'games': { 'CUSA05877' : '0100' },
        'display' : False,
    },
    {
        'path': 'CUSA05877_0100/zzz.xdelta',
        'id': 'zzz',
        'name': 'Random Tests',
        'games': { 'CUSA05877' : '0100' },
        'display' : False,
    },



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
        'name': 'Mod Support (PKG)',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/mod_support2.xdelta',
        'id': 'mod_support2',
        'name': 'Mod Support (FTP)',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/no_trp.xdelta',
        'id': 'no_trp',
        'name': 'Disable Trophies',
        'games': { 'CUSA06638' : '0100' },
    },
    {
        'path': 'CUSA06638_0100/share_button.xdelta',
        'id': 'share_button',
        'name': 'Enable Share Button',
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
        'display' : False,
    },
    {
        'path': 'CUSA06638_0100/zzz.xdelta',
        'id': 'zzz',
        'name': 'Random Tests',
        'games': { 'CUSA06638' : '0100' },
        'display' : False,
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
        'path': 'CUSA17416_0102/dlc_msg.xdelta',
        'id': 'dlc_msg',
        'name': 'Skip DLC Unlock Messages',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/intro_skip.xdelta',
        'id': 'intro_skip',
        'name': 'Intro Skip',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/mod.xdelta',
        'id': 'mod',
        'name': 'Mod Support (PKG)',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/mod_efigs.xdelta',
        'id': 'mod_efigs',
        'name': 'Mod Support EFIGS (PKG)',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/mod2.xdelta',
        'id': 'mod2',
        'name': 'Mod Support (FTP)',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/mod2_efigs.xdelta',
        'id': 'mod2_efigs',
        'name': 'Mod Support EFIGS (FTP)',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/mod3.xdelta',
        'id': 'mod3',
        'name': 'Mod Support (FTP HostFS)',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/mod3_efigs.xdelta',
        'id': 'mod3_efigs',
        'name': 'Mod Support EFIGS (FTP HostFS)',
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
        'path': 'CUSA17416_0102/share_button.xdelta',
        'id': 'share_button',
        'name': 'Enable Share Button',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/square.xdelta',
        'id': 'square',
        'name': 'Global Square Menu',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/bgm_ord.xdelta',
        'id': 'bgm_ord',
        'name': 'Sequential Battle BGM',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/bgm_rnd.xdelta',
        'id': 'bgm_rnd',
        'name': 'Randomized Battle BGM',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
    },
    {
        'path': 'CUSA17416_0102/env.xdelta',
        'id': 'env',
        'name': 'ENV Test',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
        'display' : False,
    },
    {
        'path': 'CUSA17416_0102/zzz.xdelta',
        'id': 'zzz',
        'name': 'Random Tests',
        'games' : { 'CUSA17416' : '0102', 'CUSA17419' : '0102' },
        'display' : False,
    },



    {
        'path': 'CUSA12380_0100/intro_skip.xdelta',
        'id': 'intro_skip',
        'name': 'Intro Skip',
        'games' : { 'CUSA12380' : '0100' },
    },
    {
        'path': 'CUSA12380_0100/mod.xdelta',
        'id': 'mod',
        'name': 'Mod Support',
        'games' : { 'CUSA12380' : '0100' },
    },
    {
        'path': 'CUSA12380_0100/no_trp.xdelta',
        'id': 'no_trp',
        'name': 'Disable Trophies',
        'games' : { 'CUSA12380' : '0100' },
    },
    {
        'path': 'CUSA12380_0100/overlay.xdelta',
        'id': 'overlay',
        'name': 'Disable Screenshot Overlay',
        'games' : { 'CUSA12380' : '0100' },
    },
    {
        'path': 'CUSA12380_0100/psvc.xdelta',
        'id': 'psvc',
        'name': 'PSV Content Compat.',
        'games' : { 'CUSA12380' : '0100' },
        'display' : False,
    },



    {
        'path': 'CUSA12636_0100/intro_skip.xdelta',
        'id': 'intro_skip',
        'name': 'Intro Skip',
        'games' : { 'CUSA12636' : '0100' },
    },
    {
        'path': 'CUSA12636_0100/mod.xdelta',
        'id': 'mod',
        'name': 'Mod Support',
        'games' : { 'CUSA12636' : '0100' },
    },
    {
        'path': 'CUSA12636_0100/no_trp.xdelta',
        'id': 'no_trp',
        'name': 'Disable Trophies',
        'games' : { 'CUSA12636' : '0100' },
    },
    {
        'path': 'CUSA12636_0100/overlay.xdelta',
        'id': 'overlay',
        'name': 'Disable Screenshot Overlay',
        'games' : { 'CUSA12636' : '0100' },
    },
    {
        'path': 'CUSA12636_0100/psvc.xdelta',
        'id': 'psvc',
        'name': 'PSV Content Compat.',
        'games' : { 'CUSA12636' : '0100' },
        'display' : False,
    },



    {
        'path': 'CUSA12811_0100/intro_skip.xdelta',
        'id': 'intro_skip',
        'name': 'Intro Skip',
        'games' : { 'CUSA12811' : '0100' },
    },
    {
        'path': 'CUSA12811_0100/mod.xdelta',
        'id': 'mod',
        'name': 'Mod Support',
        'games' : { 'CUSA12811' : '0100' },
    },
    {
        'path': 'CUSA12811_0100/no_trp.xdelta',
        'id': 'no_trp',
        'name': 'Disable Trophies',
        'games' : { 'CUSA12811' : '0100' },
    },
]
