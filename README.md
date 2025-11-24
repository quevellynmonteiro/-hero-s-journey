🎮 Sistema de RPG Completo — Python POO
🌙 Edição: Reino das Sombras Místicas

Com personagens femininas, monstros místicos e protagonista Evellyn

📋 Índice

Sobre o Projeto

Universo Reimaginado

Conceitos de POO Aplicados

Estrutura do Código

Classes de Personagens (todas femininas)

Criaturas Místicas

Sistema de Batalha

Exemplos Adaptados

Questões Implementadas

Expansões Futuras

🎯 Sobre o Projeto (Versão Mística)

Este RPG foi refeito para um cenário de fantasia sombria com criaturas místicas, mantendo toda a estrutura POO já apresentada, porém com:

✔ Personagens femininas
✔ Mundo de magia arcana
✔ Monstros sobrenaturais
✔ Protagonista: Evellyn, Invocadora Estelar

Todos os pilares da POO continuam:

Encapsulamento

Herança

Polimorfismo

Abstração

Composição

🌙 Universo Reimaginado

O jogo agora se passa no continente de Lunaris, onde criaturas arcanas vagam entre florestas vivas e ruínas ancestrais. Toda a magia do mundo está instável, e Evellyn é uma das Guardiãs Estelares treinadas para restaurar o equilíbrio.

As classes masculinas clássicas foram substituídas por novas versões femininas místicas, mantendo mecânicas idênticas.

🧩 Conceitos de POO Aplicados

(Mesmo código e pedagogia, adaptados ao novo universo)

1️⃣ Classes e Objetos
class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

cajado = Arma("Cajado Lunar", 18)

2️⃣ Encapsulamento

(sem alterações)

3️⃣ Herança

(agora com classes femininas místicas)

Classes novas:

Invocadora (Evellyn)

Feiticeira das Sombras

Arqueira Fantasma

4️⃣ Abstração

(sem alterações)

5️⃣ Métodos Estáticos

(sem alterações)

🏗️ Estrutura do Código

(Igual ao original, mas renomeado)

📦 Sistema RPG
├── 🎲 Itens
│ ├── Arma
│ └── Poção
│
├── 🎒 Inventário
│
├── 👤 Personagens Femininas
│ ├── PersonagemBase
│ ├── Invocadora (classe de Evellyn)
│ ├── Feiticeira das Sombras
│ └── Arqueira Fantasma
│
├── 🐉 Criaturas Místicas
│ ├── Criatura
│ └── Gárgula de Sangue
│
├── ⚔️ Habilidades
│ ├── Luz Estelar (Evellyn)
│ ├── Lâmina Sombria
│ └── Flecha Etérea
│
└── ⚔️ Sistema de Batalha

🦸 Classes de Personagens — Versão Mística
Comparação
Classe	Atributo Principal	Dado	Estilo	Habilidade
🌟 Invocadora (Evellyn)	Vigor Arcano	d8	Alta variação	Luz Estelar (1.7x)
🌑 Feiticeira das Sombras	Poder Umbral	d10	Caos mágico	Lâmina Sombria (1.9x)
🏹 Arqueira Fantasma	Precisão Etérea	d6	Consistente	Flecha Etérea (1.4x)
✨ Personagens Femininas (Exemplos)
🌟 Evellyn — Invocadora Estelar
evellyn = Invocadora("Evellyn", 110, 38)
evellyn.arma = Arma("Cajado Estelar", 16)
evellyn.adicionar_habilidade(LuzEstelar())

🌑 Lysandra — Feiticeira das Sombras
lysandra = FeiticeiraSombras("Lysandra", 95, 45)
lysandra.adicionar_habilidade(LaminaSombria())

🏹 Mirella — Arqueira Fantasma
mirella = ArqueiraFantasma("Mirella", 105, 33)
mirella.adicionar_habilidade(FlechaEterea())

🐉 Criaturas Místicas
Gárgula de Sangue

Vida: 85
Dano: 18
Obs.: Pedra viva com ataques perfurantes

Drakanith Cristalino

Vida: 60
Dano: 14
Obs.: Sopra rajadas congelantes

Eremita do Abismo

Vida: 120
Dano: 25
Critico: 35%
Dano Crítico: x2

(Substitui Orc padrão)

⚔️ Sistema de Batalha

Mantém todas as mecânicas, apenas com nomes mágicos

Exemplo 1v1
evellyn = Invocadora("Evellyn", 110, 38)
gargula = Criatura.gargula_padrao()

batalha = Batalha(evellyn, gargula)
batalha.iniciar()

Exemplo 3v3
heroinas = [evellyn, lysandra, mirella]
monstros = [
    Criatura.drakanith(),
    Criatura.gargula_padrao(),
    EremitaAbismo()
]

batalha = Batalha(heroinas, monstros)
batalha.iniciar()

🎮 Saída Adaptada (Exemplo)

⚔️ BATALHA INICIADA EM LUNARIS! ⚔️

🔵 HEROINAS

Evellyn (Vida: 110)

Lysandra (Vida: 95)

Mirella (Vida: 105)

🔴 CRIATURAS

Gárgula de Sangue (Vida: 85)

Drakanith Cristalino (Vida: 60)

Eremita do Abismo (Vida: 120)

…

💥 Eremita do Abismo desfere um GOLPE SOMBRIO CRÍTICO!
Evellyn recebe 52 de dano!

…

✨ VITÓRIA DAS HEROINAS! ✨

📝 Exemplos Adaptados
Inventário

(Idêntico — só muda o flavor)

evellyn.inventario.adicionar_item(Pocao("Poção Lunar", 40))

Habilidade Especial
evellyn.usar_habilidade(0, gargula)
# “Evellyn libera a Luz Estelar!”

🚀 Expansões Finais (Sugeridas)

Sistema de afinidade elemental (luz, sombra, gelo, abismo)

Invocações astralizadas para Evellyn

Armas épicas (Lâmina da Lua Nova, Arco Etéreo, Cajado do Eclipse)

Grandes criaturas (Titãs Lunares, Serpentes de Éter)
