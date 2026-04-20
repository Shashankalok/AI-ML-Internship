from agents.coordinator import coordinator_agent

def test_full_workflow():
    query = "What is financial risk?"
    
    result = coordinator_agent(query)
    
    assert isinstance(result, str)
    assert len(result) > 0
    assert "final" in result.lower() or "report" in result.lower()