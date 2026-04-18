from typing import TypedDict, Optional
import pandas as pd


class AgentState(TypedDict):
    file_path: str
    data: Optional[pd.DataFrame]
    processed_data: Optional[pd.DataFrame]

  
    analysis: Optional[dict]

    final_output: Optional[str]
    report_json: Optional[dict]

    status: str
    message: Optional[str]
    retry_count: int