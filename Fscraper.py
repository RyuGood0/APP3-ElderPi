def get_counties():
    file = open('list_of_countries.txt').read()
    
    temp = []
    
    for line in file.split('\n'):
        line = "".join(word+' ' for word in line.split() if word.lower() not in ['\n', '\r','drapeau','du','de',"l'","la","le"])
        line = line[2:] if line[0:2] == "l'" else line
        line = line.replace(',','.')

        
        sline = line.split()
        temp.append(sline)
    return temp
        
def remove_duplicates(list):
    return list[:1] + [item for item in list[1:] if item not in list[:1]]
print(remove_duplicates(get_counties()))
#
