# sftp-bandwidth #
## Instalación ##

Ejecutar comando para levantar ambiente python

```
pipenv shell
```

## Configurar variables ambiente ##

Crear variables ambiente

```
export SFTPHOSTNAME=VALUE
export SFTPPORT=VALUE
export SFTPUSERNAME=VALUE
export SFTPPASSWORD=VALUE
export SFTPLOCALFILE=VALUE
export SFTPREMOTEPATH=VALUE 
```

## Ejecución ##

Ejecutar directamente

```
python src/main.py
```

Ejecutar docker

```
#construir imagen
docker build --pull --rm -f "Dockerfile" -t sftp-bandwith:latest "sftp-bandwidth"

#ejecutar imagen
docker run --rm --name sftp_bandwith_test -e SFTPHOSTNAME=VALUE -e SFTPPORT=VALUE -e SFTPUSERNAME=VALUE -e SFTPPASSWORD=VALUE -e SFTPLOCALFILE=VALUE -e SFTPREMOTEPATH=VALUE sftp-bandwith:latest

#ver log
docker logs -f sftp_bandwith_test
```

