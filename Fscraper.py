import copy
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
        
def remove_duplicates(values):
    names = copy.deepcopy(values)
    for i in range(len(names)):
        temp = []
        for j in range(len(names[i])-8):
            if names[i][j] not in temp:
                temp.append(values[i][j])
        names[i] = temp
    
    
    for i in range(len(values)):
        
        temp = []
        for j in range(len(values[i])-8,len(values[i])):
            
            temp.append(values[i][j])
        values[i] = temp
    
    for item in range(len(names)):
        
        if len(names[item]) != 1:
            names[item] = ["".join(element+ ' ' for element in names[item])]
            
            
    return [names, values]


def list_to_dict(both_lists):
    combined_dict = {}

    names = both_lists[0]
    values = both_lists[1]

    for name,value in zip(names,values):
        combined_dict["".join(name)] = value
    open('countries_dict.txt','w').write(str(combined_dict))
    return combined_dict


import json
def all_countries():
    f = open("countries_dict.json", "r")
    raw_dict = json.load(f)
    to_export = "(" + "".join(key + " | " for key in raw_dict.keys()) + ")"
    print(to_export)
all_countries()

