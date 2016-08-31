## FoxBot - A Plug-able Command-Driven IRC Bot
Join #fox in IRC.SwiftIRC.net for help.

### Available IRC Plugins

Google - Returns first result.    
Roll - Random dice rolling system for games.    
Wolfram - Evaluate through wolfram!    
RuneScape - Highscores, Mobs, and Item Lookups.
Dictionary - Get the first definition of a word.

### Packages

Twisted Python    
http://twistedmatrix.com/trac/wiki/Downloads

WolframAlpha
`sudo pip install wolframalpha`    
Then get an API key - https://developer.wolframalpha.com/portal/signin.html

### To get started:
Set variables in `config.py`.   
    
Then run foxbot:   
```
python foxbox.py
```

### Development
Creating a plug-in for Foxbot is easier than any other bot.

####Step 1:    
Create a class inheriting `Interface`, and put it in the `cmd/` folder.    
```python
from interface import Interface

class Sample(Interface):
```

####Step 2:    
Create your method that will respond to commands in the IRC channel.    
```python
# For the command: .sample
def dot_sample(self, data):
	pass
```

Methods are called by what the command is:    
	The command:    
		`.test hi`    
	Calls:    
		```python
		def dot_test(self, data):
		```
		
####Step 3:    
Now use the parameter `data`, which is an object with everything you need for the method.    
```python
def dot_sample(self, data):
	data.conn.msg(data.channel, "You typed in '.sample'!")
```
#####API:    
| Param        		| Definition		|
| ---------------------- | -------------|
| `data.conn` | is the reference to anything with the bot, like notices, or messages:  |
| `data.conn.notice(<to>, <msg>)` | sends a notice to the recip. | 
| `data.conn.msg(<to>, <msg>)` | sends a message to the recip. |
| `data.channel`	| is the channel that the message came from.   |
| `data.usernick`	|  is the caller's nick.  |
| `data.host` |  the host of the caller.  |
| `data.user` | the bot's nick. |
| `data.admin` | the list of admins. |
| `data.action` | The string of the action in the cmd. ie. bang (!), question (?), dot (.).  |
| `data.cmd` | is a dictionary of what was in the command. |
| `data.cmd['action']` | action of the command. (.!?) ---- ex. `!`google test |
| `data.cmd['method']` | the method to call. --------------- ex. !`google` test |
| `data.cmd['parameters']` | the last part of a command. ----- ex. !google `test` |


####Step 4. (Optional)    
If the command needs to be protected, add your name to `admin` in `config.py` and use the provided decorator:    

```python
from cmds.admin import requiresAdmin

@requiresAdmin
def dot_sample(self, data):
	data.conn.msg(data.channel, "You are an admin.")
```
