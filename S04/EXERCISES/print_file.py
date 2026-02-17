from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "../SEQUENCES/ADA.txt"
# FILENAME = "../../" es para coger un archivo de S02 por ejemplo, porque tienes que salir de dos carpetas

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)
