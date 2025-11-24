RPG: Reino das Sombras Místicas
Arquivo único: rpg_sombras_misticas.py
Versão didática que demonstra conceitos de POO em Python (Encapsulamento, Herança,
Polimorfismo, Abstração, Composição, Factory Methods, Métodos Estáticos).

Execute:
    python rpg_sombras_misticas.py


import random
from abc import ABC, abstractmethod
from typing import List, Optional



class Dado:
    @staticmethod
    def rolar(lados: int = 6) -> int:
        return random.randint(1, lados)

    @staticmethod
    def rolar_com_modificador(lados: int, modificador: int = 0) -> int:
        return Dado.rolar(lados) + modificador



class Arma:
    def __init__(self, nome: str, poder: int):
        self.nome = nome
        self.poder = poder

    def __repr__(self):
        return f"Arma(nome={self.nome}, poder={self.poder})"


class Pocao:
    def __init__(self, nome: str, cura: int):
        self.nome = nome
        self.cura = cura

    def __repr__(self):
        return f"Pocao(nome={self.nome}, cura={self.cura})"



class Inventario:
    def __init__(self):
        self.itens: List[object] = []

    def adicionar_item(self, item: object):
        self.itens.append(item)

    def mostrar_itens(self):
        if not self.itens:
            print("Inventário vazio.")
            return
        for i, it in enumerate(self.itens, 1):
            if isinstance(it, Pocao):
                print(f"{i}. Poção: {it.nome} (Cura: {it.cura})")
            elif isinstance(it, Arma):
                print(f"{i}. Arma: {it.nome} (+{it.poder})")
            else:
                print(f"{i}. {it}")

    def usar_pocao(self, personagem) -> bool:
        # Usa a primeira poção encontrada
        for it in self.itens:
            if isinstance(it, Pocao):
                cura = it.cura
                personagem.vida += cura
                self.itens.remove(it)
                print(f"{personagem.nome} usou {it.nome} e recuperou {cura} de vida!")
                return True
        print("Nenhuma poção disponível no inventário.")
        return False



class Habilidade(ABC):
    @abstractmethod
    def usar(self, usuario, alvo):
        pass


class LuzEstelar(Habilidade):
    def usar(self, usuario, alvo):
        # dano = poder do usuário + arma + dado d8 * multiplicador
        base = usuario.poder_base()
        arma = usuario.arma.poder if usuario.arma else 0
        rolagem = Dado.rolar(8)
        dano = int((base + arma + rolagem) * 1.7)
        alvo.vida -= dano
        print(f"{usuario.nome} convoca Luz Estelar! ({base}+{arma}+d8:{rolagem}) -> {dano} de dano em {alvo.nome}.")


class LaminaSombria(Habilidade):
    def usar(self, usuario, alvo):
        base = usuario.poder_base()
        arma = usuario.arma.poder if usuario.arma else 0
        rolagem = Dado.rolar(10)
        dano = int((base + arma + rolagem) * 1.9)
        alvo.vida -= dano
        print(f"{usuario.nome} desfere Lâmina Sombria! ({base}+{arma}+d10:{rolagem}) -> {dano} de dano em {alvo.nome}.")


class FlechaEterea(Habilidade):
    def usar(self, usuario, alvo):
        base = usuario.poder_base()
        arma = usuario.arma.poder if usuario.arma else 0
        rolagem = Dado.rolar(6)
        dano = int((base + arma + rolagem) * 1.4)
        alvo.vida -= dano
        print(f"{usuario.nome} atira Flecha Etérea! ({base}+{arma}+d6:{rolagem}) -> {dano} de dano em {alvo.nome}.")



