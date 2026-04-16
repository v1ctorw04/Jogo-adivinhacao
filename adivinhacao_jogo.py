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

# CLASSE RANKING (Nova)
# Responsável por gerenciar as pontuações
class Ranking:
    def __init__(self):
        self.__jogadores = []

    def adicionar_pontuacao(self, nome, pontos):
        self.__jogadores.append({"nome": nome, "pontos": pontos})
        # Ordena do maior para o menor ponto
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
        self.__nome_jogador = ""
        self.__pontuacao_maxima = 100

    def selecionar_dificuldade(self):
        print("\nEscolha o nível de dificuldade:")
        print("1 - Fácil (13 tentativas)")
        print("2 - Médio (9 tentativas)")
        print("3 - Difícil (5 tentativas)")

        opcao = input("Opção: ")
        if opcao == '1':
            self.__limite = 13
        elif opcao == '3':
            self.__limite = 5
        else:
            self.__limite = 9 # Padrão Médio

    def iniciar(self):
        print("\n🎮 JOGO DA ADIVINHAÇÃO")
        self.__nome_jogador = input("Digite seu nome: ")
        self.selecionar_dificuldade()
        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas_usadas = 0
        print(f"\nBoa sorte, {self.__nome_jogador}!")
        print(f"Tente adivinhar o número entre 1 e 100 em {self.__limite} tentativas.")

    def calcular_pontuacao(self):
        # A pontuação é baseada nas tentativas restantes
        # Se acertar de primeira, ganha 100. Se gastar todas, ganha pouco.
        pontos = self.__pontuacao_maxima - (self.__tentativas_usadas * (100 // self.__limite))
        return max(pontos, 10) # Garante o mínimo de 10 pontos se vencer

    def jogar(self):
        venceu = False
        while self.__tentativas_usadas < self.__limite:
            try:
                palpite = int(input(f"\nTentativa {self.__tentativas_usadas + 1}/{self.__limite} - Digite seu palpite: "))
                self.__tentativas_usadas += 1

                if palpite == self.__numero_secreto:
                    pontos = self.calcular_pontuacao()
                    print(f"🎉 Parabéns, {self.__nome_jogador}! Você acertou em {self.__tentativas_usadas} tentativas.")
                    print(f"Sua pontuação: {pontos} pontos.")
                    return self.__nome_jogador, pontos

                elif palpite < self.__numero_secreto:
                    print("⬆️ O número secreto é MAIOR")
                else:
                    print("⬇️ O número secreto é MENOR")
            except ValueError:
                print("⚠️ Por favor, digite apenas números inteiros.")

        print(f"\n❌ Fim de jogo! O número era: {self.__numero_secreto}")
        return self.__nome_jogador, 0

# POLIMORFISMO
def executar_ciclo_jogo(jogo: Jogo, ranking: Ranking):
    nome, pontos = jogo.iniciar(), 0 # Inicialização genérica
    nome, pontos = jogo.jogar()

    if pontos > 0:
        ranking.adicionar_pontuacao(nome, pontos)

    ranking.exibir()

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    ranking_global = Ranking()

    while True:
        partida = JogoAdivinhacao()
        executar_ciclo_jogo(partida, ranking_global)

        continuar = input("Deseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar!")
            break
