from scripts.automation import run_automation


def test_automation():
    assert run_automation() is True
