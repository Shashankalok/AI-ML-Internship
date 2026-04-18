from tools.logger import log_info


def route_after_critic(state):
    """
    Routing logic after critic agent
    """

    status = state.get("status")

    log_info(f" Routing decision based on status: {status}")

    # Retry loop
    if status == "retry":
        return "analyzer"

    # Approved → move forward
    if status == "approved":
        return "writer"

    # Pprevents system crash
    log_info(" Unknown status → defaulting to writer")

    return "writer"