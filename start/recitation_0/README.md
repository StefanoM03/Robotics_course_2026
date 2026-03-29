# Installazione e Avvio dell'Ambiente ROS 2 con Docker

Questo metodo utilizza un container pre-configurato che trasmette l'interfaccia grafica direttamente nel browser web. Bypassa i problemi di permessi (schermo/scheda video) tipici di Docker Desktop su Linux, creando un ambiente isolato e stabile.

### Description
1. Creazione e Primo Avvio (Da eseguire UNA SOLA VOLTA)

Apri il terminale sul tuo computer host e lancia il seguente comando. Q
uesto scaricherà l'immagine, mapperà la cartella di lavoro corrente e avvierà il container in background:

```
docker run -d \
  --pull always \
  -p 6080:80 \
  -p 9090:9090 \
  --security-opt seccomp=unconfined \
  --shm-size=512m \
  -v "/home/stefano-milantoni/Documents/GitHub/Robotics_course_2026:/github" \
  --name racademy \
  voss01dev/racademy:amd64
```
  
    Nota sul Volume (-v): Il percorso /home/stefano-milantoni/Documents/GitHub/Robotics_course_2026 
    è collegato alla cartella /github all'interno del container. 
    Le modifiche fatte ai file sul computer host si rifletteranno istantaneamente nel simulatore.

2. Accesso all'Interfaccia Grafica

Una volta avviato il container, l'ambiente Desktop non si aprirà come una normale finestra di Ubuntu, ma sarà accessibile tramite browser.

    Apri un browser web.

    Naviga all'indirizzo: http://localhost:6080

    Usa il terminale presente nel desktop virtuale per lanciare i comandi ROS 2 e Gazebo (sp
    ostandoti prima nella cartella di lavoro con cd /github).

3. Comandi di Gestione

Dopo aver creato il container la prima volta, non usare più il comando lungo in alto. Utilizza invece questi comandi per la gestione quotidiana:

Fermare il container (a fine sessione di studio):


    docker stop racademy

Riavviare il container (per le sessioni successive):

    docker start racademy
 
Una volta avviato, ricarica semplicemente la pagina web http://localhost:6080 per rientrare.

Entrare nel terminale del container dall'host (opzionale):
Se preferisci usare il terminale nativo di Ubuntu invece di quello nel browser, puoi "entrare" nel container con questo comando:
  

    docker exec -it --user ubuntu racademy bash

Dentro il **Desktop Virtuale** 

    cd /github

Per Gazebo

    ign gazebo