class Personagem:
    def __init__(self, nome: str, vida_maxima: int, atributo_principal: int):
        self.nome = nome
        self._vida = vida_maxima
        self.vida_maxima = vida_maxima
        self.atributo = atributo_principal
        self.arma: Optional[Arma] = None
        self.inventario = Inventario()
        self.habilidades: List[Habilidade] = []
        self.status = {}  # ex: {'sangramento': {'turns':2,'dano':5}}

    # Encapsulamento de vida
    @property
    def vida(self) -> int:
        return self._vida

    @vida.setter
    def vida(self, valor: int):
        if valor < 0:
            self._vida = 0
        elif valor > self.vida_maxima:
            self._vida = self.vida_maxima
        else:
            self._vida = valor

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def adicionar_habilidade(self, habilidade: Habilidade):
        self.habilidades.append(habilidade)
        print(f"{self.nome} aprendeu {habilidade.__class__.__name__}!")

    def poder_base(self) -> int:
        """Valor base de ataque derivado do atributo principal.
        Sobrescrever em classes filhas se necessário."""
        return self.atributo

    def atacar(self, alvo):
        """Ataque padrão: atributo + arma + dado (d6)"""
        base = self.poder_base()
        arma = self.arma.poder if self.arma else 0
        rolagem = Dado.rolar(6)
        dano = base + arma + rolagem
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome}! ({base}+{arma}+d6:{rolagem}) -> {dano} de dano.")

    def usar_habilidade(self, indice: int, alvo):
        if indice < 0 or indice >= len(self.habilidades):
            print(f"Habilidade inválida para {self.nome}.")
            return
        habilidade = self.habilidades[indice]
        habilidade.usar(self, alvo)

    def aplicar_status_turno(self):
        # Aplica efeitos como sangramento
        if 'sangramento' in self.status:
            st = self.status['sangramento']
            dano = st['dano']
            self.vida -= dano
            st['turns'] -= 1
            print(f"{self.nome} sofre {dano} de sangramento! (turnos restantes: {st['turns']})")
            if st['turns'] <= 0:
                del self.status['sangramento']

    def aplicar_status_critico(self, nome_status: str, turns: int, dano: int):
        self.status[nome_status] = {'turns': turns, 'dano': dano}



class Invocadora(Personagem):
    # equivalente ao Mago/Invocadora: d8
    def poder_base(self) -> int:
        return self.atributo

    def atacar(self, alvo):
        base = self.poder_base()
        arma = self.arma.poder if self.arma else 0
        rolagem = Dado.rolar(8)
        dano = base + arma + rolagem
        alvo.vida -= dano
        print(f"{self.nome} ataca com magias & cajado! ({base}+{arma}+d8:{rolagem}) -> {dano} de dano.")


class FeiticeiraSombras(Personagem):
    # equivalente ao Guerreiro: d10 (mais robusta)
    def poder_base(self) -> int:
        return self.atributo

    def atacar(self, alvo):
        base = self.poder_base()
        arma = self.arma.poder if self.arma else 0
        rolagem = Dado.rolar(10)
        dano = base + arma + rolagem
        alvo.vida -= dano
        print(f"{self.nome} desferre ataque sombrio! ({base}+{arma}+d10:{rolagem}) -> {dano} de dano.")


class ArqueiraFantasma(Personagem):
    # equivalente ao Arqueiro: d6
    def poder_base(self) -> int:
        return self.atributo

    def atacar(self, alvo):
        base = self.poder_base()
        arma = self.arma.poder if self.arma else 0
        rolagem = Dado.rolar(6)
        dano = base + arma + rolagem
        alvo.vida -= dano
        print(f"{self.nome} dispara Flecha Etérea! ({base}+{arma}+d6:{rolagem}) -> {dano} de dano.")



class Criatura:
    def __init__(self, nome: str, vida: int, dano_base: int, chance_critico: int = 0):
        self.nome = nome
        self._vida = vida
        self.vida_maxima = vida
        self.dano_base = dano_base
        self.chance_critico = chance_critico
        self.status = {}

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, v):
        if v < 0:
            self._vida = 0
        elif v > self.vida_maxima:
            self._vida = self.vida_maxima
        else:
            self._vida = v

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def atacar(self, alvo: Personagem):
        # dano pode criticar
        rolagem = Dado.rolar(100)
        dano = self.dano_base + Dado.rolar(6)
        if self.chance_critico and rolagem <= self.chance_critico:
            dano *= 2
            # aplica sangramento em críticos
            if hasattr(alvo, 'aplicar_status_critico'):
                alvo.aplicar_status_critico('sangramento', turns=2, dano=max(1, int(alvo.vida_maxima*0.05)))
            print(f"💥 {self.nome} acerta CRÍTICO! ({rolagem}<= {self.chance_critico})")
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome}! -> {dano} de dano.")

    @classmethod
    def gargula_padrao(cls):
        return cls("Gárgula de Sangue", vida=85, dano_base=18, chance_critico=0)

    @classmethod
    def drakanith(cls):
        return cls("Drakanith Cristalino", vida=60, dano_base=14, chance_critico=0)

    @classmethod
    def eremita_abismo(cls):
        return cls("Eremita do Abismo", vida=120, dano_base=25, chance_critico=35)



