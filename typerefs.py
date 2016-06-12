import clang.cindex
from clang_config import *
import os

clang.cindex.Config.set_library_file(CLANG_LIBRARY_FILE)
index = clang.cindex.Index.create()


def main():
    cpp_filename = 'cppfiles\\type_example.cpp'
    assert(os.path.exists(cpp_filename))
    tu = index.parse(cpp_filename, CLANG_CXXFLAGS)

if __name__ == '__main__':
    main()
