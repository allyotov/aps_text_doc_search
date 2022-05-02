import typer

from searchapp.tools.db import create_db, fill_db_initially

app = typer.Typer()


@app.command()
def create():
    typer.echo('Creating database...')
    create_db.create()
    typer.echo('The process of creation is over. See logs for details.')


@app.command()
def fill(csv: str = typer.Argument('posts.csv')):  # noqa: WPS404, B008
    fill_db_initially.fill_db_from_given_csv(csv_path=csv)


if __name__ == '__main__':
    app()