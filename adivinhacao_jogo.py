import random
from abc import ABC, abstractmethod

# ABSTRAÇÃO
class Jogo(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass

# CLASSE RANKING
class Ranking:
    def __init__(self):
        self.__jogadores = []

    def adicionar_pontuacao(self, nome, pontos):
        self.__jogadores.append({"nome": nome, "pontos": pontos})
        self.__jogadores.sort(key=lambda x: x["pontos"], reverse=True)

    def exibir(self):
        print("\n🏆 --- RANKING ATUAL --- 🏆")
        if not self.__jogadores:
            print("Nenhum registro ainda.")
        for i, jogador in enumerate(self.__jogadores, 1):
            print(f"{i}º. {jogador['nome']} - {jogador['pontos']} pts")
        print("--------------------------\n")

# HERANÇA E ENCAPSULAMENTO
class JogoAdivinhacao(Jogo):
    def __init__(self):
        self.__numero_secreto = 0
        self.__tentativas_usadas = 0
        self.__limite = 0
        self.__multiplicador = 1
        self.__nome_jogador = ""
        self.__pontuacao_base = 100
        self.__cheat_code = 77

    def selecionar_dificuldade(self):
        print("\nEscolha o nível de dificuldade:")
        print("1 - Fácil (10 tentativas)")
        print("2 - Médio (5 tentativas)")
        print("3 - Difícil (3 tentativas)")
        print("4 - Mega-Sena (1 tentativa) (considere apostar na Mega-Sena se acertar)")

        opcao = input("Opção: ")
        if opcao == '1':
            self.__limite = 10
            self.__multiplicador = 1
        elif opcao == '2':
            self.__limite = 5
            self.__multiplicador = 2
        elif opcao == '3':
            self.__limite = 3
            self.__multiplicador = 5
        elif opcao == '4':
            self.__limite = 1
            self.__multiplicador = 10
        else:
            print("Opção inválida! Padrão: Médio.")
            self.__limite = 5
            self.__multiplicador = 2

    def iniciar(self):
        print("\n🎮 JOGO DA ADIVINHAÇÃO")
        self.__nome_jogador = input("Digite seu nome: ")
        self.selecionar_dificuldade()
        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas_usadas = 0
        print(f"\nBoa sorte, {self.__nome_jogador}!")
        print(f"Número entre 1 e 100. Você tem {self.__limite} tentativa(s).")

    def calcular_pontuacao(self):
        # Perde 10 pontos da base por cada tentativa errada
        pontos_finais = (self.__pontuacao_base - (self.__tentativas_usadas - 1) * 10)
        # Aplica o multiplicador da dificuldade
        return max(pontos_finais * self.__multiplicador, 10)

    def jogar(self):
        while self.__tentativas_usadas < self.__limite:
            try:
                entrada = input(f"\nTentativa {self.__tentativas_usadas + 1}/{self.__limite}: ")
                palpite = int(entrada)
                self.__tentativas_usadas += 1

                if palpite == self.__cheat_code or palpite == self.__numero_secreto:
                    if palpite == self.__cheat_code:
                        self.__numero_secreto = self.__cheat_code
                        
                    pontos = self.calcular_pontuacao()
                    print(f"🎉 ACERTOU! {self.__nome_jogador}, você fez {pontos} pontos.")
                    return self.__nome_jogador, pontos

                elif palpite < self.__numero_secreto:
                    print("⬆️ MAIOR")
                else:
                    print("⬇️ MENOR")
            except ValueError:
                print("⚠️ Apenas números inteiros!")

        print(f"\n❌ Fim de jogo! O número era: {self.__numero_secreto}")
        return self.__nome_jogador, 0

# POLIMORFISMO
def executar_ciclo_jogo(jogo: Jogo, ranking: Ranking):
    jogo.iniciar()
    nome, pontos = jogo.jogar()
    if pontos > 0:
        ranking.adicionar_pontuacao(nome, pontos)
    ranking.exibir()

if __name__ == "__main__":
    ranking_global = Ranking()
    while True:
        partida = JogoAdivinhacao()
        executar_ciclo_jogo(partida, ranking_global)
        if input("Jogar novamente? (s/n): ").lower() != 's':
            break
