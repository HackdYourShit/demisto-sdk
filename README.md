[![PyPI version](https://badge.fury.io/py/demisto-sdk.svg)](https://badge.fury.io/py/demisto-sdk)
[![CircleCI](https://circleci.com/gh/demisto/demisto-sdk/tree/master.svg?style=svg)](https://circleci.com/gh/demisto/demisto-sdk/tree/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ppwwyyxx/OpenPano.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/demisto/demisto-sdk/context:python)
[![Coverage Status](https://coveralls.io/repos/github/demisto/demisto-sdk/badge.svg)](https://coveralls.io/github/demisto/demisto-sdk)

# Demisto SDK

The Demisto SDK library can be used to manage your Demisto content with ease and efficiency.
The library uses python 3.7+.

## Usage

### Installation

1. **Install** - `pip3 install demisto-sdk`

2. **Upgrade** - `pip3 install --upgrade demisto-sdk`

3. **Demisto server demisto-sdk integration** - In order that demisto-sdk and Demisto server communicate, perfrom the following steps:

   1. Get an API key for Demisto-server - `Settings` -> ` Integrations` -> `API keys` -> `Get your Key` (copy it, you will be to copy it once)
   2. Add the following parameters to `~/.zshrc` and `~/.bash_profile`:

   ```shell
   export DEMISTO_BASE_URL=<http or https>://<demisto-server url or ip>:<port>
   export DEMISTO_API_KEY=<API key>
   ```

   for example:

   ```shell
   export DEMISTO_BASE_URL=http://127.0.0.1:8080
   export DEMISTO_API_KEY=XXXXXXXXXXXXXXXXXXXXXX
   ```

   3. Reload your terminal before continue.

---

### CLI usage

You can use the SDK in the CLI as follows:

```shell
demisto-sdk <command> <args>
```

For more information, run `demisto-sdk -h`.
For more information on a specific command execute `demisto-sdk <command> -h`.

----

## Commands

Supported commands:

1. [init](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md)
2. [Validate](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md)
3. [Lint](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/lint/README.md)
4. [Secrets](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/secrets/README.md)
5. [Unify](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/unify/README.md)
6. [Split-yml](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/split_yml/README.md)
7. [Create](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/create_artifacts/README.md)
8. [Format](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/format/README.md)
9. [Run](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/run_cmd/README.md)
10. [Run-playbook](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/run_playbook/README.md)
11. [Upload](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/upload/README.md)
12. [Download](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/download/README.md)
13. [Generate-docs](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/generate_docs/README.md)
14. [Generate-test-playbook](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/generate_test_playbook/README.md)
15. [Json-to-outputs](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/json_to_outputs/README.md)
16. [Create-id-set](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/create_id_set/README.md)
17. [Update-release-notes](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/update_release_notes/README.md)

---

### How to run commands in your development environment
In the Demisto-SDK repository while on the git branch you want to activate and run this command to use python 3.7:
 ```
 source .tox/py37/bin/activate
 ```
or this command to use python 3.8:

For detailed command usage press [here](demisto_sdk/commands/upload/README.md)

---

### Autocomplete

Our CLI supports autocomplete for Linux/MacOS machines, you can turn this feature on by running one of the following:
for zsh users run in the terminal

```shell
eval "$(_DEMISTO_SDK_COMPLETE=source_zsh demisto-sdk)"
```

for regular bashrc users run in the terminal

```shell
eval "$(_DEMISTO_SDK_COMPLETE=source demisto-sdk)"
```

---

## License
MIT - See [LICENSE](LICENSE) for more information.

---

## Contributions
Contributions are welcome and appreciated.\
For information regarding contributing, press [here](CONTRIBUTION.md).
For release guide, press [here](docs/release_guide.md)
