module Test exposing (..)

import Main
import ElmTest exposing (..)

main =
    test "true" (assert True)
        |> runSuite
