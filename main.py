from primitives import Ponto3, Vetor3
from camera import Camera
from intersection import Esfera, Plano, renderizar
import matplotlib.pyplot as plt


def main():
    # Configuração da câmera
    camera_pos = Ponto3(0, 0, 0)
    camera_mira = Ponto3(0, 0, -1)
    camera_up = Vetor3(0, 1, 0)
    distancia_tela = 1.0
    altura_resolucao = 500
    largura_resolucao = 500

    camera = Camera(camera_pos, camera_mira, camera_up, distancia_tela, altura_resolucao, largura_resolucao)

    # Configuração dos objetos
    esfera1 = Esfera(Ponto3(0, 0, -3), 1, (1, 0, 0))  # Esfera vermelha
    esfera2 = Esfera(Ponto3(2, 0, -4), 1, (0, 1, 0))  # Esfera verde
    plano = Plano(Ponto3(0, -1, 0), Vetor3(0, 1, 0), (0.5, 0.5, 0.5))  # Plano cinza

    objetos = [esfera1, esfera2, plano]

    # Renderizar a cena
    imagem = renderizar(camera, objetos)

    # Salvar a imagem
    plt.imshow(imagem)
    plt.axis('off')
    plt.savefig("renderizacao.png", bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()