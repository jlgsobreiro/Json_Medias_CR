import urllib.request


url = "https://gist.githubusercontent.com/leonardocordeiro/0f3c4c548117a69b15c6268d6feef735/raw/2c87fd06120d4cc0494ae57197740a91f77bb991/gistfile1.txt"
uf = urllib.request.urlopen(url)
html = uf.read()

estrutura = [{ "semestre" : "", "codigo" : "", "nome" : "", "av1" : 0, "av2" : 0, "av3" : 0, "media" : 0 }]

linha = []
texto = str(html)
print(texto)
formatado = (texto.replace("\""," ").replace(" ","").replace("semestre:","").replace("codigo:","").replace("nome:","").replace("av1:","").replace("av2:","").replace("av3:","").replace("media:",""))
texto = formatado
y = 0
for x in range(len(texto)) :
    if texto[x] == "{":
       linha.insert(len(linha),texto[y:x].replace("}","").replace("{","").split(","))
       y=x

print(linha[3])
estr = []
for x in len(linha):
    for n in len(estrutura):
        print(linha[x][n])