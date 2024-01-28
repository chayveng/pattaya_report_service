@echo off
title EX-PROJECT
call .\venv\Scripts\activate

set APP_MODULE=main:app
set HOST=0.0.0.0
set PORT=19909

call uvicorn %APP_MODULE% --host %HOST% --port %PORT%