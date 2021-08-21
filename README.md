# Blockchain Template

## Preface

This repository is designed for [Blockchain Environment](https://github.com/kazutoiris/blockchain_env).

Three files you need to care: `eth.sol`, `custom.py`, `Dockerfile`.

## Usage

+ In `Dockerfile`

  You need to specify the version of `solc`.

  ```dockerfile
  ENV tag_name="v0.5.10"
  ```

+ In `eth.sol`

  You need to specify the version of `solc`.

  ```solidity
  pragma solidity ^0.5.10;
  ```

+ In `custom.py`

  You need to implement `get_url`, `check`, `code` function.

  + get_url

    return: `HTTP/WSS`, `url`, `Chain ID`, `isPoA`

    | KEY      | TYPE      | VALUE                                         |
    | -------- | --------- | --------------------------------------------- |
    | HTTP/WSS | BOOL      | True means HTTP/HTTPS, False means WebSocket. |
    | url      | String    | JSON-RPC Address                              |
    | Chain ID | Int (Dec) | The Chain ID in Decimal.                      |
    | isPoA    | BOOL      | True means PoA, False means PoW.              |

  + check

    param: `acct`, `tx_hash`, `cont_if`

    | KEY     | TYPE    | VALUE                               |
    | ------- | ------- | ----------------------------------- |
    | acct    | ACCOUNT | User’s Account                      |
    | tx_hash | String  | Transaction that achieved the goal. |
    | cont_if | CONT_IF | Compile of sol file                 |

    return: True means Pass, False means Fail.

  + code

    param: `public`

    True means the code show to the competition, False means the code used to deploy.

    If you don’t want competition know the source code, just return empty string in *True* condition.

    If you want to randomize the source code, random it in *False* condition.

    return: String

## Final

Feel free to pull requests or create an issue.

