import builtins
from main import coordinator_agent

def test_main_input(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "Test query")
    
    result = coordinator_agent("Test query")
    
    assert isinstance(result, str)