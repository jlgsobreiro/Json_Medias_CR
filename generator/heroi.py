class heroi:
    nome = ""
    raca = ""
    level = ""
    classe = ""

    forca = 0
    destreza = 0
    constituicao = 0
    inteligencia = 0
    sabedoria = 0
    carisma = 0

    Pforca = False
    Pdestreza = False
    Pconstituicao = False
    Pinteligencia = False
    Psabedoria = False
    Pcarisma = False

    def Modificador(atributo):
        modificador = int(atributo / 2) - 5
        return modificador

    Acrobacia = Modificador(destreza) if Pdestreza else 0
    Arcanismo = Modificador(inteligencia) if Pinteligencia else 0
    Atletismo = Modificador(forca) if Pforca else 0
    Atuacao = Modificador(carisma) if Pcarisma else 0
    Blefar = Modificador(carisma) if Pcarisma else 0
    Furtividade = Modificador(destreza) if Pdestreza else 0
    Historia = Modificador(inteligencia) if Pinteligencia else 0
    Intimidacao = Modificador(carisma) if Pcarisma else 0
    Intuicao = Modificador(sabedoria) if Psabedoria else 0
    Investigacao = Modificador(inteligencia) if Pinteligencia else 0
    LidarComAnimais = Modificador(sabedoria) if Psabedoria else 0
    Medicina = Modificador(sabedoria) if Psabedoria else 0
    Natureza = Modificador(inteligencia) if Pinteligencia else 0
    Percepcao = Modificador(sabedoria) if Psabedoria else 0
    Persuasao = Modificador(carisma) if Pcarisma else 0
    Prestidigitacao = Modificador(destreza) if Pdestreza else 0
    Religiao = Modificador(inteligencia) if Pinteligencia else 0
    Sobrevivencia = Modificador(sabedoria) if Psabedoria else 0

    classeArmadura = 0
    deslocamento = 0
    pontosDeVida = 0
    pontosDeVidaTemporarios = 0

    inventario = list
