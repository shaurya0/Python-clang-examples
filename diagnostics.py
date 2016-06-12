import clang.cindex
import sys
from clang_config import *


clang.cindex.Config.set_library_file(CLANG_LIBRARY_FILE)
index = clang.cindex.Index.create()


def print_diagnostics(translation_unit):
    diagnostics = translation_unit.diagnostics
    for d in diagnostics:
        print(d)


def main():
    filename = sys.argv[1]
    tu = index.parse(filename, CLANG_CXXFLAGS)
    print_diagnostics(tu)


if __name__ == '__main__':
    main()
