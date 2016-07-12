# elm-package-for-production

Wrap around elm-package with config options so you don't have to duplicate everything all the time. Look at [this example file](example/prod_elm_package.json) for an idea on the additional config stuff.


Usage:

- `--app` will compile the app
- `--tests` will compile the tests

```
(py3)Noahs-MacBook-Pro:example noah$ python ../prod_package.py --app
Packages configured successfully!
Success! Compiled 0 modules.
Packages configured successfully!
Success! Compiled 1 module.
Successfully generated build/main.js
(py3)Noahs-MacBook-Pro:example noah$ python ../prod_package.py --test
Packages configured successfully!
Success! Compiled 0 modules.
Packages configured successfully!
Success! Compiled 2 modules.
Successfully generated _elm_tests.js
```
