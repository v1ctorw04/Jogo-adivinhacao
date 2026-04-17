# 🎮 Jogo de Adivinhação em Python
Projeto desenvolvido em Python com foco na aplicação de **Programação Orientada a Objetos (POO)** e dos princípios **SOLID**, simulando um jogo interativo de adivinhação com sistema de pontuação e ranking.

---
## 📌 Sobre o projeto
O jogo consiste em adivinhar um número aleatório entre **1 e 100**, dentro de um número limitado de tentativas, que varia conforme a dificuldade escolhida.

O projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de desenvolvimento de software, incluindo organização de código, reutilização e boas práticas, como:
- Abstração
- Encapsulamento
- Herança
- Polimorfismo
- Princípios SOLID
---
## 🚀 Funcionalidades

* 🎯 Escolha de dificuldade (Fácil, Médio e Difícil ou se quiser testar a sorte de verdade, o modo Mega-Sena)
* 🔢 Número aleatório a cada partida
* 📊 Sistema de pontuação baseado no desempenho
* 🏆 Ranking global dos jogadores
* 🔁 Possibilidade de jogar múltiplas partidas
* ⚠️ Tratamento de erros (entrada inválida)
---

## 🧠 Conceitos aplicados
### 🔹 Abstração
Classe base `Jogo` define os métodos genéricos:
* `iniciar()`
* `jogar()`
---

### 🔹 Encapsulamento
Atributos privados protegem o estado interno do jogo:
```python
self.__numero_secreto
self.__tentativas_usadas
```
---

### 🔹 Herança
A classe `JogoAdivinhacao` herda da classe abstrata `Jogo`, reutilizando e especializando comportamentos.

---

### 🔹 Polimorfismo
Os métodos `iniciar()` e `jogar()` são implementados de forma específica na classe filha.

---

## 🧮 Sistema de Pontuação
A pontuação é calculada com base no número de tentativas utilizadas:

* Quanto menos tentativas → maior a pontuação
* Pontuação máxima: **100 pontos**
* Pontuação mínima ao vencer: **10 pontos**

Fórmula utilizada:
```python
pontos = 100 - (tentativas_usadas * (100 // limite))
```
---

## 🏆 Sistema de Ranking
* Armazena nome e pontuação dos jogadores
* Ordena automaticamente do maior para o menor
* Exibido ao final de cada partida

Exemplo:

```
🏆 --- RANKING ATUAL --- 🏆
1º. João - 90 pts
2º. Maria - 70 pts
--------------------------
```

---

## ▶️ Como executar

### Pré-requisitos

* Python 3.x instalado

### Execução

```bash
python adivinhacao_jogo.py ou diretamente no Google Colab: https://colab.research.google.com/drive/1qXBy7wYbZ5X5WSBkHHH7GbLT5EsjjNYI?usp=sharing
```
---

## 📁 Estrutura do projeto

```
README.md
adivinhacao_jogo.py
```
---

## 💡 Possíveis melhorias

* 💾 Salvar ranking em arquivo
* 🌐 Transformar em API ou jogo online
* 🔊 Adicionar efeitos sonoros
* 🧠 Implementar níveis com inteligência artificial
---

## 👨‍💻 Autor

Desenvolvido por v1ctorw04
---
