FROM python:3.9

WORKDIR /app

COPY ai_autoscaler/ /app/

RUN pip install google-cloud-container fbprophet pandas flask

CMD ["python", "autoscaler.py"]
