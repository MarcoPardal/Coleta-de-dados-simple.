def coletar_dados():  
    print("Coletando dados pessoais...")  
    
    nome_completo = input("Digite seu nome completo:")
    estado = input("Digite o estado que você mora:")  
    endereco = input("Digite seu endereço:")  
    telefone = input("Digite seu telefone:")  
    idade = input("Digite sua idade:")  
    cpf = input("Digite seu CPF (apenas números):")
    

    
    dados = {  
        'Nome Completo': nome_completo,
        'Estado de residência':estado,
        'Endereço': endereco,  
        'Telefone': telefone,  
        'Idade': idade,  
        'CPF': cpf  
        
    }  
    
    return dados  

def exibir_dados(dados):  
    print("\nDados coletados:")  
    for chave, valor in dados.items():  
        print(f"{chave}: {valor}")  

def main():  
    dados_pessoais = coletar_dados()  
    exibir_dados(dados_pessoais)  

if __name__ == "__main__":  
    main()
