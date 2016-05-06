###########################################################
########              S e t t i n g s              ########
###########################################################
identity = {
    'Bot': {
        'nickname': '',
        'realname': '',
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
        'identity': identity['Bot'],
        'autojoin': (
            '',
        )
    },
}
###########################################################