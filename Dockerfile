FROM python:2.7

# Add sample application
ADD application.py /tmp/application.py
COPY requirements.txt /usr/src/app/
COPY ./aem-apps-file/* /usr/src/app/
COPY ./aem-apps-file/Archive /usr/src/app/Archive
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
RUN apt-get update
RUN yes | apt-get install zip unzip
RUN python3 /usr/src/app/__push-publisher.py

EXPOSE 5000

# Run it
ENTRYPOINT ["python", "/tmp/application.py"]
