from primitives import Ponto3, Vetor3
from math import sqrt


class Esfera:
    def __init__(self, centro: Ponto3, raio: float, cor: tuple):
        if raio <= 0:
            raise ValueError("O raio deve ser positivo e maior que zero.")
        self.centro = centro
        self.raio = raio
        self.cor = cor

    def intersecta(self, origem: Ponto3, direcao: Vetor3):
        """
        Calcula a interseção do raio com a esfera.
        origem: Ponto de origem do raio
        direcao: Vetor direção do raio (normalizado)
        Retorna a menor distância positiva ou None se não houver interseção.
        """
        L = self.centro - origem
        tca = L.dot(direcao)
        d2 = L.dot(L) - tca * tca
        r2 = self.raio * self.raio

        if d2 > r2:
            return None

        thc = sqrt(r2 - d2)
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0 and t1 < 0:
            return None

        return t0 if t0 > 0 else t1

class Plano:
    def __init__(self, ponto: Ponto3, normal: Vetor3, cor: tuple):
        if normal.magnitude() == 0:
            raise ValueError("O vetor normal ao plano não pode ser nulo.")
        self.ponto = ponto
        self.normal = normal.normalize()
        self.cor = cor

    def intersecta(self, origem: Ponto3, direcao: Vetor3):
        """
        Calcula a interseção do raio com o plano.
        origem: Ponto de origem do raio
        direcao: Vetor direção do raio (normalizado)
        Retorna a distância positiva ou None se não houver interseção.
        """
        denominador = self.normal.dot(direcao)

        if abs(denominador) < 1e-6:
            return None

        t = (self.ponto - origem).dot(self.normal) / denominador
        return t if t >= 0 else None

# Função para renderizar a cena
def renderizar(camera, objetos):
    largura = camera.largura_resolucao
    altura = camera.altura_resolucao

    imagem = [[(0, 0, 0) for _ in range(largura)] for _ in range(altura)]

    for i in range(altura):
        for j in range(largura):
            pixel_pos = camera.calcular_ponto_tela(i, j)
            direcao = (pixel_pos - camera.posicao).normalize()

            cor_pixel = (0, 0, 0)  # Cor de fundo
            menor_distancia = float('inf')

            for objeto in objetos:
                distancia = objeto.intersecta(camera.posicao, direcao)

                if distancia is not None and distancia < menor_distancia:
                    menor_distancia = distancia
                    cor_pixel = objeto.cor

            imagem[i][j] = cor_pixel

    return imagem