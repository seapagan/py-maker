# Changelog

This is an auto-generated log of all the changes that have been made to the
project since the first release.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [v0.13.0](https://github.com/seapagan/py-maker/releases/tag/v0.13.0) (October 07, 2024)

This is a security release to fix several vulnerabilities in dependency packages.

We also migrate from `Poetry` to `uv` for dependency management.

**Merged Pull Requests**

- Lower dependabot check frequency in template to weekly ([#433](https://github.com/seapagan/py-maker/pull/433)) by [seapagan](https://github.com/seapagan)

**New Features**

- Migrate to using `uv` for dependency management ([#516](https://github.com/seapagan/py-maker/pull/516)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps-dev): bump pre-commit from 3.7.1 to 3.8.0 ([#470](https://github.com/seapagan/py-maker/pull/470)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump simple-toml-settings from 0.6.1 to 0.7.0 ([#469](https://github.com/seapagan/py-maker/pull/469)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Update ruff and fix errors and warnings ([#468](https://github.com/seapagan/py-maker/pull/468)) by [seapagan](https://github.com/seapagan)
- Build(deps): bump validators from 0.28.3 to 0.33.0 ([#460](https://github.com/seapagan/py-maker/pull/460)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump rtoml from 0.10.0 to 0.11.0 ([#449](https://github.com/seapagan/py-maker/pull/449)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump github-changelog-md from 0.9.3 to 0.9.4 ([#444](https://github.com/seapagan/py-maker/pull/444)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump urllib3 from 2.2.1 to 2.2.2 ([#443](https://github.com/seapagan/py-maker/pull/443)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 25.1.0 to 25.4.0 ([#432](https://github.com/seapagan/py-maker/pull/432)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pymarkdownlnt from 0.9.19 to 0.9.20 ([#431](https://github.com/seapagan/py-maker/pull/431)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump requests from 2.31.0 to 2.32.3 ([#430](https://github.com/seapagan/py-maker/pull/430)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 12 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.12.0...v0.13.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.12.0...v0.13.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.12.0...v0.13.0.patch)

## [v0.12.0](https://github.com/seapagan/py-maker/releases/tag/v0.12.0) (May 08, 2024)

**New Features**

- Only ask for repo name if we are creating a git repo ([#405](https://github.com/seapagan/py-maker/pull/405)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Validate urls inputed by the user ([#406](https://github.com/seapagan/py-maker/pull/406)) by [seapagan](https://github.com/seapagan)

**Refactoring**

- Refactor the main `Pymaker` class ([#404](https://github.com/seapagan/py-maker/pull/404)) by [seapagan](https://github.com/seapagan)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.11.0...v0.12.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.11.0...v0.12.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.11.0...v0.12.0.patch)

## [v0.11.0](https://github.com/seapagan/py-maker/releases/tag/v0.11.0) (May 07, 2024)

**Closed Issues**

- Several instances in the generated `pyproject.toml` still point to the `py_maker` folder. ([#387](https://github.com/seapagan/py-maker/issues/387)) by [seapagan](https://github.com/seapagan)
- Initial update to `.pre-commit.yaml` should be added to the git repo if applicable ([#386](https://github.com/seapagan/py-maker/issues/386)) by [seapagan](https://github.com/seapagan)
- Tests crash on a newly created project ([#385](https://github.com/seapagan/py-maker/issues/385)) by [seapagan](https://github.com/seapagan)

**New Features**

- Ensure a second commit is created if the pre-commit is updated ([#398](https://github.com/seapagan/py-maker/pull/398)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Fix some 'py_maker' folder references ending up in the generated projects ([#396](https://github.com/seapagan/py-maker/pull/396)) by [seapagan](https://github.com/seapagan)
- Fix Tests crash on a newly created project ([#395](https://github.com/seapagan/py-maker/pull/395)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps): bump rtoml from 0.9.0 to 0.10.0 ([#402](https://github.com/seapagan/py-maker/pull/402)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump typer from 0.9.4 to 0.12.3 ([#401](https://github.com/seapagan/py-maker/pull/401)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Update multiple deps to latest versions ([#400](https://github.com/seapagan/py-maker/pull/400)) by [seapagan](https://github.com/seapagan)
- Update pre-commit to latest tools ([#399](https://github.com/seapagan/py-maker/pull/399)) by [seapagan](https://github.com/seapagan)
- Build(deps-dev): bump ruff from 0.4.2 to 0.4.3 ([#394](https://github.com/seapagan/py-maker/pull/394)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump simple-toml-settings from 0.6.0 to 0.6.1 ([#393](https://github.com/seapagan/py-maker/pull/393)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 25.0.0 to 25.0.1 ([#392](https://github.com/seapagan/py-maker/pull/392)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pygments from 2.17.2 to 2.18.0 ([#391](https://github.com/seapagan/py-maker/pull/391)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocstrings from 0.25.0 to 0.25.1 ([#390](https://github.com/seapagan/py-maker/pull/390)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.5.20 to 9.5.21 ([#389](https://github.com/seapagan/py-maker/pull/389)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 1 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.10.3...v0.11.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.10.3...v0.11.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.10.3...v0.11.0.patch)

## [v0.10.3](https://github.com/seapagan/py-maker/releases/tag/v0.10.3) (May 01, 2024)

This is a security release to fix several vulnerabilities in dependency packages.

**Dependency Updates**

- Build(deps-dev): bump pymarkdownlnt from 0.9.18 to 0.9.19 ([#383](https://github.com/seapagan/py-maker/pull/383)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-git-revision-date-localized-plugin from 1.2.4 to 1.2.5 ([#382](https://github.com/seapagan/py-maker/pull/382)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump poethepoet from 0.25.0 to 0.26.1 ([#381](https://github.com/seapagan/py-maker/pull/381)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 24.4.0 to 25.0.0 ([#380](https://github.com/seapagan/py-maker/pull/380)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pytest-xdist from 3.5.0 to 3.6.1 ([#379](https://github.com/seapagan/py-maker/pull/379)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.5.17 to 9.5.20 ([#378](https://github.com/seapagan/py-maker/pull/378)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pytest from 8.1.1 to 8.2.0 ([#377](https://github.com/seapagan/py-maker/pull/377)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocstrings from 0.24.2 to 0.25.0 ([#375](https://github.com/seapagan/py-maker/pull/375)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pymdown-extensions from 10.7.1 to 10.8.1 ([#374](https://github.com/seapagan/py-maker/pull/374)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump ruff from 0.3.5 to 0.4.2 ([#371](https://github.com/seapagan/py-maker/pull/371)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 20 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.10.2...v0.10.3) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.10.2...v0.10.3.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.10.2...v0.10.3.patch)

## [v0.10.2](https://github.com/seapagan/py-maker/releases/tag/v0.10.2) (March 13, 2024)

**Closed Issues**

- License name is missing in the generated README ([#321](https://github.com/seapagan/py-maker/issues/321)) by [seapagan](https://github.com/seapagan)
- The templates for some generated files need updating ([#320](https://github.com/seapagan/py-maker/issues/320)) by [seapagan](https://github.com/seapagan)

**New Features**

- Add pytest watcher task ([#326](https://github.com/seapagan/py-maker/pull/326)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Fix some bugs in the template files and update obsolete information ([#325](https://github.com/seapagan/py-maker/pull/325)) by [seapagan](https://github.com/seapagan)
- Fix missing license name in generated README ([#324](https://github.com/seapagan/py-maker/pull/324)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps): bump pydantic from 2.6.3 to 2.6.4 ([#323](https://github.com/seapagan/py-maker/pull/323)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.10.1...v0.10.2) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.10.1...v0.10.2.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.10.1...v0.10.2.patch)

## [v0.10.1](https://github.com/seapagan/py-maker/releases/tag/v0.10.1) (March 12, 2024)

**Closed Issues**

- Empty string for 'homepage' in `pyproject.html` crashes Poetry ([#317](https://github.com/seapagan/py-maker/issues/317)) by [seapagan](https://github.com/seapagan)

**Testing**

- Add unit tests for the `Settings` module ([#310](https://github.com/seapagan/py-maker/pull/310)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Fix bug where bad homepage field crashes `poetry install` ([#318](https://github.com/seapagan/py-maker/pull/318)) by [seapagan](https://github.com/seapagan)

**Refactoring**

- Convert settings module to use new `get_settings()` method ([#309](https://github.com/seapagan/py-maker/pull/309)) by [seapagan](https://github.com/seapagan)

**Documentation**

- Update Docs to mention previous linting changes ([#305](https://github.com/seapagan/py-maker/pull/305)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps): bump simple-toml-settings from 0.5.0 to 0.6.0 ([#316](https://github.com/seapagan/py-maker/pull/316)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mypy from 1.8.0 to 1.9.0 ([#315](https://github.com/seapagan/py-maker/pull/315)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump types-requests from 2.31.0.20240218 to 2.31.0.20240311 ([#314](https://github.com/seapagan/py-maker/pull/314)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pytest from 8.1.0 to 8.1.1 ([#313](https://github.com/seapagan/py-maker/pull/313)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 24.0.0 to 24.1.0 ([#312](https://github.com/seapagan/py-maker/pull/312)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump ruff from 0.3.1 to 0.3.2 ([#311](https://github.com/seapagan/py-maker/pull/311)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump simple-toml-settings from 0.4.0 to 0.5.0 ([#307](https://github.com/seapagan/py-maker/pull/307)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump ruff from 0.3.0 to 0.3.1 ([#306](https://github.com/seapagan/py-maker/pull/306)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.10.0...v0.10.1) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.10.0...v0.10.1.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.10.0...v0.10.1.patch)

## [v0.10.0](https://github.com/seapagan/py-maker/releases/tag/v0.10.0) (March 06, 2024)

**Closed Issues**

- When missing the config file, it does not properly read the users Git username/email ([#291](https://github.com/seapagan/py-maker/issues/291)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Fix bug in post create-file hook ([#300](https://github.com/seapagan/py-maker/pull/300)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps-dev): bump mkdocs-material from 9.5.12 to 9.5.13 ([#303](https://github.com/seapagan/py-maker/pull/303)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pymdown-extensions from 10.7 to 10.7.1 ([#302](https://github.com/seapagan/py-maker/pull/302)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 23.3.0 to 24.0.0 ([#301](https://github.com/seapagan/py-maker/pull/301)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.9.5...v0.10.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.9.5...v0.10.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.9.5...v0.10.0.patch)

## [v0.9.5](https://github.com/seapagan/py-maker/releases/tag/v0.9.5) (March 04, 2024)

**Closed Issues**

- For standalone app, the suggested GitHub URL is wrong, it should be the same as if the app was a package ([#296](https://github.com/seapagan/py-maker/issues/296)) by [seapagan](https://github.com/seapagan)
- Template deps need updating and template config files need a freshening ([#294](https://github.com/seapagan/py-maker/issues/294)) by [seapagan](https://github.com/seapagan)
- Standalone app should have the ending text changed. ([#293](https://github.com/seapagan/py-maker/issues/293)) by [seapagan](https://github.com/seapagan)
- If creating a standalone, `poetry install` should set 'package-mode=false' in the pyproject.toml ([#292](https://github.com/seapagan/py-maker/issues/292)) by [seapagan](https://github.com/seapagan)

**Merged Pull Requests**

- Fix formatting to new Ruff 3.0 ([#289](https://github.com/seapagan/py-maker/pull/289)) by [seapagan](https://github.com/seapagan)

**New Features**

- Update deps and template, freshen the template config files. ([#297](https://github.com/seapagan/py-maker/pull/297)) by [seapagan](https://github.com/seapagan)

**Testing**

- Continue writing tests. ([#267](https://github.com/seapagan/py-maker/pull/267)) by [seapagan](https://github.com/seapagan)
- Add a testing stage to CI with coverage reports from codacy ([#266](https://github.com/seapagan/py-maker/pull/266)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Ask for repo name and offer to create for both type of projects ([#298](https://github.com/seapagan/py-maker/pull/298)) by [seapagan](https://github.com/seapagan)
- Fix several issues with generating standalone projects ([#295](https://github.com/seapagan/py-maker/pull/295)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps-dev): bump pytest from 8.0.2 to 8.1.0 ([#290](https://github.com/seapagan/py-maker/pull/290)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump ruff from 0.2.1 to 0.3.0 ([#288](https://github.com/seapagan/py-maker/pull/288)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-autorefs from 0.5.0 to 1.0.1 ([#287](https://github.com/seapagan/py-maker/pull/287)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.5.9 to 9.5.12 ([#286](https://github.com/seapagan/py-maker/pull/286)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump rich from 13.7.0 to 13.7.1 ([#285](https://github.com/seapagan/py-maker/pull/285)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump pydantic from 2.6.1 to 2.6.3 ([#284](https://github.com/seapagan/py-maker/pull/284)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 23.2.0 to 23.3.0 ([#282](https://github.com/seapagan/py-maker/pull/282)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocstrings from 0.24.0 to 0.24.1 ([#281](https://github.com/seapagan/py-maker/pull/281)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pytest from 8.0.0 to 8.0.2 ([#280](https://github.com/seapagan/py-maker/pull/280)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump poethepoet from 0.24.4 to 0.25.0 ([#277](https://github.com/seapagan/py-maker/pull/277)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 35 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.9.4...v0.9.5) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.9.4...v0.9.5.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.9.4...v0.9.5.patch)

## [v0.9.4](https://github.com/seapagan/py-maker/releases/tag/v0.9.4) (December 11, 2023)

This is a security release that fixes a vulnerability in the 'cryptography'
package.

**Refactoring**

- Update pre commit config to use poetry-export-plugin directly ([#203](https://github.com/seapagan/py-maker/pull/203)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps-dev): bump mkdocs-material from 9.4.8 to 9.5.1 ([#216](https://github.com/seapagan/py-maker/pull/216)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump actions/stale from 8 to 9 ([#215](https://github.com/seapagan/py-maker/pull/215)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump ruff from 0.1.5 to 0.1.7 ([#214](https://github.com/seapagan/py-maker/pull/214)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump cryptography from 41.0.5 to 41.0.6 ([#213](https://github.com/seapagan/py-maker/pull/213)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pytest-xdist from 3.4.0 to 3.5.0 ([#209](https://github.com/seapagan/py-maker/pull/209)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pygments from 2.16.1 to 2.17.2 ([#208](https://github.com/seapagan/py-maker/pull/208)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 20.0.3 to 20.1.0 ([#206](https://github.com/seapagan/py-maker/pull/206)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump rich from 13.6.0 to 13.7.0 ([#202](https://github.com/seapagan/py-maker/pull/202)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocstrings from 0.23.0 to 0.24.0 ([#201](https://github.com/seapagan/py-maker/pull/201)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump poethepoet from 0.24.3 to 0.24.4 ([#200](https://github.com/seapagan/py-maker/pull/200)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 16 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.9.3...v0.9.4) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.9.3...v0.9.4.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.9.3...v0.9.4.patch)

## [v0.9.3](https://github.com/seapagan/py-maker/releases/tag/v0.9.3) (October 29, 2023)

**Refactoring**

- Run Ruff on github actions ([#174](https://github.com/seapagan/py-maker/pull/174)) by [seapagan](https://github.com/seapagan)
- Migrate linting and formatting to Ruff ([#173](https://github.com/seapagan/py-maker/pull/173)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps-dev): bump faker from 19.10.0 to 19.12.0 ([#172](https://github.com/seapagan/py-maker/pull/172)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump black from 23.10.0 to 23.10.1 ([#171](https://github.com/seapagan/py-maker/pull/171)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pylint from 3.0.1 to 3.0.2 ([#170](https://github.com/seapagan/py-maker/pull/170)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mypy from 1.6.0 to 1.6.1 ([#168](https://github.com/seapagan/py-maker/pull/168)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pylint-pytest from 1.1.2 to 1.1.3 ([#167](https://github.com/seapagan/py-maker/pull/167)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.9.2...v0.9.3) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.9.2...v0.9.3.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.9.2...v0.9.3.patch)

## [v0.9.2](https://github.com/seapagan/py-maker/releases/tag/v0.9.2) (October 24, 2023)

**Merged Pull Requests**

- Migrate to new changelog generator ([#165](https://github.com/seapagan/py-maker/pull/165)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps): bump simple-toml-settings from 0.2.2 to 0.3.0 ([#163](https://github.com/seapagan/py-maker/pull/163)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pymdown-extensions from 10.3 to 10.3.1 ([#162](https://github.com/seapagan/py-maker/pull/162)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pytest-mock from 3.11.1 to 3.12.0 ([#161](https://github.com/seapagan/py-maker/pull/161)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump black from 23.9.1 to 23.10.0 ([#160](https://github.com/seapagan/py-maker/pull/160)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump gitpython from 3.1.37 to 3.1.40 ([#159](https://github.com/seapagan/py-maker/pull/159)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump types-requests from 2.31.0.8 to 2.31.0.10 ([#158](https://github.com/seapagan/py-maker/pull/158)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump flake8-type-checking from 2.4.2 to 2.5.1 ([#157](https://github.com/seapagan/py-maker/pull/157)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump urllib3 from 2.0.6 to 2.0.7 ([#156](https://github.com/seapagan/py-maker/pull/156)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.4.5 to 9.4.6 ([#154](https://github.com/seapagan/py-maker/pull/154)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-git-revision-date-localized-plugin from 1.2.0 to 1.2.1 ([#152](https://github.com/seapagan/py-maker/pull/152)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 1 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.9.1...v0.9.2) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.9.1...v0.9.2.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.9.1...v0.9.2.patch)

## [v0.9.1](https://github.com/seapagan/py-maker/releases/tag/v0.9.1) (October 12, 2023)

**Bug Fixes**

- Remove extra '\_\_init\_\_.py' file ([#150](https://github.com/seapagan/py-maker/pull/150)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps-dev): bump faker from 19.8.0 to 19.10.0 ([#149](https://github.com/seapagan/py-maker/pull/149)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mypy from 1.5.1 to 1.6.0 ([#147](https://github.com/seapagan/py-maker/pull/147)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.9.0...v0.9.1) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.9.0...v0.9.1.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.9.0...v0.9.1.patch)

## [v0.9.0](https://github.com/seapagan/py-maker/releases/tag/v0.9.0) (October 10, 2023)

**Merged Pull Requests**

- Unlock 'poethepoet' upgrades ([#142](https://github.com/seapagan/py-maker/pull/142)) by [seapagan](https://github.com/seapagan)

**New Features**

- Migrate settings to my 'simple-toml-settings' library ([#146](https://github.com/seapagan/py-maker/pull/146)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps-dev): bump mkdocs-material from 9.4.4 to 9.4.5 ([#145](https://github.com/seapagan/py-maker/pull/145)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pylint from 2.17.7 to 3.0.1 ([#144](https://github.com/seapagan/py-maker/pull/144)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 19.6.2 to 19.8.0 ([#143](https://github.com/seapagan/py-maker/pull/143)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pylint-pydantic from 0.2.4 to 0.3.0 ([#139](https://github.com/seapagan/py-maker/pull/139)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.4.3 to 9.4.4 ([#138](https://github.com/seapagan/py-maker/pull/138)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump flake8-type-checking from 2.4.1 to 2.4.2 ([#137](https://github.com/seapagan/py-maker/pull/137)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump types-requests from 2.31.0.7 to 2.31.0.8 ([#136](https://github.com/seapagan/py-maker/pull/136)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.8.0...v0.9.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.8.0...v0.9.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.8.0...v0.9.0.patch)

## [v0.8.0](https://github.com/seapagan/py-maker/releases/tag/v0.8.0) (October 04, 2023)

**Merged Pull Requests**

- Add help to poe tasks ([#130](https://github.com/seapagan/py-maker/pull/130)) by [seapagan](https://github.com/seapagan)

**New Features**

- Automatically create a GitHub repository for the new project ([#134](https://github.com/seapagan/py-maker/pull/134)) by [seapagan](https://github.com/seapagan)

**Refactoring**

- Migrate tomli lib to rtoml ([#131](https://github.com/seapagan/py-maker/pull/131)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps-dev): bump mkdocs-material from 9.4.2 to 9.4.3 ([#133](https://github.com/seapagan/py-maker/pull/133)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump urllib3 from 2.0.4 to 2.0.6 ([#132](https://github.com/seapagan/py-maker/pull/132)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump rich from 13.5.3 to 13.6.0 ([#128](https://github.com/seapagan/py-maker/pull/128)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pylint from 2.17.6 to 2.17.7 ([#127](https://github.com/seapagan/py-maker/pull/127)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump types-requests from 2.31.0.6 to 2.31.0.7 ([#126](https://github.com/seapagan/py-maker/pull/126)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump poethepoet from 0.23.0 to 0.24.0 ([#125](https://github.com/seapagan/py-maker/pull/125)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.7.0...v0.8.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.7.0...v0.8.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.7.0...v0.8.0.patch)

## [v0.7.0](https://github.com/seapagan/py-maker/releases/tag/v0.7.0) (October 01, 2023)

**Merged Pull Requests**

- Improve typing across the package ([#115](https://github.com/seapagan/py-maker/pull/115)) by [seapagan](https://github.com/seapagan)
- Adjust suggested git repo name ([#103](https://github.com/seapagan/py-maker/pull/103)) by [seapagan](https://github.com/seapagan)

**New Features**

- Implement 'config edit' command ([#124](https://github.com/seapagan/py-maker/pull/124)) by [seapagan](https://github.com/seapagan)
- Add '--bare' option ([#123](https://github.com/seapagan/py-maker/pull/123)) by [seapagan](https://github.com/seapagan)
- Add '--standalone' CLI flag ([#113](https://github.com/seapagan/py-maker/pull/113)) by [seapagan](https://github.com/seapagan)
- Add optional  github_token setting ([#106](https://github.com/seapagan/py-maker/pull/106)) by [seapagan](https://github.com/seapagan)
- Store and use GitHub username ([#104](https://github.com/seapagan/py-maker/pull/104)) by [seapagan](https://github.com/seapagan)

**Documentation**

- Adjust and clarify some docs ([#114](https://github.com/seapagan/py-maker/pull/114)) by [seapagan](https://github.com/seapagan)
- Add a contributing guide ([#109](https://github.com/seapagan/py-maker/pull/109)) by [seapagan](https://github.com/seapagan)
- Add a POE Task to automatically create and update the CHANGELOG.md ([#107](https://github.com/seapagan/py-maker/pull/107)) by [seapagan](https://github.com/seapagan)
- Add MkDocs Tasks to the Documentation ([#105](https://github.com/seapagan/py-maker/pull/105)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps): bump pydantic from 2.3.0 to 2.4.2 ([#122](https://github.com/seapagan/py-maker/pull/122)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump types-requests from 2.31.0.4 to 2.31.0.6 ([#120](https://github.com/seapagan/py-maker/pull/120)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pylint from 2.17.5 to 2.17.6 ([#119](https://github.com/seapagan/py-maker/pull/119)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump types-requests from 2.31.0.3 to 2.31.0.4 ([#112](https://github.com/seapagan/py-maker/pull/112)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.4.0 to 9.4.2 ([#111](https://github.com/seapagan/py-maker/pull/111)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump poethepoet from 0.22.1 to 0.23.0 ([#110](https://github.com/seapagan/py-maker/pull/110)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.6.2...v0.7.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.6.2...v0.7.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.6.2...v0.7.0.patch)

## [v0.6.2](https://github.com/seapagan/py-maker/releases/tag/v0.6.2) (September 24, 2023)

**Closed Issues**

- --version flag does not work. ([#101](https://github.com/seapagan/py-maker/issues/101)) by [seapagan](https://github.com/seapagan)

**Merged Pull Requests**

- Add poe tasks for documentation if mkdocs enabled ([#100](https://github.com/seapagan/py-maker/pull/100)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Fix #101 (--version flag does not work) ([#102](https://github.com/seapagan/py-maker/pull/102)) by [seapagan](https://github.com/seapagan)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.6.1...v0.6.2) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.6.1...v0.6.2.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.6.1...v0.6.2.patch)

## [v0.6.1](https://github.com/seapagan/py-maker/releases/tag/v0.6.1) (September 23, 2023)

**Merged Pull Requests**

- Update tool versions in both pre-commit configs ([#99](https://github.com/seapagan/py-maker/pull/99)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Fix typos and wording in the generated readme ([#98](https://github.com/seapagan/py-maker/pull/98)) by [seapagan](https://github.com/seapagan)

**Documentation**

- Remove dependency spam from changelog ([#97](https://github.com/seapagan/py-maker/pull/97)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps): bump gitpython from 3.1.36 to 3.1.37 ([#96](https://github.com/seapagan/py-maker/pull/96)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.3.2 to 9.4.0 ([#95](https://github.com/seapagan/py-maker/pull/95)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump types-requests from 2.31.0.2 to 2.31.0.3 ([#94](https://github.com/seapagan/py-maker/pull/94)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 19.6.1 to 19.6.2 ([#93](https://github.com/seapagan/py-maker/pull/93)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs from 1.5.2 to 1.5.3 ([#92](https://github.com/seapagan/py-maker/pull/92)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.3.1 to 9.3.2 ([#91](https://github.com/seapagan/py-maker/pull/91)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump rich from 13.5.2 to 13.5.3 ([#90](https://github.com/seapagan/py-maker/pull/90)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.6.0...v0.6.1) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.6.0...v0.6.1.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.6.0...v0.6.1.patch)

## [v0.6.0](https://github.com/seapagan/py-maker/releases/tag/v0.6.0) (September 14, 2023)

**New Features**

- Auto install and update 'pre commit' ([#88](https://github.com/seapagan/py-maker/pull/88)) by [seapagan](https://github.com/seapagan)
- Add code of conduct to project and the template ([#87](https://github.com/seapagan/py-maker/pull/87)) by [seapagan](https://github.com/seapagan)
- Add Github templates to the default output template ([#86](https://github.com/seapagan/py-maker/pull/86)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Build(deps): bump actions/stale from 5 to 8 ([#89](https://github.com/seapagan/py-maker/pull/89)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.5.1...v0.6.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.5.1...v0.6.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.5.1...v0.6.0.patch)

## [v0.5.1](https://github.com/seapagan/py-maker/releases/tag/v0.5.1) (September 12, 2023)

**New Features**

- Add --version command to CLI ([#63](https://github.com/seapagan/py-maker/pull/63)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Add missing 'requests' library to pyproject.toml ([#82](https://github.com/seapagan/py-maker/pull/82)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump faker from 19.6.0 to 19.6.1 ([#85](https://github.com/seapagan/py-maker/pull/85)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump gitpython from 3.1.35 to 3.1.36 ([#84](https://github.com/seapagan/py-maker/pull/84)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mkdocs-material from 9.2.8 to 9.3.1 ([#83](https://github.com/seapagan/py-maker/pull/83)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pymarkdownlnt from 0.9.13.3 to 0.9.13.4 ([#80](https://github.com/seapagan/py-maker/pull/80)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump faker from 19.3.1 to 19.6.0 ([#79](https://github.com/seapagan/py-maker/pull/79)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump black from 23.7.0 to 23.9.1 ([#78](https://github.com/seapagan/py-maker/pull/78)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pytest from 7.4.0 to 7.4.2 ([#77](https://github.com/seapagan/py-maker/pull/77)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump gitpython from 3.1.33 to 3.1.35 ([#76](https://github.com/seapagan/py-maker/pull/76)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pymarkdownlnt from 0.9.13 to 0.9.13.3 ([#74](https://github.com/seapagan/py-maker/pull/74)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mkdocs-material from 9.2.7 to 9.2.8 ([#73](https://github.com/seapagan/py-maker/pull/73)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 8 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.5.0...v0.5.1) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.5.0...v0.5.1.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.5.0...v0.5.1.patch)

## [v0.5.0](https://github.com/seapagan/py-maker/releases/tag/v0.5.0) (August 31, 2023)

**New Features**

- Ask for homepage & repository if not standalone ([#61](https://github.com/seapagan/py-maker/pull/61)) by [seapagan](https://github.com/seapagan)
- Update template toml and pre-commit deps ([#58](https://github.com/seapagan/py-maker/pull/58)) by [seapagan](https://github.com/seapagan)
- Override config options from command line ([#55](https://github.com/seapagan/py-maker/pull/55)) by [seapagan](https://github.com/seapagan)
- Check PyPI for existing packages ([#46](https://github.com/seapagan/py-maker/pull/46)) by [seapagan](https://github.com/seapagan)

**Bug Fixes**

- Fix unable to create standalone app ([#60](https://github.com/seapagan/py-maker/pull/60)) by [seapagan](https://github.com/seapagan)

**Refactoring**

- Override config options from command line ([#55](https://github.com/seapagan/py-maker/pull/55)) by [seapagan](https://github.com/seapagan)

**Documentation**

- Update docs for latest additions ([#59](https://github.com/seapagan/py-maker/pull/59)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump mkdocs-material from 9.2.3 to 9.2.6 ([#57](https://github.com/seapagan/py-maker/pull/57)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pymdown-extensions from 10.1 to 10.2.1 ([#56](https://github.com/seapagan/py-maker/pull/56)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pymdown-extensions from 10.1 to 10.2 ([#54](https://github.com/seapagan/py-maker/pull/54)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mkdocs-material from 9.2.3 to 9.2.5 ([#53](https://github.com/seapagan/py-maker/pull/53)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pydantic from 2.1.1 to 2.3.0 ([#52](https://github.com/seapagan/py-maker/pull/52)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump faker from 19.3.0 to 19.3.1 ([#51](https://github.com/seapagan/py-maker/pull/51)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mkdocs-material from 9.1.21 to 9.2.3 ([#50](https://github.com/seapagan/py-maker/pull/50)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mypy from 1.5.0 to 1.5.1 ([#45](https://github.com/seapagan/py-maker/pull/45)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.4.5...v0.5.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.4.5...v0.5.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.4.5...v0.5.0.patch)

## [v0.4.5](https://github.com/seapagan/py-maker/releases/tag/v0.4.5) (August 17, 2023)

**New Features**

- Work on the TODO list. See commits for details ([#44](https://github.com/seapagan/py-maker/pull/44)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump pytest-randomly from 3.14.0 to 3.15.0 ([#43](https://github.com/seapagan/py-maker/pull/43)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.4.4...v0.4.5) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.4.4...v0.4.5.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.4.4...v0.4.5.patch)

## [v0.4.4](https://github.com/seapagan/py-maker/releases/tag/v0.4.4) (August 15, 2023)

**New Features**

- Add mkdocs as an option ([#42](https://github.com/seapagan/py-maker/pull/42)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump poethepoet from 0.21.1 to 0.22.0 ([#41](https://github.com/seapagan/py-maker/pull/41)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pytest-randomly from 3.13.0 to 3.14.0 ([#40](https://github.com/seapagan/py-maker/pull/40)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.4.3...v0.4.4) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.4.3...v0.4.4.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.4.3...v0.4.4.patch)

## [v0.4.3](https://github.com/seapagan/py-maker/releases/tag/v0.4.3) (August 13, 2023)

**New Features**

- Tweak linting ([#39](https://github.com/seapagan/py-maker/pull/39)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump mypy from 1.4.1 to 1.5.0 ([#38](https://github.com/seapagan/py-maker/pull/38)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.4.2...v0.4.3) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.4.2...v0.4.3.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.4.2...v0.4.3.patch)

## [v0.4.2](https://github.com/seapagan/py-maker/releases/tag/v0.4.2) (August 10, 2023)

- Added a missing runtime dep (rtoml). It must have been in my venv but not in the `pyproject.toml` 🙄
[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.4.1...v0.4.2) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.4.1...v0.4.2.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.4.1...v0.4.2.patch)

## [v0.4.1](https://github.com/seapagan/py-maker/releases/tag/v0.4.1) (August 10, 2023)

- Fixed bug where the first-time config file gets the wrong default template path.
- Update the internal template `pyproject.toml` and `.pre-commit-config.yaml` to use latest dependencies
[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.4.0...v0.4.1) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.4.0...v0.4.1.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.4.0...v0.4.1.patch)

## [v0.4.0](https://github.com/seapagan/py-maker/releases/tag/v0.4.0) (August 10, 2023)

**New Features**

- Implement custom template additions ([#31](https://github.com/seapagan/py-maker/pull/31)) by [seapagan](https://github.com/seapagan)

**Refactoring**

- Implement custom template additions ([#31](https://github.com/seapagan/py-maker/pull/31)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump faker from 19.2.0 to 19.3.0 ([#37](https://github.com/seapagan/py-maker/pull/37)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pygments from 2.15.1 to 2.16.1 ([#36](https://github.com/seapagan/py-maker/pull/36)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mkdocs from 1.5.1 to 1.5.2 ([#35](https://github.com/seapagan/py-maker/pull/35)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump rich from 13.5.0 to 13.5.2 ([#34](https://github.com/seapagan/py-maker/pull/34)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mkdocs-minify-plugin from 0.7.0 to 0.7.1 ([#33](https://github.com/seapagan/py-maker/pull/33)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.3.0...v0.4.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.3.0...v0.4.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.3.0...v0.4.0.patch)

## [v0.3.0](https://github.com/seapagan/py-maker/releases/tag/v0.3.0) (July 30, 2023)

**New Features**

- Add a configuration file ([#30](https://github.com/seapagan/py-maker/pull/30)) by [seapagan](https://github.com/seapagan)
- Use conditional logic in templates ([#24](https://github.com/seapagan/py-maker/pull/24)) by [seapagan](https://github.com/seapagan)

**Refactoring**

- Use conditional logic in templates ([#24](https://github.com/seapagan/py-maker/pull/24)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump mkdocs-material from 9.1.19 to 9.1.21 ([#29](https://github.com/seapagan/py-maker/pull/29)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mkdocs from 1.4.3 to 1.5.1 ([#28](https://github.com/seapagan/py-maker/pull/28)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pylint from 2.17.4 to 2.17.5 ([#26](https://github.com/seapagan/py-maker/pull/26)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pydantic from 2.0.3 to 2.1.1 ([#22](https://github.com/seapagan/py-maker/pull/22)) by [dependabot[bot]](https://github.com/apps/dependabot)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.2.1...v0.3.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.2.1...v0.3.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.2.1...v0.3.0.patch)

## [v0.2.1](https://github.com/seapagan/py-maker/releases/tag/v0.2.1) (July 26, 2023)

**New Features**

- Add a documentation site ([#23](https://github.com/seapagan/py-maker/pull/23)) by [seapagan](https://github.com/seapagan)

**Documentation**

- Add a documentation site ([#23](https://github.com/seapagan/py-maker/pull/23)) by [seapagan](https://github.com/seapagan)

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.2.0...v0.2.1) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.2.0...v0.2.1.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.2.0...v0.2.1.patch)

## [v0.2.0](https://github.com/seapagan/py-maker/releases/tag/v0.2.0) (July 26, 2023)

**Refactoring**

- Move licenses out of template folder ([#21](https://github.com/seapagan/py-maker/pull/21)) by [seapagan](https://github.com/seapagan)
- Subclass the Rich prompt locally ([#20](https://github.com/seapagan/py-maker/pull/20)) by [seapagan](https://github.com/seapagan)

**Dependency Updates**

- Bump pytest-asyncio from 0.21.0 to 0.21.1 ([#19](https://github.com/seapagan/py-maker/pull/19)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump flake8-type-checking from 2.4.0 to 2.4.1 ([#18](https://github.com/seapagan/py-maker/pull/18)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump gitpython from 3.1.31 to 3.1.32 ([#17](https://github.com/seapagan/py-maker/pull/17)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pydantic from 2.0.2 to 2.0.3 ([#16](https://github.com/seapagan/py-maker/pull/16)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump mock from 5.0.2 to 5.1.0 ([#15](https://github.com/seapagan/py-maker/pull/15)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump faker from 18.11.2 to 19.2.0 ([#14](https://github.com/seapagan/py-maker/pull/14)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump poethepoet from 0.20.0 to 0.21.1 ([#12](https://github.com/seapagan/py-maker/pull/12)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pytest-reverse from 1.6.0 to 1.7.0 ([#10](https://github.com/seapagan/py-maker/pull/10)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump black from 23.3.0 to 23.7.0 ([#9](https://github.com/seapagan/py-maker/pull/9)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Bump pytest-randomly from 3.12.0 to 3.13.0 ([#8](https://github.com/seapagan/py-maker/pull/8)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 1 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.1.0...v0.2.0) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.1.0...v0.2.0.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.1.0...v0.2.0.patch)

## [v0.1.0](https://github.com/seapagan/py-maker/releases/tag/v0.1.0) (July 06, 2023)

**Merged Pull Requests**

- Add base app functionality ([#1](https://github.com/seapagan/py-maker/pull/1)) by [seapagan](https://github.com/seapagan)

**New Features**

- Customize or remove the Package layout ([#5](https://github.com/seapagan/py-maker/pull/5)) by [seapagan](https://github.com/seapagan)

**Refactoring**

- Refactor the src template layout and logic ([#2](https://github.com/seapagan/py-maker/pull/2)) by [seapagan](https://github.com/seapagan)

---
*This changelog was generated using [github-changelog-md](http://changelog.seapagan.net/) by [Seapagan](https://github.com/seapagan)*
