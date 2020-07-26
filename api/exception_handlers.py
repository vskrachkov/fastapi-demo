from fastapi import status, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def server_error_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": [{"msg": "Internal server error"}]},
    )


async def http_exception_handler(
    request: Request, exc: HTTPException
) -> JSONResponse:
    headers = getattr(exc, "headers", None)
    if headers:
        return JSONResponse(
            {"detail": [{"msg": exc.detail}]},
            status_code=exc.status_code,
            headers=headers,
        )
    else:
        return JSONResponse(
            {"detail": [{"msg": exc.detail}]}, status_code=exc.status_code
        )
