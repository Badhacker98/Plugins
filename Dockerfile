FROM debian:11
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install \
    git python3 python3-dev python3-pip python3-venv ffmpeg
RUN pip3 install --upgrade pip
WORKDIR /Pbx
COPY requirements.txt ./requirements.txt
RUN pip3 install flask
RUN pip3 install -r requirements.txt
COPY mogenius.sh mogenius.sh
COPY webapp.py webapp.py
EXPOSE 5000
RUN chmod 777 /Pbx/mogenius.sh
ENTRYPOINT ["./mogenius.sh"]
