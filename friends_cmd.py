import typer
from obj.Friends import Friends

app = typer.Typer()


@app.command()
def show():
    Friends().show()

if __name__ == "__main__":
    app()