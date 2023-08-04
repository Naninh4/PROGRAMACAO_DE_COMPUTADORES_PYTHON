import pygame
from funcoes import *
import random
import sys

temacores = False
temafrutas = False
tela_p = True
tela_j = False



def tela2(tema):
    pygame.init()
    telaatual = pygame.display.set_mode((400, 400))
    forca = []
    erros = 0
    g = False
    p =  False

    # Carrega a imagem do botão
    if tema == "f":
        palavra_secreta = random.choice(banco_de_dados("frutas"))
        pygame.display.set_caption("Bem vindo a forca FRUTAS")
        tematica = pygame.image.load("temafrutas.png")
    if tema == "c":
        palavra_secreta = random.choice(banco_de_dados("cores"))
        pygame.display.set_caption("Bem vindo a forca CORES")
        tematica = pygame.image.load("temacor.png")

    for x in palavra_secreta:
        forca.append("_")

    largura, altura = tematica.get_size()
    img_tematica  = pygame.Rect(15,13,largura,altura )
    largura, altura = (pygame.image.load("folhagemr.png")).get_size()
    folhagemr  = pygame.Rect(300,162,largura,altura )
    largura, altura = (pygame.image.load("folhageml.png")).get_size()
    folhagemf  = pygame.Rect(0,162,largura,altura )
    largura, altura = (pygame.image.load("centroflor.png")).get_size()
    centrorosa  = pygame.Rect(172.25,171.57,largura,altura )
    
    largura, altura = (pygame.image.load("ganhou.png")).get_size()
    ganhou  = pygame.Rect(49,159,largura,altura )
    
    largura, altura = (pygame.image.load("perdeu.png")).get_size()
    perdeu  = pygame.Rect(45,274,largura,altura )

    largura, altura = (pygame.image.load("legenda.png")).get_size()
    lege  = pygame.Rect(19,300,largura,altura )
    
    largura, altura = (pygame.image.load("Palavra_.png")).get_size()
    label_palavra  = pygame.Rect(7,354,largura,altura )


    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                global tela_p, tela_j, temacores, temafrutas
                temacores = False
                temafrutas = False
                tela_j = False
                tela_p = True
                main()
  
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if  evento.key == pygame.K_r and (g == True or p == True):
                    rodando = False
                    temacores = False
                    temafrutas = False
                    tela_j = False
                    tela_p = True
                    main()
                # Verificar se a letra está correta
                chute = pygame.key.name(evento.key)
                if chute.isalpha():
                    chute = chute.upper()
                    if chute in palavra_secreta.upper():
                        index = 0
                        for letra in palavra_secreta:
                            if chute == letra.upper():
                                forca[index] = letra
                            index += 1
                    else:
                        erros += 1
            
        telaatual.fill((255, 87, 127))
        telaatual.blit(tematica,(img_tematica.x, img_tematica.y))
        telaatual.blit(pygame.image.load("folhagemr.png"),(folhagemr.x, folhagemr.y))
        telaatual.blit(pygame.image.load("folhageml.png"),(folhagemf.x, folhagemf.y))
        telaatual.blit(pygame.image.load("centroflor.png"),(centrorosa.x, centrorosa.y))
        telaatual.blit(pygame.image.load("Palavra_.png"),(label_palavra.x, label_palavra.y))
        if not g and not p:
            telaatual.blit(pygame.image.load("legenda.png"),(lege.x, lege.y))
        desenhar_letras_adivinhadas(forca, telaatual)
        desenhar_forca(telaatual, erros)
        # Verificar se o jogador acertou ou enforcou
        pala = "".join(forca)
        if pala == palavra_secreta and not p:
                g = True
                telaatual.blit(pygame.image.load("ganhou.png"),(ganhou.x, ganhou.y))

        if erros >= 8:
                p = True
                forca = palavra_secreta
                telaatual.blit(pygame.image.load("perdeu.png"),(perdeu.x, perdeu.y))
                desenhar_letras_adivinhadas(forca, telaatual)
        # Atualiza a tela
        pygame.display.flip()
    pygame.quit()
def tela1():
    pygame.init()
    telaprincipal = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Bem vindo a forca")

    # Carrega a imagem do botão
    botao_fruta = pygame.image.load("frutas_botao.png")
    botao_cores = pygame.image.load("cores_botao.png")
    enfeite_flor = pygame.image.load("enfeite_flor.png")
    cabecalho = pygame.image.load("cabecalho.png")
  

    # Obtém as dimensões da imagem do botão
  
    largura, altura = botao_fruta.get_size()
    # Cria um retângulo para representar a área do botão na tela
    botaof = pygame.Rect(32,155,largura,altura )
    largura, altura = botao_cores.get_size()
    botaoc = pygame.Rect(214,155,largura,altura )
    largura, altura = cabecalho.get_size()
    cabe = pygame.Rect(54,27,largura,altura )
    largura, altura = enfeite_flor.get_size()
    enfei = pygame.Rect(-18,268,largura,altura )

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o botão foi clicado
                if botaof.collidepoint(evento.pos):
                    global temacores, temafrutas
                    temacores = False
                    temafrutas = True
                    print("Botão frutas foi clicado!")
                    return False
                if botaoc.collidepoint(evento.pos): 
                    temacores = True
                    temafrutas = False

                    print("Botão cores foi clicado!")
                    return  False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        # Preenche a tela com a cor branca (RGB: 255, 255, 255)
        telaprincipal.fill((255, 87, 127))

        # Desenha a imagem do botão na tela
        telaprincipal.blit(botao_fruta, (botaof.x, botaof.y))
        telaprincipal.blit(botao_cores, (botaoc.x, botaoc.y))
        telaprincipal.blit(cabecalho, (cabe.x, cabe.y))
        telaprincipal.blit(enfeite_flor, (enfei.x, enfei.y))

        # Atualiza a tela
        pygame.display.flip()
    pygame.quit()
def main():
    global tela_p, tela_j
    while tela_p and tela_j == False:
        tela_p = tela1()
    tela_j = True
    while tela_j:
        if temacores == True:
            print(temacores)
            tela_j = tela2("c")
        if temafrutas == True:
            print(temafrutas)
            tela_j = tela2("f")
if __name__ == "__main__":
    main()
