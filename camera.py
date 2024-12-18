from primitives import Ponto3, Vetor3


class Camera:
    def __init__(self, 
                 posicao: Ponto3, 
                 mira: Ponto3, 
                 vetor_up: Vetor3, 
                 distancia_tela: float, 
                 altura_resolucao: int, 
                 largura_resolucao: int):
        if vetor_up.magnitude() == 0:
            raise ValueError("O vetor para cima (vetor_up) não pode ser nulo.")

        self.posicao = posicao
        self.mira = mira
        self.vetor_up = vetor_up.normalize()
        self.distancia_tela = distancia_tela
        self.altura_resolucao = altura_resolucao
        self.largura_resolucao = largura_resolucao

        # Vetores ortonormais
        self.w = (self.posicao - self.mira).normalize()
        self.u = self.vetor_up.cross(self.w).normalize()
        self.v = self.w.cross(self.u).normalize()

        # Dimensões dos pixels
        self.tamanho_pixel_h = 1 / largura_resolucao
        self.tamanho_pixel_v = 1 / altura_resolucao

    def calcular_ponto_tela(self, i, j):
        """
        Calcula a posição do centro do pixel (i, j) na tela.
        i: linha do pixel (0 é o pixel mais alto)
        j: coluna do pixel (0 é o pixel mais à esquerda)
        Retorna um ponto 3D na tela no espaço do mundo.
        """
        if not (0 <= i < self.altura_resolucao and 0 <= j < self.largura_resolucao):
            raise ValueError("Índices do pixel fora do intervalo da resolução da tela.")

        # Centro da tela no espaço do mundo
        centro_tela = self.posicao - self.w * self.distancia_tela

        # Vetor para o pixel na direção horizontal e vertical
        deslocamento_h = self.u * (j - (self.largura_resolucao - 1) / 2) * self.tamanho_pixel_h
        deslocamento_v = self.v * ((self.altura_resolucao - 1) / 2 - i) * self.tamanho_pixel_v

        return centro_tela + deslocamento_h + deslocamento_v

    def __repr__(self):
        return (f"Camera(posicao={self.posicao}, mira={self.mira}, vetor_up={self.vetor_up}, "
                f"distancia_tela={self.distancia_tela}, altura_resolucao={self.altura_resolucao}, "
                f"largura_resolucao={self.largura_resolucao})")