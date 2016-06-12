from clang_config import *
import clang.cindex
import os

clang.cindex.Config.set_library_file(CLANG_LIBRARY_FILE)
index = clang.cindex.Index.create()


def print_type_info(translation_unit, file_handle, locations):
    print('type info for: ' + str(file_handle))
    for loc in locations:
        location = clang.cindex.SourceLocation().from_position(
            translation_unit, file_handle, loc[0], loc[1])
        cursor = clang.cindex.Cursor.from_location(translation_unit, location)
        print(cursor.type.spelling, cursor.kind)


def print_definition_locations(translation_unit, file_handle, locations):
    for loc in locations:
        location = clang.cindex.SourceLocation().from_position(
            translation_unit, file_handle, loc[0], loc[1])
        cursor = clang.cindex.Cursor.from_location(translation_unit, location)
        definition = cursor.get_definition()
        print('definition : ' + str(definition.location))


def main():
    header_filename = 'cppfiles\\type_example.h'
    cpp_filename = 'cppfiles\\type_example.cpp'
    assert(os.path.exists(cpp_filename))
    tu = index.parse(cpp_filename, CLANG_CXXFLAGS)
    cpp_file_handle = tu.get_file(cpp_filename)
    CPP_LOCATIONS = [(26, 30), (28, 42), (29, 14)]
    print_type_info(tu, cpp_file_handle, CPP_LOCATIONS)

    header_file_handle = tu.get_file(header_filename)
    HEADER_LOCATIONS = [(15, 22)]
    print_type_info(tu, header_file_handle, HEADER_LOCATIONS)

    DEFINTION_LOCATIONS = [(28, 34), (29, 14)]
    print_definition_locations(tu, cpp_file_handle, DEFINTION_LOCATIONS)


if __name__ == '__main__':
    main()
