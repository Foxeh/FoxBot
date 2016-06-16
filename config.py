###########################################################
########              S e t t i n g s              ########
###########################################################
TO=""
FROM=""
PASSWORD=""

identity = {
    'bot': {
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
        'identity': identity['bot'],
        'autojoin': (
            '',
        )
    },
}
admin = [""]
###########################################################
