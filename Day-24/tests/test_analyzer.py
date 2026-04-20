from agents.analyzer import analyzer_agent

def test_analyzer_agent():
    input_text = "Financial risk is the possibility of losing money."
    
    result = analyzer_agent(input_text)
    
    assert isinstance(result, str)
    assert len(result) > 0