__all__ = ['add', 'run', 'remove', 'rm',
           'rename', 'set_url', 'remotes', 'names', 'urls']


import runcmd

"""
https://git-scm.com/docs/git-remote
"""


def run(args):
    """run `git remote` with args and return output"""
    return runcmd.run(["git", "remote"] + list(args))._raise().out


def add(name, url):
    """`git remote add name url`"""
    run(["add", name, url])


def remove(name):
    """`git remote rm name`"""
    run(["remove", name])


def rm(name):
    """`git remote rm name`"""
    run(["rm", name])


def rename(old, new):
    """`git remote rename old new`"""
    run(["rename", old, new])


def set_url(name, url):
    """`git remote set-url old new`"""
    return run(["set-url", name, url])


def remotes():
    """return a list of git remote tuples (name, url)"""
    result = []
    for l in run(["-v"]).splitlines():
        name, url, role = l.split()
        if "fetch" in role:
            result.append([name, url])
    return result


def names():
    """return git remote names"""
    return list(lambda name, url: name, remotes())


def urls():
    """return git remote urls"""
    return list(lambda name, url: url, remotes())
