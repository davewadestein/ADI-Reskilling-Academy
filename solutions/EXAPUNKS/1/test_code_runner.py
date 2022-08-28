from code_runner import run_instruction

def test_run_instruction():
    import pytest

    with pytest.raises(Exception):
        run_instruction(['INVALID'])
