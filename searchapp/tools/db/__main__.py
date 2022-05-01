import typer

from searchapp.tools.db import create_db

app = typer.Typer()


@app.command()
def create():
    typer.echo('Creating database...')
    create_db.create()
    typer.echo('The process of creation is over. See logs for details.')


# @app.command()
# def fill(csv: str = typer.Argument('books.csv')):  # noqa: WPS404, B008
#     populate_db_initially.populate_db_from_given_csv(csv_path=csv)


if __name__ == '__main__':
    app()