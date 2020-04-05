from unittest.mock import patch

import pytest
from demisto_sdk.commands.common.constants import TYPE_PWSH, TYPE_PYTHON


@patch('builtins.print')
@pytest.mark.parametrize(argnames="return_exit_code, skipped_code, pkgs_type",
                         argvalues=[(0b0, 0b0, [TYPE_PWSH, TYPE_PYTHON])])
def test_report_pass_lint_checks(mocker, return_exit_code: int, skipped_code: int, pkgs_type: list):
    from demisto_sdk.commands.lint import lint_manager
    lint_manager.LintManager.report_pass_lint_checks(return_exit_code, skipped_code, pkgs_type)
    assert mocker.call_count == 8
