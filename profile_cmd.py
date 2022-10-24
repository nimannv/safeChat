import typer
from obj.Profile import Profile

app = typer.Typer()


@app.command()
def show():
    Profile().show_keys()

if __name__ == "__main__":
    app()