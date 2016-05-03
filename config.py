###########################################################
########              S e t t i n g s              ########
###########################################################
identity = {
    'TestBot': {
        'nickname': 'Unknown34893458',
        'realname': 'IRCBot',
        'username': '',
        'nickserv_pw': '',
        'adminPass': '',
        'wolframID': ''
    },
}
networks = {
    'SwiftIRC': {
        'host': 'irc.SwiftIRC.net',
        'port': 6667,
        'ssl': False,
        'identity': identity['TestBot'],
        'autojoin': (
            '#fox',
        )
    },
}
###########################################################