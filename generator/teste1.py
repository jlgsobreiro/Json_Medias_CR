from pymongo import MongoClient
from randomHeroGenerator import randomHero

client = MongoClient("127.0.0.1",27017)
bd = client["local"]
lista = list

collection = bd["local"]
#uniqueCollection = bd["unique"]

post = {"Nome": "Zaion",
        "Level": 69,
        "Classe": "Warrior",
        "Raça": "Gnomo"}








#for i in range(0,900000,1):
#    collection.insert_one(randomHero())

#for g in collection.find({}): #Apaga registro de nome com menos de 3 digitos
#    if(len(g["Nome"])<3):
#        collection.delete_one(g)

#for g in collection.find({}): #Apaga registro com Level maior que 25
#    if(g["Level"]>25):
#        collection.delete_one(g)

#x = 0
#for g in collection.find({}):
#    x+=1
#    print(x)
#    uniqueCollection.update({"Nome": g["Nome"]},{"$set":{"Nome": g["Nome"],"Level": g["Level"],"Classe": g["Classe"],"Raça": g["Raça"]}}, upsert = True)
