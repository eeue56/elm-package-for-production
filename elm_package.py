import json
import ops_parts
# import typing

# ValidFieldTypes = typing.TypeVar('ValidFieldTypes', int, float, bool, str)

class Package(object):

    def __init__(self, package_json):
        self.version = package_json['version']
        self.summary = package_json['summary']
        self.has_native_code = package_json['native-modules']
        self.license = package_json["license"]
        self.exposed_modules =  package_json["exposed-modules"]
        self.elm_version = package_json["elm-version"]
        self.source_directories = package_json["source-directories"]
        self.dependencies = package_json['dependencies']
        self.repository = package_json['repository']

    def install(self, **kwargs):
        self.write_elm_package_file()
        ops_parts.run_elm_make('.')
        self.clean()

    def clean(self):
        ops_parts.clean_elm_package_file()

    def compile(self):
        self.install()

    def to_dict(self): # -> typing.Dict[str, ValidFieldTypes]:
        return {
            'version' : self.version,
            'summary' : self.summary,
            'native-modules' : self.has_native_code,
            'license' : self.license,
            'exposed-modules' : self.exposed_modules,
            'elm-version' : self.elm_version,
            'source-directories' : self.source_directories,
            'dependencies' : self.dependencies,
            'repository' : self.repository
        }

    def write_elm_package_file(self):
        self_as_dict = self.to_dict()

        with open('elm-package.json', 'w') as f:
            json.dump(self_as_dict, f, indent=4)


class ProductionAppPackage(Package):

    def __init__(self, package_json):
        Package.__init__(self, package_json)
        self.output_dir = package_json["output-dir"]
        self.entry_points = package_json['entry-points']

    def compile(self):
        Package.compile(self)
        Package.write_elm_package_file(self)

        if self.output_dir == '':
            raise "You really don't want to have an empty output dir"

        for entry_point in self.entry_points:
            out_file = self.output_dir + '/' + self.entry_points[entry_point]
            ops_parts.run_elm_make('.', entry_point, '--output', out_file)

        Package.clean(self)


class ProductionTestPackage(Package):

    def __init__(self, package_json):
        Package.__init__(self, package_json)
        self.source_directories.append(package_json['test-directory'])
        self.dependencies.update(package_json['test-deps'])
        self.entry_point = package_json['test-file']

    def compile(self):
        Package.compile(self)
        Package.write_elm_package_file(self)

        ops_parts.run_elm_make('.', self.entry_point, '--output', '_elm_tests.js')

        Package.clean(self)


class ProductionPackage(object):

    def __init__(self, package_json):
        self.app_package = ProductionAppPackage(package_json)
        self.test_package = ProductionTestPackage(package_json)



