from mysql.connector import connect

def obtemConexaoComMySQL (servidor, usuario, senha, bd):
    if obtemConexaoComMySQL.conexao==None:
        obtemConexaoComMySQL.conexao = \
        connect(host="127.0.0.1", user="root", passwd="root", database="buzziolbd")
    return obtemConexaoComMySQL.conexao
obtemConexaoComMySQL.conexao=None

padronizacao = 320

def calcularIndiceN1 (concFinal, concInicial, concMedida):
    indiceN1 = 0 + ((40 - 0)/(concFinal - concInicial)) * (concMedida - concInicial)
    return indiceN1

def calcularIndiceN2 (concFinal, concInicial, concMedida):
    indiceN2 = 41 + ((80 - 41)/(concFinal - concInicial)) * (concMedida - concInicial)
    return indiceN2

def calcularIndiceN3 (concFinal, concInicial, concMedida):
    indiceN3 = 81 + ((120 - 81)/(concFinal - concInicial)) * (concMedida - concInicial)
    return indiceN3

def calcularIndiceN4 (concFinal, concInicial, concMedida):
    indiceN4 = 121 + ((200 - 121)/(concFinal - concInicial)) * (concMedida - concInicial)
    return indiceN4

def calcularIndiceN5 (concInicial, concMedida):
    indiceN5 = 201 + ((padronizacao - 201)/(concMedida - concInicial)) * (concMedida - concInicial)
    return indiceN5

comando="select * from valores"
conexao=obtemConexaoComMySQL("127.0.0.1","root","root","buzziolbd")
cursor=conexao.cursor()
cursor.execute(comando)

todosValores = cursor.fetchall()

listaIndices = []

