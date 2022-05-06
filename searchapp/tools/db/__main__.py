import typer

from searchapp.tools.db import create_db, fill_db_initially
from searchapp.resources.models import es

app = typer.Typer()


@app.command()
def create():
    typer.echo('Creating database...')
    create_db.create()
    typer.echo('The process of creation is over. See logs for details.')


@app.command()
def fill(csv: str = typer.Argument('posts.csv')):  # noqa: WPS404, B008
    fill_db_initially.fill_db_from_given_csv(csv_path=csv)


@app.command()
def elastic():
    es_ping = es.ping()
    typer.echo("Elastic connection ping: %r !" % es_ping)
    typer.echo(es.cluster.health())


if __name__ == '__main__':
    app()