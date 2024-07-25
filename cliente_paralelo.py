import Pyro4
import threading

def add_candidate(servidor_votacao, nome_candidato):
    resultado = servidor_votacao.adicionar_candidato(nome_candidato)
    print(f"Thread {threading.current_thread().name}: {resultado}")

def vote(servidor_votacao, nome_candidato):
    resultado = servidor_votacao.votar(nome_candidato)
    print(f"Thread {threading.current_thread().name}: {resultado}")

def view_results(servidor_votacao):
    resultados = servidor_votacao.obter_resultados()
    print(f"Thread {threading.current_thread().name}: Resultados da Votação:")
    for candidato, votos in resultados.items():
        print(f"{candidato}: {votos} votos")

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
            # Cria uma nova thread para adicionar o candidato
            thread = threading.Thread(target=add_candidate, args=(servidor_votacao, nome_candidato))
            thread.start()

        elif escolha == 2:
            resultados = servidor_votacao.obter_resultados()
            print("Candidatos:")
            for candidato in resultados.keys():
                print(f"{candidato}")
            nome_candidato = input("Digite o nome do candidato que deseja votar: ")
            # Cria uma nova thread para votar
            thread = threading.Thread(target=vote, args=(servidor_votacao, nome_candidato))
            thread.start()

        elif escolha == 3:
            # Cria uma nova thread para ver resultados
            thread = threading.Thread(target=view_results, args=(servidor_votacao,))
            thread.start()

        elif escolha == 4:
            break

if __name__ == "__main__":
    main()
