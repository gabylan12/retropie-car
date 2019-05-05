ARG architecture
FROM $architecture/python:2.7.13-jessie
COPY src /apps
WORKDIR /apps
RUN pip install cryptography && pip install pipenv && pipenv install
RUN pip install -r /apps/requirements.txt
RUN pip install --no-cache-dir rpi.gpio
CMD ["sh","/apps/bootstrap.sh"]