# Usage

## Glossary

- *database* is the collective term for Geometry Dash save files.

## Options

- `--help (-h)` displays help information.
- `--version (-V)` shows the application version.

## `list`

`list` command is used to list all the levels in the database.

```console
$ gd.share list
loading the database...
```

Below is the table representation of the result:

| `index` | `name`      |
|--------:|-------------|
| `0`     | `Bloodbath` |

## `dump`

`dump` command dumps the level at specified `index` from the database.

```console
$ gd.share dump 0
loading the database...
dumped `0` to `Bloodbath.level.gd`
```

## `load`

`load` command loads the level at specified `path` into the database.

```console
$ gd.share load Bloodbath.level.gd
loading the database...
dumping the database...
loaded `Bloodbath.level.gd`
```
