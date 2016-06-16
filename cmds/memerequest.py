import smtplib
import config
import random

from interface import Interface

class MemeRequest(Interface):
    '''
        Declare variables with desired to and from email addresses.
        Only works if the from is a gmail address.

        Example usage:
        .mr <text describing meme>
    '''
    def start(self, *args, **kwargs):
        # address to send requests to
        self.to = ""
        # must be logged into gmail in order to work
        self.fr = ""
        # password for form email
        self.pwd = ""
        self.replies = [ "dank meme-o friend-o",
                        "spicy",
                        "#nicememe",
                        "that's an odd request",
                        "http://imgur.com/9uCFmha"
                        ]

    def send_email(self, data):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fr, self.pwd)

        msg = data.usernick + " has requested a meme of you:\n\n" + data.cmd['parameters']
        server.sendmail(self.fr, self.to, msg)
        server.quit()

    def dot_mr(self,data):
        data.conn.msg(data.channel, random.choice(self.replies))
        self.send_email(data)
