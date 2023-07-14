import os
import subprocess
import shutil

def komprimiere_video(datei_pfad, ziel_datei_pfad):
    # Komprimiere das Video mit ffmpeg über die subprocess-Bibliothek
    print(f"Komprimiere {datei_pfad}...") # Fortschritt anzeigen
    ziel_datei_pfad_mp4 = os.path.splitext(ziel_datei_pfad)[0] + '.mp4'
    kommando = ['ffmpeg', '-i', datei_pfad, '-crf', '28', ziel_datei_pfad_mp4]  # -crf: Qualität höher = min 0, niedriger = max 51
    subprocess.run(kommando, capture_output=True, text=True)  # capture_output=True, text=True: Ausgabe in der Konsole anzeigen

def komprimiere_ordnerstruktur(quellpfad, zielpfad): 
    for ordnername, unterordner, dateien in os.walk(quellpfad): 
        # Erzeuge den Zielordner, wenn er nicht vorhanden ist
        zielordner = os.path.join(zielpfad, os.path.relpath(ordnername, quellpfad))
        if not os.path.exists(zielordner):
            os.makedirs(zielordner)

        # Komprimiere und kopiere jede Videodatei in den Zielordner
        for index, datei in enumerate(dateien, start=1):
            datei_pfad = os.path.join(ordnername, datei)
            ziel_datei_pfad = os.path.join(zielordner, datei)
            if os.path.exists(ziel_datei_pfad): # 
                print(f"Die Zieldatei {ziel_datei_pfad} existiert bereits. Überspringe das Komprimieren.")
            else:
                if datei.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm')): # Nur Dateien mit diesen Endungen komprimieren
                    komprimiere_video(datei_pfad, ziel_datei_pfad)
                else:
                    # Kopiere andere Dateien einfach in den Zielordner
                    shutil.copy2(datei_pfad, ziel_datei_pfad)
            # Fortschritt anzeigen
            prozent = int(index / len(dateien) * 100) # Berechne den Fortschritt in Prozent
            print(f"Fortschritt des Ordners: {prozent}%") # Zeige den Fortschritt in der Konsole an

# Beispielaufruf
quellpfad = 'Quelle'  # Ordner, der komprimiert werden soll
zielpfad = 'Ziel'  # Ordner, in den die komprimierten Videos kopiert werden sollen

komprimiere_ordnerstruktur(quellpfad, zielpfad)
