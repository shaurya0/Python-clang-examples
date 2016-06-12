import clang.cindex
from clang_config import *
import os

clang.cindex.Config.set_library_file(CLANG_LIBRARY_FILE)
index = clang.cindex.Index.create()


MAX_RECURSION_DEPTH = 20
def walk_preorder(cursor):
    wp = next(cursor.walk_preorder())
    print(wp.spelling)
    walk_preorder(wp)



def main():
    cpp_filename = 'cppfiles\\type_example.cpp'
    assert(os.path.exists(cpp_filename))
    tu = index.parse(cpp_filename, CLANG_CXXFLAGS)
    walk_preorder(tu.cursor)

if __name__ == '__main__':
    main()
