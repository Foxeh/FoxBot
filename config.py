###########################################################
########              S e t t i n g s              ########
###########################################################
identity = {
    'TestBot': {
        'nickname': 'TestBot',
        'realname': 'IRCBot',
        'username': '',
        'nickserv_pw': '',
        'adminPass': '',
        'wolframID': ''
    },
}
networks = {
    'SwiftIRC': {
        'host': 'bipartite.nj.us.SwiftIRC.net',
        'port': 6667,
        'ssl': False,
        'identity': identity['TestBot'],
        'autojoin': (
            '#fox',
        )
    },
}
###########################################################