## FoxBot - A Plug-able Command-Driven IRC Bot
Join #fox in IRC.SwiftIRC.net for help.

### Available IRC Plugins

Google - Returns first result.    
Roll - Random dice rolling system for games.    
Wolfram - Evaluate through wolfram!    
RuneScape - Highscores, Mobs, and Item Lookups.
Dictionary - Get the first definition of a word.

### Packages

Twisted 16.1.1    
http://twistedmatrix.com/trac/wiki/Downloads

WolframAlpha 2.4    
`sudo pip install wolfralpha`    
Then get an API key - https://developer.wolframalpha.com/portal/signin.html

### To get started:
Set variables in config.py.    
```
python foxbox.py
```

### Development
Creating a plug-in for Foxbot is easier than any other bot.

####Step 1:    
Create a class inheriting `Interface`, and put it in the `cmd/` folder.    
```
from interface import Interface

class Sample(Interface):
```

####Step 2:    
Create your method that will respond to commands in the IRC channel.    
````
from interface import Interface

class Sample(Interface):
	def dot_sample(self, data):
		pass
````

Methods are called by what the command is:    
	The cammand:    
		`.test hi`    
	Calls:    
		````
		def dot_test(self, data):
			pass
		````
		
####Step 3:    
Now use the parameter `data`, which is an object with everything you need for the method.    
````
from interface import Interface

class Sample(Interface):
	def dot_sample(self, data):
		data.conn.msg(data.channel, "You typed in '.sample'!"
````
    
`data.conn` is the reference to anything with the bot, like notices, or messages:
	`data.conn.notice(<to>, <msg>)`    
	`data.conn.msg(<to>, <msg>)`    
`data.cmd[]` is a dictionary of what was in the command.    
	!wolf 2+2
	`data.cmd['action']` ex. !.?$%#^    
	`data.action` ex. bang (converts the special character into a string rep.)    
	`data.cmd['method']` ex. wolf    
	`data.cmd['parameters']` ex. 2+2    
`data.channel` is the channel that the message came from.    
`data.usernick` is the caller's nick.    
`data.host` the host of the caller.    
`data.user` the bot's nick.    
`data.admin` the list of admins.    

####Step 4. (Optional)    
If the command needs to be protected, add your name to `admin` in `config.py` and use the provided decorator:    

````
from cmds.admin import requiresAdmin
from interface import Interface

class Sample(Interface):

	@requiresAdmin
	def dot_sample(self, data):
		data.conn.msg(data.channel, "You typed in '.sample'!"
````