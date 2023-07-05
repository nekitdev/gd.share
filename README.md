![Image]

# `gd.share`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]

> *Sharing Geometry Dash levels through CLI.*

## Installing

**Python 3.7 or above is required.**

### pip

Installing the library with `pip` is quite simple:

```console
$ pip install gd.share
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/gd.share.git
$ cd gd.share
$ python -m pip install .
```

### poetry

You can add `gd.share` as a dependency with the following command:

```console
$ poetry add gd.share
```

Or by directly specifying it in the configuration like so:

```toml
[tool.poetry.dependencies]
"gd.share" = "^1.0.0"
```

Alternatively, you can add it directly from the source:

```toml
[tool.poetry.dependencies."gd.share"]
git = "https://github.com/nekitdev/gd.share.git"
```

## Compiling

Compiling an executable version of the `gd.share` library:

```console
$ pyinstaller --onefile --icon assets/gd.share.ico --exclude numpy --exclude PIL --exclude IPython --exclude Crypto gd.share.py
```

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send an [email][Email]
or refer to the official [Discord server][Discord].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `gd.share` [here][Security].

## Contributing

If you are interested in contributing to `gd.share`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`gd.share` is licensed under the MIT License terms. See [License][License] for details.

[Image]: https://github.com/nekitdev/gd.share/blob/main/assets/gd.share.svg?raw=true

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/discord

[Actions]: https://github.com/nekitdev/gd.share/actions

[Changelog]: https://github.com/nekitdev/gd.share/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/gd.share/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/gd.share/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/gd.share/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/gd.share/blob/main/LICENSE

[Package]: https://pypi.org/project/gd.share
[Documentation]: https://nekitdev.github.io/gd.share

[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2
[License Badge]: https://img.shields.io/pypi/l/gd.share
[Version Badge]: https://img.shields.io/pypi/v/gd.share
[Downloads Badge]: https://img.shields.io/pypi/dm/gd.share

[Documentation Badge]: https://github.com/nekitdev/gd.share/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/gd.share/workflows/check/badge.svg
