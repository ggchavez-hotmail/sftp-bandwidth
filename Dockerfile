FROM python:3.11.5-slim-bullseye AS develop

RUN apt-get update && \
    apt-get install -y ssh && \
    ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD src/. .

ENV SFTPHOSTNAME=VALUE
ENV SFTPPORT=VALUE
ENV SFTPUSERNAME=VALUE
ENV SFTPPASSWORD=VALUE
ENV SFTPLOCALFILE=VALUE
ENV SFTPREMOTEPATH=VALUE

#Comando para ejecutar proceso principal
CMD ["python", "main.py"]