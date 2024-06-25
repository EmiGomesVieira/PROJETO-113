import sys
import time
import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Verifique se o caminho do diretório está correto
from_dir = "C:/Users/eg200/Downloads"

if not os.path.exists(from_dir):
    print(f"Erro: O caminho {from_dir} não existe. Verifique o caminho e tente novamente.")
    sys.exit(1)

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    # Método chamado quando um arquivo é criado
    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado!")

    # Método chamado quando um arquivo é deletado
    def on_deleted(self, event):
        print(f"Opa! Alguém excluiu {event.src_path}!")

    # Método chamado quando um arquivo é modificado
    def on_modified(self, event):
        print(f"Olá!, {event.src_path} foi modificado")

    # Método chamado quando um arquivo é movido
    def on_moved(self, event):
        print(f"Alguém moveu {event.src_path} para {event.dest_path}")

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

# Exceção para KeyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()

# Espere que o observer finalize
observer.join()







