from datetime import datetime
from fastapi import Request


async def audit_log_transaction(request: Request, call_next):
    action = f"{request.method} {request.url.path}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_ip = request.client.host
    query_params = dict(request.query_params)
    path_params = dict(request.path_params)

    log_message = f"""{timestamp} - Action: {action}, IP: {client_ip}
                      Query Parameters: {query_params}
                      Path Parameters: {path_params}
                  """

    with open("audit_log_transaction.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_message + "\n")

    response = await call_next(request)
    return response
