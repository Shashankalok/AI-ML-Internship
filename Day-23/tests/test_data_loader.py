from tools.data_loader import load_data


def test_load_data():
    df = load_data("data/sample/creditcard.csv")

    assert df is not None
    assert len(df) > 0
    assert "amount" in df.columns
    assert "class" in df.columns