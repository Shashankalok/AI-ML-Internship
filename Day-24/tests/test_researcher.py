from agents.researcher import researcher_agent

def test_researcher_agent():
    result = researcher_agent("What is financial risk?")
    
    assert isinstance(result, str)
    assert len(result) > 0