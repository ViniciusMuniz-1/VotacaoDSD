import Pyro4

def main():
    uri_servidor_votacao = input('SERVIDOR: ')
        
    servidor_votacao = Pyro4.Proxy(uri_servidor_votacao)

    while True:
        print("\n1. Adicionar Candidato")
        print("2. Votar")
        print("3. Ver Resultados")
        print("4. Sair")
        escolha = int(input("Selecione uma opção: "))

        if escolha == 1:
            nome_candidato = input("Digite o nome do candidato: ")
            resultado = servidor_votacao.adicionar_candidato(nome_candidato)
            print(resultado)

        elif escolha == 2:
            resultados = servidor_votacao.obter_resultados()

            print("Candidatos:")
            for candidato, votos in resultados.items():
                print(f"{candidato}")
            nome_candidato = input("Digite o nome do candidato que deseja votar: ")

            resultado = servidor_votacao.votar(nome_candidato)
            print(resultado)

        elif escolha == 3:
            resultados = servidor_votacao.obter_resultados()
            print("Resultados da Votação:")
            for candidato, votos in resultados.items():
                print(f"{candidato}: {votos} votos")

        elif escolha == 4:
            break

if __name__ == "__main__":
    main()
