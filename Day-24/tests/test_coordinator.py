from agents.coordinator import coordinator_agent

def test_coordinator_agent():
    result = coordinator_agent("Explain financial fraud")
    
    assert isinstance(result, str)
    assert len(result) > 0