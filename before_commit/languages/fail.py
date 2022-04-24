from __future__ import annotations

from typing import Sequence

from before_commit.hook import Hook
from before_commit.languages import helpers

ENVIRONMENT_DIR = None
get_default_version = helpers.basic_get_default_version
healthy = helpers.basic_healthy
install_environment = helpers.no_install


def run_hook(
        hook: Hook,
        file_args: Sequence[str],
        color: bool,
) -> tuple[int, bytes]:
    out = f'{hook.entry}\n\n'.encode()
    out += b'\n'.join(f.encode() for f in file_args) + b'\n'
    return 1, out