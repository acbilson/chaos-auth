FROM debian:10.2-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install vim python3 python3-pip -y
RUN pip3 install --upgrade setuptools wheel

WORKDIR /src
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["tail", "-f", "/dev/null"]
