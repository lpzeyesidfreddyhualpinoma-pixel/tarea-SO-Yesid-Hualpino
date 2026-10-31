import threading
import queue
import time
import random

cola_docs = queue.Queue()
conteo_trabajadores = {}
lock_mutex = threading.Lock()

for num_doc in range(1, 25):
    cola_docs.put((num_doc, random.randint(1, 3)))

def procesar_documentos(nombre_trabajador):
    while True:
        try:
            doc_id, duracion = cola_docs.get_nowait()
        except queue.Empty:
            break
            
        time.sleep(duracion * 0.1)
        cola_docs.task_done()
        
        with lock_mutex:
            conteo_trabajadores[nombre_trabajador] = conteo_trabajadores.get(nombre_trabajador, 0) + 1

lista_trabajadores = ["candia", "pablo", "arturo", "ricardo"]
hilos_activos = []

for persona in lista_trabajadores:
    t = threading.Thread(target=procesar_documentos, args=(persona,))
    hilos_activos.append(t)
    t.start()

for t in hilos_activos:
    t.join()

print("\n--- RESUMEN FINAL ---")
total_procesados = 0
for persona, docs in conteo_trabajadores.items():
    print(f"{persona}: {docs} documentos")
    total_procesados += docs

print(f"\nTotal general: {total_procesados}")