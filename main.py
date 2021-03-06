import blackjack as bj
import os, platform

def main():
    def limpar_tela():
        os_name = platform.system()
        if 'Windows' in os_name:
            os.system('cls')
        else:
            os.system('clear')

    def mensagem_vitoria_jogador(jogador):
        print('Parabéns {0}, você venceu a rodada! {1}'.format(
            jogador.nome(), 
            '\U0001F44F' * 10)
        )

    def mensagem_derrota_jogador(jogador):
        print(f'{jogador.nome()}, você perdeu a rodada! \U0001F44E')

    def mensagem_empate():
        print(f'A rodada terminou em empate! \U0001F450')

    def exibir_boas_vindas():
        print(f'===============\u2660\u2665\u2666\u2663===============')
        print('  Seja bem-vindo ao blackjack  ')
        print(f'===============\u2660\u2665\u2666\u2663===============')

    limpar_tela()
    exibir_boas_vindas()
    dealer = bj.Dealer()

    nome_incorreto = True
    while nome_incorreto:    
        print('Informe seu nome: ', end='')
        nome = str(input(''))
        if len(nome.strip()) > 0: 
            nome_incorreto = False
        else:
            limpar_tela()
            exibir_boas_vindas()
            print(f'Nome inválido')

    jogador = bj.Jogador(nome.capitalize())
    continuar_jogando = True
    while continuar_jogando:    
        dealer.iniciar_jogo()
        limpar_tela()
        jogador.receber_cartas(dealer.entregar_cartas_jogador())    

        # Caso o jogador já tenha 21 no entregar das cartas
        somatorio_jogador = dealer.somatorio_cartas(jogador.cartas())
        escolher_decisao = True if somatorio_jogador < 21 else False
        while escolher_decisao:
            print('************************ Mesa ************************')
            print(f'Dealer: {str(dealer.cartas_str()).split(" ")[0]} -     ', end='')
            print(f'Você: {jogador.cartas_str()}({dealer.somatorio_cartas(jogador.cartas())})', end="\n\n")

            print('-------------------')
            print('1 - Comprar carta')
            print('2 - Parar de jogar')
            print('-------------------')
            print('O que deseja fazer? ', end='')
            decisao = str(input(''))
            if decisao not in ['1', '2']:    
                limpar_tela()
                continue
            else:
                limpar_tela()
                if decisao == '1':
                    jogador.receber_carta(dealer.entregar_carta())                    
                    somatorio_jogador = dealer.somatorio_cartas(jogador.cartas())
                    if somatorio_jogador == 21: 
                        escolher_decisao = False
                    elif somatorio_jogador > 21: 
                        escolher_decisao = False
                    else: 
                        continue
                else:                    
                    escolher_decisao = False

        resultado = dealer.resultado_jogador(jogador)
        if resultado == -1:
            mensagem_derrota_jogador(jogador)                    
        elif resultado == 0:
            mensagem_empate()                        
        else:
            mensagem_vitoria_jogador(jogador)

        print(f'Suas cartas: {jogador.cartas_str()}({dealer.somatorio_cartas(jogador.cartas())})')
        print(f'Cartas do Dealer: {dealer.cartas_str()}({dealer.somatorio_cartas(dealer.cartas())})')
        dealer.receber_cartas_jogador(jogador.entregar_cartas())
        print('Deseja jogar novamente?')
        continuar_jogando = True if str(input()).upper() == 'S' else False

if __name__ == "__main__":
    main()