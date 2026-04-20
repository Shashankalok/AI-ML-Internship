from agents.critic import critic_agent

def test_critic_agent():
    input_text = "This is a simple explanation of financial risk."
    
    result = critic_agent(input_text)
    
    assert isinstance(result, str)
    assert len(result) > 0