class Batalha:
    def __init__(self, lado_a, lado_b):
        # lados podem ser um único personagem/monstro ou lista
        self.lado_a = lado_a if isinstance(lado_a, list) else [lado_a]
        self.lado_b = lado_b if isinstance(lado_b, list) else [lado_b]
        # padroniza objetos com metodo esta_vivo e atacar

    def exibir_combatentes(self):
        print("\n🔵 LADO A:")
        for p in self.lado_a:
            vida = getattr(p, 'vida', 'N/A')
            print(f"  - {p.nome} (Vida: {vida})")
        print("\n🔴 LADO B:")
        for p in self.lado_b:
            vida = getattr(p, 'vida', 'N/A')
            print(f"  - {p.nome} (Vida: {vida})")
        print()

    def vivos(self, lado):
        return [p for p in lado if getattr(p, 'esta_vivo')()]

    def escolher_alvo_aleatorio(self, inimigos):
        vivos = self.vivos(inimigos)
        return random.choice(vivos) if vivos else None

    def ordem_iniciativa(self, todos):
        # gera lista embaralhada com iniciativa básica (d20)
        iniciativas = [(Dado.rolar(20), p) for p in todos]
        iniciativas.sort(key=lambda x: x[0], reverse=True)
        return [p for ini, p in iniciativas]

    def iniciar(self):
        print("⚔️  BATALHA INICIADA EM LUNARIS! ⚔️\n")
        self.exibir_combatentes()

        turno = 1
        while self.vivos(self.lado_a) and self.vivos(self.lado_b):
            print(f"--- TURNO {turno} ---")
            todos = self.vivos(self.lado_a) + self.vivos(self.lado_b)
            ordem = self.ordem_iniciativa(todos)

            for ator in ordem:
                # jogador ou monstro
                if not ator.esta_vivo():
                    continue

                # aplica status de turno (sangramento etc)
                if hasattr(ator, 'aplicar_status_turno'):
                    ator.aplicar_status_turno()
                else:
                    # monstros também podem ter status (simplificado)
                    pass

                # escolhe lado alvo
                if ator in self.lado_a:
                    inimigos = self.lado_b
                else:
                    inimigos = self.lado_a

                alvo = self.escolher_alvo_aleatorio(inimigos)
                if alvo is None:
                    break

                # lógica simples: se ator tem habilidades e é jogador, usa habilidade aleatória 30% das vezes
                if hasattr(ator, 'habilidades') and ator.habilidades and random.random() < 0.3:
                    indice = random.randrange(len(ator.habilidades))
                    ator.usar_habilidade(indice, alvo)
                else:
                    ator.atacar(alvo)

                # verifica se alvo morreu
                if not alvo.esta_vivo():
                    print(f"{alvo.nome} foi derrotado!")

                # verifica vitória
                if not self.vivos(self.lado_a) or not self.vivos(self.lado_b):
                    break

            turno += 1
            print()

        vencedor = "Lado A" if self.vivos(self.lado_a) else "Lado B"
        print("🏆 FIM DA BATALHA! 🏆")
        print(f"✨ VITÓRIA: {vencedor}! ✨\n")
        print("Sobreviventes:")
        for p in (self.vivos(self.lado_a) + self.vivos(self.lado_b)):
            print(f"  - {p.nome} (Vida restante: {p.vida})")



if __name__ == "__main__":
    # Criando heroínas
    evellyn = Invocadora("Evellyn", 110, 38)
    evellyn.arma = Arma("Cajado Estelar", 16)
    evellyn.adicionar_habilidade(LuzEstelar())
    evellyn.inventario.adicionar_item(Pocao("Poção Lunar", 40))

    lysandra = FeiticeiraSombras("Lysandra", 95, 45)
    lysandra.arma = Arma("Lâmina Noturna", 14)
    lysandra.adicionar_habilidade(LaminaSombria())

    mirella = ArqueiraFantasma("Mirella", 105, 33)
    mirella.arma = Arma("Arco Etéreo", 12)
    mirella.adicionar_habilidade(FlechaEterea())

    # Criando monstros
    g1 = Criatura.gargula_padrao()
    g2 = Criatura.drakanith()
    boss = Criatura.eremita_abismo()

    # Batalha 3v3
    batalha = Batalha([evellyn, lysandra, mirella], [g1, g2, boss])
    batalha.iniciar()

    # Exemplo de 1v1
    print("\n--- Exemplo 1v1 ---")
    conan = FeiticeiraSombras("Aldara", 100, 30)
    conan.arma = Arma("Espada Rúnica", 15)
    orc = Criatura("Orc Antigo", 100, 20, chance_critico=30)
    batalha2 = Batalha(conan, orc)
    batalha2.iniciar()
