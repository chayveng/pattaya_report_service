from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware


class CORSMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, request: Request, response: Response):
        # response.headers["Access-Control-Allow-Origin"] = "*"
        # response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        # response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        # response.headers["Access-Control-Allow-Credentials"] = "true"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Credentials"] = "true"

        if request.method == "OPTIONS":
            return Response(content="", status_code=200)

        return await self.app(request, response)