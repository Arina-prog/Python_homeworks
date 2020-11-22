names_1 = ['Annabel', 'Vardan', 'Nver', 'Nshan','Arev']

def get_names(num):
    return num, len(num) ,num[:3]
result = list(map(lambda name:(name,len(name),name[:2]), names_1))
result = list(map(get_names,names_1))
print(result)