# 🎮 Sistema de RPG Completo — Python POO

### 🌙 **Edição: Reino das Sombras Místicas**


---

# 📋 Índice

* Sobre o Projeto
* Universo Reimaginado
* Conceitos de POO Aplicados
* Estrutura do Código
* Classes de Personagens (todas femininas)
* Criaturas Místicas
* Sistema de Batalha
* Exemplos de Código
* Questões Implementadas
* Expansões Futuras
* Licença

---

# 🎯 Sobre o Projeto 

Este projeto é um **RPG completo em Python**, criado para demonstrar — de forma prática — todos os pilares da Programação Orientada a Objetos.

Nesta edição especial, o universo foi feito para um cenário de fantasia sombria com:

✔ Personagens femininas
✔ Criaturas arcanas e místicas
✔ Magias sombrias e estelares
✔ Protagonista: **Evellyn, Invocadora Estelar**

Pilares de POO aplicados:

* **Encapsulamento**
* **Herança**
* **Polimorfismo**
* **Abstração**
* **Composição**
* **Métodos Estáticos**
* **Factory Methods**
* **Type Checking**
* **Property Decorators**

---

# 🌙 Universo Reimaginado

O mundo agora é **Lunaris**, um continente envolto por névoas mágicas e ruínas ancestrais. Após o Despertar Sombrio, criaturas místicas surgiram, corrompidas por energia abissal.

Evellyn, a última Invocadora Estelar, lidera um grupo de heroínas em busca do equilíbrio.


---

# 🧩 Conceitos de POO Aplicados

## 1️⃣ Classes e Objetos

```python
class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

cajado = Arma("Cajado Lunar", 18)
```

## 2️⃣ Encapsulamento

```python
@property
def vida(self):
    return self._vida

@vida.setter
def vida(self, valor):
    if valor < 0:
        self._vida = 0
    elif valor > self.vida_maxima:
        self._vida = self.vida_maxima
    else:
        self._vida = valor
```

## 3️⃣ Herança

Classes adaptadas:

* **PersonagemBase (classe mãe)**
* **Invocadora (classe da Evellyn)**
* **Feiticeira das Sombras**
* **Arqueira Fantasma**

## 4️⃣ Abstração

```python
from abc import ABC, abstractmethod

class Habilidade(ABC):
    @abstractmethod
    def usar(self, usuario, alvo):
        pass
```

## 5️⃣ Métodos Estáticos

```python
class Dado:
    @staticmethod
    def rolar(lados=6):
        return random.randint(1, lados)
```

---

# 🏗️ Estrutura do Código

📦 Sistema RPG
├── 🎲 Itens
│   ├── Arma
│   └── Poção
│
├── 🎒 Inventário
│   ├── adicionar_item()
│   ├── usar_pocao()
│   └── mostrar_itens()
│
├── 👤 Personagens Femininas
│   ├── PersonagemBase
│   ├── **Invocadora (Evellyn)**
│   ├── **Feiticeira das Sombras**
│   └── **Arqueira Fantasma**
│
├── 🐉 Criaturas Místicas
│   ├── Criatura
│   ├── Gárgula de Sangue
│   ├── Drakanith Cristalino
│   └── Eremita do Abismo (crítico)
│
├── ⚔️ Habilidades
│   ├── Luz Estelar
│   ├── Lâmina Sombria
│   └── Flecha Etérea
│
└── ⚔️ Sistema de Batalha
   └── Batalha

---

# 🦸 Classes de Personagens 

## Comparação Geral

| Classe                    | Atributo Principal | Dado | Variação  | Habilidade Especial   |
| ------------------------- | ------------------ | ---- | --------- | --------------------- |
| 🌟 Invocadora (Evellyn)   | Vigor Arcano       | d8   | Alta      | Luz Estelar (1.7×)    |
| 🌑 Feiticeira das Sombras | Poder Umbral       | d10  | Altíssima | Lâmina Sombria (1.9×) |
| 🏹 Arqueira Fantasma      | Precisão Etérea    | d6   | Baixa     | Flecha Etérea (1.4×)  |

---

# ✨ Personagens em Código

## 🌟 Evellyn — Invocadora Estelar

```python
evellyn = Invocadora("Evellyn", 110, 38)
evellyn.arma = Arma("Cajado Estelar", 16)
evellyn.adicionar_habilidade(LuzEstelar())
```

## 🌑 Lysandra — Feiticeira das Sombras

```python
lysandra = FeiticeiraSombras("Lysandra", 95, 45)
lysandra.adicionar_habilidade(LaminaSombria())
```

## 🏹 Mirella — Arqueira Fantasma

```python
mirella = ArqueiraFantasma("Mirella", 105, 33)
mirella.adicionar_habilidade(FlechaEterea())
```

---

# 🐉 Criaturas Místicas

## Gárgula de Sangue

Vida: 85
Dano: 18

## Drakanith Cristalino

Vida: 60
Dano: 14

## Eremita do Abismo

Vida: 120
Dano: 25
Critico: 35%
Dano crítico: x2

---

# ⚔️ Sistema de Batalha


## Exemplo 1v1

```python
evellyn = Invocadora("Evellyn", 110, 38)
gargula = Criatura.gargula_padrao()

batalha = Batalha(evellyn, gargula)
batalha.iniciar()
```

## Exemplo 3v3

```python
heroinas = [evellyn, lysandra, mirella]

monstros = [
    Criatura.drakanith(),
    Criatura.gargula_padrao(),
    EremitaAbismo()
]

batalha = Batalha(heroinas, monstros)
batalha.iniciar()
```

---

# 🎮 Saída Esperada

⚔️ **BATALHA INICIADA EM LUNARIS!** ⚔️

🔵 **HEROINAS**
• Evellyn (110)
• Lysandra (95)
• Mirella (105)

🔴 **CRIATURAS**
• Gárgula de Sangue (85)
• Drakanith (60)
• Eremita do Abismo (120)

💥 *Eremita do Abismo executa um GOLPE SOMBRIO CRÍTICO!*
Evellyn recebe 52 de dano!

✨ **VITÓRIA DAS HEROINAS!** ✨

---

# 📝 Exemplos de Código

## Inventário

```python
evellyn.inventario.adicionar_item(Pocao("Poção Lunar", 40))
```

## Habilidade Especial

```python
evellyn.usar_habilidade(0, gargula)
```

---

# 📊 Questões Implementadas

| Nível            | Questões | Pontos | Status     |
| ---------------- | -------- | ------ | ---------- |
| 🟢 Básico        | Q1–Q10   | 100    | ✅ Completo |
| 🟡 Intermediário | Q11–Q20  | 150    | ✅ Completo |
| 🔴 Avançado      | Q21–Q30  | 200    | ✅ Completo |

Total: **450 pontos — 100% concluído**

---

# 🚀 Expansões Futuras

* Afinidade elemental
* Invocações estelares para Evellyn
* Sistema de crafting místico
* Interface gráfica
* Experiência e níveis
* Grandes chefes (Titãs Lunares)

---

# 📄 Licença

Projeto livre para uso educacional.



