###########################################################
########              S e t t i n g s              ########
###########################################################
identity = {
    'FoxBot': {
        'nickname': 'FoxBot',
        'realname': 'IRCBot',
        'username': '',
        'nickserv_pw': '',
        'adminPass': '',
        'wolframID': ''
    },
}
networks = {
    'SwiftIRC': {
        'host': '',
        'port': 6667,
        'ssl': False,
        'identity': identity['FoxBot'],
        'autojoin': (
            '',
        )
    },
}
###########################################################