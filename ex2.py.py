# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um pilar e retornar sua respectiva descrição.
def descrever_pilar(pilar):
    if pilar == "excelencia operacional":
        return "execucao e monitoramento de sistemas e melhoria continua"
        
    # TODO: Preencha corretamente a descrição de cada pilar, considerando as condições abaixo e Saídas possíveis:
    
    elif pilar == "seguranca":
        return "protecao de informacoes e sistemas"
        
    elif pilar == "confiabilidade":
        return "capacidade dos sistemas de executar as funcoes pretendidas"
        
    elif pilar == "eficiencia de performance":
        return "alocacao eficaz e otimizada de recursos de TI e computacao"
        
    elif pilar == "otimizacao de custos":
        return "obtencao do melhor retorno sobre o investimento em recursos"
        
    elif pilar == "sustentabilidade":
        return "reducao do impacto ambiental dos sistemas na nuvem"
 
# Imprime a descrição do pilar recebido na "entrada" através da função "descrever_pilar".
print(descrever_pilar(entrada))