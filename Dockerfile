FROM mcr.microsoft.com/playwright/python:v1.61.0
WORKDIR /framework
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["pytest", "-sv"]