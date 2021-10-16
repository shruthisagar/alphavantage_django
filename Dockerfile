FROM python:3.8.10-buster
RUN mkdir /src/
ADD . /src/
WORKDIR /src/
RUN pip install -r requirements.txt
RUN chmod +x /src/start_server.sh
USER root

CMD [ "/bin/sh", "/src/start_server.sh" ]