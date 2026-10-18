"""Thin Code Ocean entry point for the decrosstalk session split.

All logic lives in the ``aind-ophys-decrosstalk-split-session-json-library``
package; this wrapper only parses settings (CLI / environment) and invokes
``run``.
"""

from aind_ophys_decrosstalk_split_session_json_library.job import run

if __name__ == "__main__":
    run()
