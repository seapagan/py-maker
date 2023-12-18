# Changelog

This is an auto-generated log of all the changes that have been made to the
project since the first release.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/seapagan/py-maker/tree/HEAD)

These are the changes that have been merged to the repository since the last
release. If you want to try out these changes, you can install the latest
version from the main branch by running:

```console
$ pip install git+https://github.com/seapagan/github-changelog-md
```

or, if using poetry:

```console
$ poetry add git+https://github.com/seapagan/github-changelog-md
```

Everything in this section will be included in the next official release.

**Dependency Updates**

- Build(deps-dev): bump ruff from 0.1.7 to 0.1.8 ([#228](https://github.com/seapagan/py-maker/pull/228)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pre-commit from 3.5.0 to 3.6.0 ([#227](https://github.com/seapagan/py-maker/pull/227)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump mkdocs-material from 9.5.1 to 9.5.2 ([#226](https://github.com/seapagan/py-maker/pull/226)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pymdown-extensions from 10.4 to 10.5 ([#225](https://github.com/seapagan/py-maker/pull/225)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump faker from 20.1.0 to 21.0.0 ([#224](https://github.com/seapagan/py-maker/pull/224)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump github/codeql-action from 2 to 3 ([#223](https://github.com/seapagan/py-maker/pull/223)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps): bump pydantic from 2.5.1 to 2.5.2 ([#222](https://github.com/seapagan/py-maker/pull/222)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pyfakefs from 5.3.1 to 5.3.2 ([#221](https://github.com/seapagan/py-maker/pull/221)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pymarkdownlnt from 0.9.14 to 0.9.15 ([#220](https://github.com/seapagan/py-maker/pull/220)) by [dependabot[bot]](https://github.com/apps/dependabot)
- Build(deps-dev): bump pytest-asyncio from 0.21.1 to 0.23.2 ([#219](https://github.com/seapagan/py-maker/pull/219)) by [dependabot[bot]](https://github.com/apps/dependabot)
- *and 1 more dependency updates*

[`Full Changelog`](https://github.com/seapagan/py-maker/compare/v0.9.4...HEAD) | [`Diff`](https://github.com/seapagan/py-maker/compare/v0.9.4...HEAD.diff) | [`Patch`](https://github.com/seapagan/py-maker/compare/v0.9.4...HEAD.patch)

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
