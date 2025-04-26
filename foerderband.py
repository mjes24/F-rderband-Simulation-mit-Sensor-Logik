def main():
    running = False

    print("📦 Förderband-Steuerung gestartet")
    while True:
        command = input("Befehl eingeben (start/stop/exit): ").lower()

        if command == "start":
            running = True
            print("⚙️ Förderband läuft...")
        elif command == "stop":
            running = False
            print("🛑 Förderband gestoppt.")
        elif command == "exit":
            print("Programm beendet.")
            break
        else:
            print("Ungültiger Befehl.")

        if running:
            sensor = input("📡 Sensor erkennt Objekt? (ja/nein): ").lower()
            if sensor == "ja":
                print("✅ Objekt erkannt – Weiterleitung aktiviert.")
            else:
                print("❌ Kein Objekt erkannt – Förderband läuft weiter.")
            print("---")

if __name__ == "__main__":
    main()
