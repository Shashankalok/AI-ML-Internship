def coordinator(state):
    status = state.get("status")

    if status == "start":
        return {"next": "researcher"}

    if status == "data_loaded":
        return {"next": "analyzer"}

    if status == "analyzed":
        return {"next": "critic"}

    if status == "approved":
        return {"next": "writer"}

    return {"next": "end"}