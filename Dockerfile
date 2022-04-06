FROM python:3.8

# Pegar versao do chrome
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#########

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get -y install 	google-chrome-stable nano

RUN mkdir /root/.ssh
ENV TZ=America/Sao_Paulo
WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3 -u application.py" ]