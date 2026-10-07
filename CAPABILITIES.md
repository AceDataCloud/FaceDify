# Face Transform capability mapping

Compared with [MCPs at f0eed10abf31](https://github.com/AceDataCloud/MCPs/tree/f0eed10abf310824cb4c33d4944c63d3654ac95b/face) and the public API contract at PlatformBackend `fa94598267a82545fb1afed6ee26bafd6cbb9ca7`.

The table maps service operations to Dify tools. Different MCP helper functions may use the same action selector or structured JSON input.

| MCP function | Dify equivalent | Notes |
|---|---|---|
| `face_detect_keypoints` | `face_transform` | Select action=keypoints |
| `face_beautify` | `face_transform` | Select action=beautify |
| `face_change_age` | `face_transform` | Select action=age |
| `face_change_gender` | `face_transform` | Select action=gender |
| `face_swap` | `face_transform` | Select action=swap |
| `face_cartoonize` | `face_transform` | Select action=cartoon |
| `face_detect_liveness` | `face_transform` | Select action=liveness |
| `face_get_usage_guide` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |

## Parameter equivalents


## Verification boundary

Contract examples and regression tests cover request validation, transport and task handling. Actual Dify browser cases are recorded separately in `tests/e2e-results.json` and `tests/e2e-audit.json` when available. A schema test is not a successful paid generation. Unsupported service availability and untested advanced combinations must not be described as passed.
