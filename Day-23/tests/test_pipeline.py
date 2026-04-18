from main import run_pipeline


def test_pipeline():
    result = run_pipeline("data/sample/creditcard.csv")

    assert result is not None
    assert "final_output" in result