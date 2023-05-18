*** settings ***
Library     REST    http://127.0.0.1:8000

*** test cases ***
testrequest
    GET     /api/v1/users
    String      $[0].firstname  jeff
    Integer     $[0].age        18