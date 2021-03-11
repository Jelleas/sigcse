import check50

@check50.check()
def compiles():
    """hello compiles"""
    check50.run("clang hello.c -o hello").exit(0)