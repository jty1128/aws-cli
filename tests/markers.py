import platform

import pytest

_SKIP_IF_WINDOWS_REASON = "This test does not run on windows."
_IF_WINDOWS_REASON = "This test only runs on windows."


def skip_if_windows(reason=_SKIP_IF_WINDOWS_REASON):
    if callable(reason):
        return pytest.mark.skipif(
            platform.system() not in ['Darwin', 'Linux'],
            reason=_SKIP_IF_WINDOWS_REASON,
        )(reason)
    return pytest.mark.skipif(
        platform.system() not in ['Darwin', 'Linux'],
        reason=reason,
    )


def if_windows(reason=_IF_WINDOWS_REASON):
    if callable(reason):
        return pytest.mark.skipif(
            platform.system() in ['Darwin', 'Linux'],
            reason=_IF_WINDOWS_REASON,
        )(reason)
    return pytest.mark.skipif(
        platform.system() in ['Darwin', 'Linux'],
        reason=reason,
    )
