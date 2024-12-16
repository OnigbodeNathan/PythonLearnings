#Virus.bat
def virus(file_path):
    with open(file_path, 'w') as file:
        empty = file.write('')
        return empty
    
file_path = "include.docx"
print( virus(file_path))