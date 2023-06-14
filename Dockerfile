FROM python:3.11.4-slim-bullseye
WORKDIR /tests_project
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY tests/ .
CMD ["python", "-m", "pytest"]