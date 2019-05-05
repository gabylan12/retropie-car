ARG architecture
FROM $architecture/python:2.7.13-jessie
WORKDIR /apps
COPY src/requirements.txt /apps
RUN pip install cryptography && pip install pipenv && pipenv install
RUN pip install -r /apps/requirements.txt
RUN pip install --no-cache-dir rpi.gpio
COPY src /apps
CMD ["sh","/apps/bootstrap.sh"]