for tuplas in range(len(todosValores)):
    concMedidaMP10 = todosValores[tuplas][0]

    if 0 < concMedidaMP10 <= 50:
        listaIndices.append(calcularIndiceN1(50, 0, concMedidaMP10))
        print("MP 10 está classificada como N1 - Boa!")
    elif 50 < concMedidaMP10 <= 100:
        listaIndices.append(calcularIndiceN2(100, 50, concMedidaMP10))
        print("MP 10 está classificada como N2 - Moderada!")
    elif 100 < concMedidaMP10 <= 150:
        listaIndices.append(calcularIndiceN3(150, 100, concMedidaMP10))
        print("MP 10 está classificada como N3 - Ruim!")
    elif 150 < concMedidaMP10 <= 250:
        listaIndices.append(calcularIndiceN4(250, 150, concMedidaMP10))
        print("MP 10 está classificada como N4 - Muito Ruim!")
    elif concMedidaMP10 > 250:
        listaIndices.append(calcularIndiceN5(251, concMedidaMP10))
        print("MP 10 está classificada como N5 - Péssimo!")
        
    concMedidaMpFinas = todosValores[tuplas][1]

    if 0 < concMedidaMpFinas <= 25:
        listaIndices.append(calcularIndiceN1(25, 0, concMedidaMpFinas))
        print("MP 2.5 está classificada como N1 - Boa!")
    elif 25 < concMedidaMpFinas <= 50:
        listaIndices.append(calcularIndiceN2(50, 25, concMedidaMpFinas))
        print("MP 2.5 está classificada como N2 - Moderada!")
    elif 50 < concMedidaMpFinas <= 75:
        listaIndices.append(calcularIndiceN3(75, 50, concMedidaMpFinas))
        print("MP 2.5 está classificada como N3 - Ruim!")
    elif 75 < concMedidaMpFinas <= 125:
        listaIndices.append(calcularIndiceN4(125, 75, concMedidaMpFinas))
        print("MP 2.5 está classificada como N4 - Muito Ruim!")
    elif concMedidaMpFinas > 125:
        listaIndices.append(calcularIndiceN5(126, concMedidaMpFinas))
        print("MP 2.5 está classificada como N5 - Péssimo!")

    concMedidaOzonio = todosValores[tuplas][2]

    if 0 < concMedidaOzonio <= 100:
        listaIndices.append(calcularIndiceN1(100, 0, concMedidaOzonio))
        print("Ozônio está classificada como N1 - Boa!")
    elif 100 < concMedidaOzonio <= 130:
        listaIndices.append(calcularIndiceN2(130, 100, concMedidaOzonio))
        print("Ozônio está classificada como N2 - Moderada!")
    elif 130 < concMedidaOzonio <= 160:
        listaIndices.append(calcularIndiceN3(160, 130, concMedidaOzonio))
        print("Ozônio está classificada como N3 - Ruim!")
    elif 160 < concMedidaOzonio <= 200:
        listaIndices.append(calcularIndiceN4(200, 160, concMedidaOzonio))
        print("Ozônio está classificada como N4 - Muito Ruim!")
    elif concMedidaOzonio > 200:
        listaIndices.append(calcularIndiceN5(201, concMedidaOzonio))
        print("Ozônio está classificada como N5 - Péssimo!")

    concMedidaMonoxCarb = todosValores[tuplas][3]

    if 0 < concMedidaMonoxCarb <= 9:
        listaIndices.append(calcularIndiceN1(9, 0, concMedidaMonoxCarb))
        print("Monóxico de carbono está classificada como N1 - Boa!")
    elif 9 < concMedidaMonoxCarb <= 11:
        listaIndices.append(calcularIndiceN2(11, 9, concMedidaMonoxCarb))
        print("Monóxico de carbono está classificada como N2 - Moderada!")
    elif 11 < concMedidaMonoxCarb <= 13:
        listaIndices.append(calcularIndiceN3(13, 11, concMedidaMonoxCarb))
        print("Monóxico de carbono está classificada como N3 - Ruim!")
    elif 13 < concMedidaMonoxCarb <= 15:
        listaIndices.append(calcularIndiceN4(15, 13, concMedidaMonoxCarb))
        print("Monóxico de carbonoônio está classificada como N4 - Muito Ruim!")
    elif concMedidaMonoxCarb > 15:
        listaIndices.append(calcularIndiceN5(16, concMedidaMonoxCarb))
        print("Monóxico de carbono está classificada como N5 - Péssimo!")

    concMedidaDioxNitr = todosValores[tuplas][4]

    if 0 < concMedidaDioxNitr <= 200:
        listaIndices.append(calcularIndiceN1(200, 0, concMedidaDioxNitr))
        print("Dióxido de nitrogênio está classificada como N1 - Boa!")
    elif 200 < concMedidaDioxNitr <= 240:
        listaIndices.append(calcularIndiceN2(240, 200, concMedidaDioxNitr))
        print("Dióxido de nitrogênio está classificada como N2 - Moderada!")
    elif 240 < concMedidaDioxNitr <= 320:
        listaIndices.append(calcularIndiceN3(320, 240, concMedidaDioxNitr))
        print("Dióxido de nitrogênio está classificada como N3 - Ruim!")
    elif 320 < concMedidaDioxNitr <= 1130:
        listaIndices.append(calcularIndiceN4(1130, 320, concMedidaDioxNitr))
        print("Dióxido de nitrogênio está classificada como N4 - Muito Ruim!")
    elif concMedidaDioxNitr > 1130:
        listaIndices.append(calcularIndiceN5(1131, concMedidaDioxNitr))
        print("Dióxido de nitrogênio está classificada como N5 - Péssimo!")

    concMedidaDioxEnx = todosValores[tuplas][5]    

    if 0 < concMedidaDioxEnx <= 20:
        listaIndices.append(calcularIndiceN1(20, 0, concMedidaDioxEnx))
        print("Dióxido de enxofre está classificada como N1 - Boa!")
    elif 20 < concMedidaDioxEnx <= 40:
        listaIndices.append(calcularIndiceN2(40, 20, concMedidaDioxEnx))
        print("Dióxido de enxofre está classificada como N2 - Modera!")
    elif 40 < concMedidaDioxEnx <= 365:
        listaIndices.append(calcularIndiceN3(365, 40, concMedidaDioxEnx))
        print("Dióxido de enxofre está classificada como N3 - Ruim!")
    elif 365 < concMedidaDioxEnx <= 800:
        listaIndices.append(calcularIndiceN4(800, 365, concMedidaDioxEnx))
        print("Dióxido de enxofre está classificada como N4 - Muito Ruim!")
    elif concMedidaDioxEnx > 800:
        listaIndices.append(calcularIndiceN5(801, concMedidaDioxEnx))
        print("Dióxido de enxofre está classificada como N5 - Péssimo!")

    valorMaximoLista = max(listaIndices)

    if 0 < valorMaximoLista <= 40:
        print("A qualidade do ar no geral se encontra em N1 - Boa! Assim, não apresenta danos a saúde!")
    elif 41 < valorMaximoLista <= 80:
        print("A qualidade do ar no geral se encontra em N2 - Moderada! Ou seja, pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada!")
    elif 81 < valorMaximoLista <= 120:
        print("A qualidade do ar no geral se encontra em N3 - Ruim! Ou seja, toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde!")
    elif 121 < valorMaximoLista <= 200:
        print("A qualidade do ar no geral se encontra em N4 - Muito Ruim! Ou seja, toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)!")
    elif valorMaximoLista > 200:
        print("A qualidade do ar no geral se encontra em N5 - Péssima! Ou seja, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis!")

    print("---------------------------")    

    listaIndices = []