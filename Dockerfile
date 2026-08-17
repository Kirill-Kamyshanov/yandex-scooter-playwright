FROM mcr.microsoft.com/playwright/python:v1.62.0
WORKDIR /framework
COPY . .
RUN pip install uv && uv sync
ENTRYPOINT ["uv", "run", "pytest", "-sv"]