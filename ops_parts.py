import subprocess
import os
import errno


def run_elm_make(root_folder, *args):
    from subprocess import call
    os.chdir(root_folder)

    call(["elm-package", "install", "--yes"])

    elm_make_options = ['elm-make']

    if args:
        elm_make_options.extend(args)

    call(elm_make_options)

def clean_elm_package_file():
    os.remove('elm-package.json')


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
