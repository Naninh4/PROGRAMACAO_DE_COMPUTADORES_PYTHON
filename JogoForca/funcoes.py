import pygame
import random

def banco_de_dados(tema):
    forca_fruta = ["banana", "abacaxi", "morango", "laranja", "uva", "maçã", "pera", "melancia", "manga", "kiwi"]
    forca_cores = ["azul", "verde", "amarelo", "vermelho", "roxo", "laranja", "rosa", "preto", "branco", "marrom"]

    banco_de_palavras = {
        "frutas": forca_fruta,
        "cores": forca_cores,
    }
    return banco_de_palavras[tema]
def desenhar_forca(tela, erros):
 
    for i in range(0, erros):
        # Carrega e exibe a imagem da forca a cada erro
        imagem_forca = pygame.image.load(f"erro{i+1}.png")
        tela.blit(imagem_forca, (105, 96))
        
def desenhar_letras_adivinhadas(letras_adivinhadas,tela):
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render((" ".join(letras_adivinhadas)).capitalize(), True, (255, 255, 255))
    tela.blit(texto, (156, 351))
# tema = input()
# print(banco_de_dados(tema)[0])
