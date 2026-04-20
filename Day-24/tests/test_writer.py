from agents.writer import writer_agent

def test_writer_agent():
    input_text = "Financial risk involves uncertainty in returns."
    
    result = writer_agent(input_text)
    
    assert isinstance(result, str)
    assert len(result) > 0