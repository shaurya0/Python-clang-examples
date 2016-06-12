import clang.cindex
from clang_config import *
import os

clang.cindex.Config.set_library_file(CLANG_LIBRARY_FILE)
index = clang.cindex.Index.create()
COMPLETION_LINE_COL = [(23, 14), (18, 12)]


def print_completions(translation_unit, filename, line, col, predicate=None):
    code_complete = translation_unit.codeComplete(filename, line, col)
    for r in code_complete.results:
        if predicate is None:
            print(r)
        elif predicate(r):
            print(r)


def available_predicate(completion_result):
    expected_kind = clang.cindex.availabilityKinds[0]
    return completion_result.string.availability is expected_kind


def class_method_predicate(completion_result):
    return completion_result.kind is clang.cindex.CursorKind.CXX_METHOD


def main():
    filenames = ['cppfiles\\code_completion_example1.cpp',
                 'cppfiles\\code_completion_example2.cpp']

    for file, (line, col) in zip(filenames, COMPLETION_LINE_COL):
        assert(os.path.exists(file))
        tu = index.parse(file, CLANG_CXXFLAGS)
        print_completions(tu, file, line, col)


if __name__ == '__main__':
    main()
