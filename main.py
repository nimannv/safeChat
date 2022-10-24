import typer

import chat_cmd
import friends_cmd
import profile_cmd


from obj.Profile import Profile 
from obj.Friends import Friends 
from obj.Conversations import Conversations 



#load profile
Profile().load()

#load friends list
Friends('data/friends_list.json').load()

#load conversations
# Conversations('').load

app = typer.Typer()
app.add_typer(chat_cmd.app, name="chat")
app.add_typer(profile_cmd.app, name="profile")
app.add_typer(friends_cmd.app, name="friend")

if __name__ == "__main__":
    app()