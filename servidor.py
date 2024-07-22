import Pyro4

@Pyro4.expose
class ServidorVotacao:
    def __init__(self):
        self.candidatos = {}
        self.votos = {}

    def adicionar_candidato(self, nome_candidato):
        if nome_candidato not in self.candidatos:
            self.candidatos[nome_candidato] = 0
            return f"Candidato {nome_candidato} adicionado com sucesso."
        else:
            return f"Candidato {nome_candidato} já existe."

    def votar(self, nome_candidato):
        if nome_candidato in self.candidatos:
            self.candidatos[nome_candidato] += 1
            return f"Voto para {nome_candidato} registrado com sucesso."
        else:
            return f"Candidato inválido: {nome_candidato}"

    def obter_resultados(self):
        return self.candidatos

def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(ServidorVotacao)

    # Localiza o Name Server e registra o objeto
    with Pyro4.locateNS() as ns:
        ns.register("servidor_votacao", uri)

    print("Servidor de votação está pronto.")
    daemon.requestLoop()  # O servidor processa as solicitações dos clientes

if __name__ == "__main__":
    main()
