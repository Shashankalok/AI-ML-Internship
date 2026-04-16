from fastapi import Request
import time

async def log_requests(request: Request, call_next):
    start_time = time.time()

    # Before request
    print(f" {request.method} {request.url}")

    response = await call_next(request)

    # After request
    process_time = time.time() - start_time
    print(f" Status: {response.status_code} | Time: {process_time:.4f}s")

    return response