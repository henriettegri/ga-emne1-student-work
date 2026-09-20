from pathlib import Path

print(f'Current directory is {Path.cwd()}')

data_directory = Path() / "data"
support_path = data_directory / "supporthenvendelser.csv"

print(data_directory)
print(data_directory.exists())

print(support_path)
print(support_path.exists())

print("\n---\n")

with open(support_path, "r", encoding="utf-8") as file:
    content = file.read()
print(content)
