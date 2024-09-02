import paramiko
import time
import os

def measure_upload_bandwidth(hostname, port, username, password, local_file, remote_path):
    # Conectar al servidor SFTP
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Medir el tiempo de inicio
    start_time = time.time()

    # Subir el archivo
    sftp.put(local_file, remote_path)

    # Medir el tiempo de finalización
    end_time = time.time()

    # Calcular el tiempo total de transferencia
    total_time = end_time - start_time

    # Obtener el tamaño del archivo en bytes
    file_size = os.path.getsize(local_file)

    # Calcular el ancho de banda en Mbps
    bandwidth_mbps = (file_size * 8) / (total_time * 1024 * 1024)

    # Cerrar la conexión SFTP
    sftp.close()
    transport.close()

    return bandwidth_mbps

# Parámetros de conexión
hostname    = os.environ["SFTPHOSTNAME"]
port        = int(os.environ["SFTPPORT"])
username    = os.environ["SFTPUSERNAME"]
password    = os.environ["SFTPPASSWORD"]
local_file  = os.environ["SFTPLOCALFILE"]
remote_path = os.environ["SFTPREMOTEPATH"]

print(f"hostname   : {hostname}") 
print(f"port       : {port}") 
print(f"username   : {username}") 
print(f"password   : {password}") 
print(f"local_file : {local_file}") 
print(f"remote_path: {remote_path }") 

# Medir el ancho de banda
bandwidth = measure_upload_bandwidth(hostname, port, username, password, local_file, remote_path)
print(f"Ancho de banda de subida: {bandwidth:.2f} Mbps")
