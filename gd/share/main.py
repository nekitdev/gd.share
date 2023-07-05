from pathlib import Path

import click
from gd.api.levels import CreatedLevelAPI
from gd.api.save_manager import save
from gd.binary import dump_to, load_from
from iters.iters import iter
from tabulate import tabulate

from gd.share.version import version_info

version = str(version_info)


@click.help_option("--help", "-h")
@click.version_option(version, "--version", "-V")
@click.group()
def share() -> None:
    pass


LOADING = "loading the database..."
HEADERS = ("index", "name")
FORMAT = "simple_grid"


def level_name(level: CreatedLevelAPI) -> str:
    return level.name


@click.help_option("--help", "-h")
@share.command()
def list() -> None:
    click.echo(LOADING)

    database = save.load()

    levels = database.created_levels

    data = iter(levels).map(level_name).enumerate().list()

    click.echo(tabulate(data, HEADERS, FORMAT))


FILE_NAME = "{name}.level.gd"
file_name = FILE_NAME.format

DUMPED = "dumped `{index}` to `{name}`"
dumped = DUMPED.format


@click.help_option("--help", "-h")
@click.argument("index", type=int)
@share.command()
def dump(index: int) -> None:
    click.echo(LOADING)

    database = save.load()

    level = database.created_levels[index]

    name = file_name(name=level.name)

    dump_to(name, level)

    click.echo(dumped(index=index, name=name))


DUMPING = "dumping the database..."

LOADED = "loaded `{path}`"
loaded = LOADED.format

FIRST = 0


@click.help_option("--help", "-h")
@click.argument("path", type=Path)
@share.command()
def load(path: Path) -> None:
    level = load_from(path, CreatedLevelAPI)

    click.echo(LOADING)

    database = save.load()

    database.created_levels.insert(FIRST, level)

    click.echo(DUMPING)

    database.dump()

    click.echo(loaded(path=path))
