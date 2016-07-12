from elm_package import *
import json
import os

example_elm_package = open("example/prod_elm_package.json").read()
example_json = json.loads(example_elm_package)

def setup():
    return ProductionPackage(example_json)

def test_test_extensions():
    package = setup().test_package

    assert all(dir in package.source_directories for dir in ['test', 'src'])
    assert package.entry_point == 'test/Test.elm'
    assert all(dep in package.dependencies for dep in ['elm-community/elm-test', 'elm-lang/core'])

def test_app_extensions():
    package = setup().app_package

    assert 'build' == package.output_dir
    assert all(entry in package.entry_points for entry in ['src/Main.elm'])


def main():
    test_test_extensions()
    test_app_extensions()
    package = setup()

if __name__ == '__main__':
    main()

