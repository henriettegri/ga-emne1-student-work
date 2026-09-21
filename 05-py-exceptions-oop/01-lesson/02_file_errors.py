from pathlib import Path
# data_folder = Path("..").parent.parent - ("..") - gå et nivå ut, en relative path

#dunder = dobbelunderscore, en absoluttpath
data_folder = Path(__file__).parent.parent /"data"
#Hvor finner jeg fila
path = data_folder/ "message.txt"

#opprette fil ved å høyreklikke new-file

# printe pathen
print(path)

#åpne fil

try:
    #with open(path, "r", encoding="utf-8") as file:
    #en annen måte å åpne på, kan droppe r siden r er default
    with path.open("r", encoding="utf-8") as file:
        message = file.read()
    print(message)
except FileNotFoundError:
    print(f"Error, could not open file: {path}")

path = data_folder/ "number.txt"
print(path)

try:
    with path.open(encoding="utf-8") as file:
        number = int(file.read().strip())
    print(number*2)
except FileNotFoundError:
    print(f"Error, could not open file: {path}")
except ValueError:
    print("The file must contain an integer")