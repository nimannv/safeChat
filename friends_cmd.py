import typer
from obj.Friends import Friends

app = typer.Typer()


@app.command()
def show():
    friend_list = Friends().getAll()
    for username, PUK in friend_list.items():
        print(username)

@app.command()
def add():
    username = typer.prompt("Username: ")
    PUK = typer.prompt("Public Key: ")
    Friends().add(username, PUK)
    Friends().save()

@app.command()
def delete(username: str = typer.Argument("")):
    if username == "":
        username = typer.prompt("Username: ")
    Friends().delete(username)
    Friends().save()



if __name__ == "__main__":
    app()