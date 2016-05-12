###########################################################
########              S e t t i n g s              ########
###########################################################
identity = {
    'Dristebot': {
        'nickname': 'DristeBot',
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
        'identity': identity['Dristebot'],
        'autojoin': (
            'fox',
        )
    },
}
admin = ["Driste"]
###########################################################