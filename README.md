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

## Motivation

A lot of Elm code has a file directory that looks like this:

- `elm-package.json`
- `src`
- `test/elm-package.json`

Both the elm-package.jsons _should_ be almost exactly the same, except the test one will just add the test deps and sources. So, this generates an actual `elm-package.json` on the fly, compiles the code, then deletes the `elm-package.json`. This will help your production code be more reliable and save your ops team heartache.
