import typer

app = typer.Typer()


@app.command()
def create(name: str):
    print(f"Creating item: {name}")


@app.command()
def delete(name: str):
    print(f"Deleting name: {name}")


@app.command()
def sell(name: str):
    print(f"Selling name: {name}")


if __name__ == "__main__":
    app()