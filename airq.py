print("PROGRAMA PARA A LEITURA DOS PARÂMETROS E CLASSIFICAÇÃO DA QUALIDADE DO AR!!")

fimDaPerg1 = False
fimDaPerg2 = False
fimDaPerg3 = False
fimDaPerg4 = False
fimDaPerg5 = False
fimDaPerg6 = False

fimDoProg = False
while not fimDoProg:
    while not fimDaPerg1:
            try:
                part_inal = float(input("Digite o valor desejado para partículas inaláveis (MP10): "))
            except:
                print("Digite apenas números!")
            else:
                if part_inal < 0 or part_inal == "":
                    print("Digite apenas números positivos!")
                    fimDaPerg1 = False
                elif part_inal >= 10000:
                    print("Digite apenas números de até 4 caracteres!")
                    fimDaPerg1 = False
                else:
                     fimDaPerg1 = True
                     while not fimDaPerg2:
                        try:
                            part_inal_finas = float(input("Digite o valor desejado para partículas inaláveis finas (MP2,5): "))
                        except:
                            print("Digite apenas números!")
                        else:
                            if part_inal_finas < 0 or part_inal == "":
                                print("Digite apenas números positivos!")
                                fimDaPerg2 = False
                            elif part_inal_finas >= 10000:
                                print("Digite apenas números de até 4 caracteres!")   
                                fimDaPerg2 = False
                            else:
                                fimDaPerg2 = True                     
                                while not fimDaPerg3:
                                    try:
                                        ozonio = float(input("Digite o valor desejado para ozônio (O3): "))
                                    except:
                                        print("Digite apenas números!")
                                    else:
                                        if ozonio < 0 or part_inal == "":
                                            print("Digite apenas números positivos!")
                                            fimDaPerg3 = False
                                        elif ozonio >= 10000:
                                            print("Digite apenas números de até 4 caracteres!") 
                                            fimDaPerg3 = False  
                                        else:
                                            fimDaPerg3 = True
                                            while not fimDaPerg4:   
                                                try:
                                                    monox_carb = float(input("Digite o valor desejado para monóxido de carbono (CO): "))
                                                except:
                                                    print("Digite apenas números!")
                                                else:
                                                    if monox_carb < 0 or part_inal == "":
                                                        print("Digite apenas números positivos!")
                                                        fimDaPerg4 = False
                                                    elif monox_carb >= 10000:
                                                        print("Digite apenas números de até 4 caracteres!")  
                                                        fimDaPerg4 = False    
                                                    else:
                                                        fimDaPerg4 = True
                                                        while not fimDaPerg5:
                                                            try:
                                                                diox_nitro = float(input("Digite o valor desejado para dióxido de nitrogênio (NO2): "))
                                                            except:
                                                                print("Digite apenas números!")
                                                            else:
                                                                if diox_nitro < 0 or part_inal == "":
                                                                    print("Digite apenas números positivos!")  
                                                                    fimDaPerg5 = False
                                                                elif diox_nitro >= 10000:
                                                                    print("Digite apenas números de até 4 caracteres!") 
                                                                    fimDaPerg5 = False
                                                                else:
                                                                    fimDaPerg5 = True
                                                                    while not fimDaPerg6:        
                                                                        try:
                                                                            diox_enxofre = float(input("Digite o valor desejado para dióxido de enxofre (SO2): "))
                                                                        except:
                                                                            print("Digite apenas números!")
                                                                        else:
                                                                            if diox_enxofre < 0 or part_inal == "":
                                                                                print("Digite apenas números positivos!")
                                                                                fimDaPerg6 = False
                                                                            elif diox_enxofre >= 10000:
                                                                                print("Digite apenas números de até 4 caracteres!")   
                                                                                fimDaPerg6 = False
                                                                            else:
                                                                                fimDaPerg6 = True   
                                                                                                   
    if part_inal <= 50:
            indicef = 0 + ((40 - 0)/(50 - 0)) * (part_inal - 0)
            print("A classificação das partículas inaláveis é N1 - Boa! Apresentando nenhum problema à saúde das pessoas.")
    elif 50 < part_inal <= 100:
            indicef = 41 + ((80 - 41)/(100 - 50)) * (part_inal - 50)
            print("A classificação das partículas inaláveis é N2 - Moderada! Fazendo com que pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif 100 < part_inal <= 150:
            indicef = 81 + ((120 - 81)/(150 - 100)) * (part_inal - 100)
            print("A classificação das partículas inaláveis é N3 - Ruim! Ou seja, toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif 150 < part_inal <= 250:
            indicef = 121 + ((200 - 121)/(250 - 150)) * (part_inal - 150)
            print("A classificação das partículas inaláveis é N4 - Muito ruim! Ou seja, toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    elif part_inal > 250:
            print("A classificação das partículas inaláveis é N5 - Péssima! Ou seja, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")

    if part_inal_finas <= 25:
            indicef = 0 + ((40 - 0)/(25 - 0)) * (part_inal_finas - 0)
            print("A classificação das partículas inaláveis finas é N1 - Boa! Apresentando nenhum problema à saúde das pessoas.")
    elif 25 < part_inal_finas <= 50:
            indicef = 41 + ((80 - 41)/(50 - 25)) * (part_inal_finas - 25)
            print("A classificação das partículas inaláveis finas é N2 - Moderada! Fazendo com que pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif 50 < part_inal_finas <= 75:
        indicef = 81 + ((120 - 81)/(75 - 50)) * (part_inal_finas - 50)
        print("A classificação das partículas inaláveis finas é N3 - Ruim! Ou seja, toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif 75 < part_inal_finas <= 125:
        indicef = 121 + ((200 - 121)/(125 - 75)) * (part_inal_finas - 75)
        print("A classificação das partículas inaláveis finas é N4 - Muito ruim! Ou seja, toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    elif part_inal_finas > 125:
        print("A classificação das partículas inaláveis finas é N5 - Péssima! Ou seja, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")

    if ozonio <= 100:
        indicef = 0 + ((40 - 0)/(100 - 0)) * (ozonio - 0)
        print("A classificação do ozônio é N1 - Boa! Apresentando nenhum problema à saúde das pessoas.")
    elif 100 < ozonio <= 130:
        indicef = 41 + ((80 - 41)/(130 - 100)) * (ozonio - 100)
        print("A classificação do ozônio é N2 - Moderada! Fazendo com que pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif 130 < ozonio <= 160:
        indicef = 81 + ((120 - 81)/(160 - 130)) * (ozonio - 130)
        print("A classificação do ozônio é N3 - Ruim! Ou seja, toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif 160 < ozonio <= 200:
        indicef = 121 + ((200 - 121)/(200 - 160)) * (ozonio - 160)
        print("A classificação do ozônio é N4 - Muito ruim! Ou seja, toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    elif ozonio > 200:
        print("A classificação do ozônio é N5 - Péssima! Ou seja, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")

    if monox_carb <= 9:
        indicef = 0 + ((40 - 0)/(9 - 0)) * (monox_carb - 0)
        print("A classificação do monóxido de carbono é N1 - Boa! Apresentando nenhum problema à saúde das pessoas.")
    elif 9 < monox_carb <= 11:
        indicef = 41 + ((80 - 41)/(11 - 9)) * (monox_carb - 9)
        print("A classificação do monóxido de carbono é N2 - Moderada! Fazendo com que pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif 11 < monox_carb <= 13:
        indicef = 81 + ((120 - 81)/(11 - 13)) * (monox_carb - 13)
        print("A classificação do monóxido de carbono é N3 - Ruim! Ou seja, toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif 13 < monox_carb <= 15:
        indicef = 121 + ((200 - 121)/(15 - 13)) * (monox_carb - 13)
        print("A classificação do monóxido de carbono é N4 - Muito ruim! Ou seja, toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    elif monox_carb > 15:
        print("A classificação do monóxido de carbono é N5 - Péssima! Ou seja, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")

    if diox_nitro <= 200:
        indicef = 0 + ((40 - 0)/(200 - 0)) * (diox_nitro - 0)
        print("A classificação do dióxido de nitrogênio é N1 - Boa! Apresentando nenhum problema à saúde das pessoas.")
    elif 200 < diox_nitro <= 240:
        indicef = 41 + ((80 - 41)/(240 - 200)) * (diox_nitro - 200)
        print("A classificação do dióxido de nitrogênio é N2 - Moderada! Fazendo com que pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif 240 < diox_nitro <= 320:
        indicef = 81 + ((120 - 81)/(320 - 240)) * (diox_nitro - 240)
        print("A classificação do dióxido de nitrogênio é N3 - Ruim! Ou seja, toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif 320 < diox_nitro <= 1130:
        indicef = 121 + ((200 - 121)/(1130 - 320)) * (diox_nitro - 320)
        print("A classificação do dióxido de nitrogênio é N4 - Muito ruim! Ou seja, toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    elif diox_nitro > 1130:
        print("A classificação do dióxido de nitrogênio é N5 - Péssima! Ou seja, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")

    if diox_enxofre <= 20:
        indicef = 0 + ((40 - 0)/(20 - 0)) * (diox_enxofre - 0)
        print("A classificação do dióxido de enxofre é N1 - Boa! Apresentando nenhum problema à saúde das pessoas.")
    elif 20 < diox_enxofre <= 40:
        indicef = 41 + ((80 - 41)/(40 - 20)) * (diox_enxofre - 20)
        print("A classificação do dióxido de enxofre é N2 - Moderada! Fazendo com que pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.")
    elif 40 < diox_enxofre <= 365:
        indicef = 81 + ((120 - 81)/(365 - 40)) * (diox_enxofre - 40)
        print("A classificação do dióxido de enxofre é N3 - Ruim! Ou seja, toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.")
    elif 365 < diox_enxofre <= 800:
        indicef = 121 + ((200 - 121)/(800 - 365)) * (diox_enxofre - 365)
        print("A classificação do dióxido de enxofre é N4 - Muito ruim! Ou seja, toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).")
    elif diox_enxofre > 800:
        print("A classificação do dióxido de enxofre é N5 - Péssima! Ou seja, toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.")

    fimDaPergFinalizacao = False
    while not fimDaPergFinalizacao:
        resposta_cont = input("Deseja realizar outra verificação? (Responda apenas com sim ou não): ")
        if resposta_cont.upper() in ["SIM","S"]:
            fimDoProg = False
            fimDaPergFinalizacao = True
            fimDaPerg1 = False
            fimDaPerg2 = False
            fimDaPerg3 = False
            fimDaPerg4 = False
            fimDaPerg5 = False
            fimDaPerg6 = False
        elif resposta_cont.upper() in ["NAO","NÃO","N"]:
            fimDoProg = True
            fimDaPergFinalizacao = True
        else:
            print("Digite respostas válidas!")
            fimDoProg = False
            fimDaPergFinalizacao = False

print("OBRIGADO POR UTILIZAR ESTE PROGRAMA!") 
