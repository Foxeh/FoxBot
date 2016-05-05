###########################################################
########              S e t t i n g s              ########
###########################################################
identity = {
    'TestBot': {
        'nickname': 'Unknon35',
        'realname': 'IRCBotDerp',
        'username': 'derpyder',
        'nickserv_pw': '',
        'adminPass': 'shitsngigs',
        'wolframID': ''
    },
}
networks = {
    'SwiftIRC': {
        'host': 'IRC.SwiftIRC.net',
        'port': 6667,
        'ssl': False,
        'identity': identity['TestBot'],
        'autojoin': (
            'fox',
        )
    },
}
###########################################################