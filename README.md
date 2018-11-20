[![](https://img.shields.io/pypi/pyversions/git-remote.svg?longCache=True)](https://pypi.org/pypi/git-remote/)
[![](https://img.shields.io/pypi/v/git-remote.svg?maxAge=3600)](https://pypi.org/pypi/git-remote/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/git-remote.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/git-remote.py/)

#### Install
```bash
$ [sudo] pip install git-remote
```

#### Functions
function|description
-|-
`git_remote.add(name, url)`|`git remote add name url`
`git_remote.names()`|return git remote names
`git_remote.remotes()`|return list of git remote tuples (name, url)
`git_remote.remove(name)`|`git remote rm name`
`git_remote.rename(old, new)`|`git remote rename old new`
`git_remote.rm(name)`|`git remote rm name`
`git_remote.run(args)`|run `git remote` with args and return output
`git_remote.set_url(name, url)`|`git remote set-url old new`
`git_remote.urls()`|return git remote urls

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>