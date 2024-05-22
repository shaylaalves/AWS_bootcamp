# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um cenário e retornar a estratégia indicada.
def escolher_estrategia(cenario):
    if "aplicativo a ser descomissionado" in cenario or "sem valor comercial" in cenario:
        return "retire"
        
    # TODO: Preencha corretamente a estratégia indicada para cada cenário, considerando as condições abaixo e Saídas possíveis:

    elif "manter aplicativos no ambiente de origem" in cenario or "adiar sua migracao para a nuvem" in cenario:
        return "retain"
        
    elif "mover aplicativos para a nuvem sem modifica-los" in cenario or "lift and shift" in cenario:
        return "rehost"
        
    elif "transferir servidores ou instancias para outra plataforma na nuvem" in cenario:
        return "replatform"
        
    elif "substituir o aplicativo por uma versao ou produto diferente" in cenario:
        return "repurchase"
        
    elif "mover o aplicativo para a nuvem" in cenario or "introduzir otimizacoes para opera-lo de forma eficiente" in cenario:
        return "rehost"
        
    elif "modificar a arquitetura do aplicativo" in cenario or "aproveitar os recursos nativos para melhorar agilidade" in cenario:
        return "refactor or re-architect"
        
# Imprime a estratégia indicada para o cenário recebido na "entrada" através da função "escolher_estrategia".
print(escolher_estrategia(entrada))
