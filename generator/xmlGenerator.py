from xml.dom import minidom
import os

heroi = minidom.Document()

xml = heroi.createElement("heroi")
heroi.appendChild(xml)

xmlP = "C:\\Users\\jl_so\\PycharmProjects\\mongoDB_Teste\\filename.xml"


def heroiCreate(nome, level, classe, raca):

    heroiNome = heroi.createElement("Nome")
    heroiNome.appendChild(heroi.createTextNode(nome))

    heroiClasse = heroi.createElement("Classe")
    heroiClasse.appendChild(heroi.createTextNode(classe))

    heroiRaca = heroi.createElement("Raca")
    heroiRaca.appendChild(heroi.createTextNode(raca))

    heroiLevel = heroi.createElement("Level")
    heroiLevel.appendChild(heroi.createTextNode(level))

    xml.appendChild(heroiNome)
    xml.appendChild(heroiLevel)
    xml.appendChild(heroiClasse)
    xml.appendChild(heroiRaca)

    xml_str = heroi.toprettyxml(indent="\t")

    with open(xmlP, "w") as f:
        f.write(xml_str)


def adicionaAoHeroi(node, atributo):

    item = heroi.getElementsByTagName(node)
    item.text = "asdads"

    xml_str = heroi.toprettyxml(indent="\t")
    with open(xmlP, "wp") as f:
        f.write(xml_str)
