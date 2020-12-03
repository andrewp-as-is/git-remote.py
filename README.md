<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/git-remote.svg?maxAge=3600)](https://pypi.org/project/git-remote/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/git-remote.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/git-remote.py/actions)

### Installation
```bash
$ [sudo] pip install git-remote
```

#### Examples
```python
>>> import git_remote
>>> git_remote.add("github","git@github.com:owner/repo.git")
>>> git_remote.remotes()
[['github', 'git@github.com:owner/repo.git']]

>>> git_remote.names()
['github']

>>> git_remote.urls()
['git@github.com:owner/repo.git']

>>> git_remote.set_url("github","git@github.com:owner/repo2.git")
>>> git_remote.rm("github")
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
