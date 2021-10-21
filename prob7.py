sir=input("Dati un sir la dorinta: ")
sir1_final=""
sir2_final=""
sir3_final=""
aparitii_A=sir.count("A")
print(f"NUmarul de aparitii ale caracterului A in sir este : {aparitii_A}")
for litera in sir:
    if ord(litera)==65:
        litera=chr(ord("*"))
    sir1_final+=litera
print(f"Sirul obtinut prin substituirea caracterului A prin caracterul * este : {sir1_final}")
for litera in sir:
    if ord(litera)==66:
        litera=""
    sir2_final+=litera
print(f"Sirul obtinut prin radierea din sir a tuturor aparitiilor caracterului B este : {sir2_final}")
nr_silabe_MA=sir.count("MA")
print(f"Numarul de aparitii ale silabei MA in sir este {nr_silabe_MA}")
sir3_final=sir.replace("MA","TA")
print(f"Sirul obtinut prin substituirea tuturor aparitiilor in sir a silabei MA prin silaba TA este : {sir3_final}")
sir4_final=sir.replace("TO","")
print(f"Sirul obtinut prin radierea din sir a tuturor aparitiilor silabei TO este : {sir4_final}")
print(f"Scrierea inversa a sirului este: {sir[::-1]}")
