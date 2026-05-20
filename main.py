
vendas = 0
valor_b= 0
desconto_total = 0
final_total = 0
try:
    while True:
        print ('=== Sistema de vendas === \n')
        print ('1 - registrar venda')
        print ('2 - ver resumo parcial')
        print ('3 - Encerrar sistema')
        opcao = int(input('\nEscolha uma opção: '))
        

        if opcao == 1 :
            vendas += 1

            nome = input('Nome do produto: ')
            valor_unitario = float(input('Valor unitario: '))
            quantidade = int(input('Quantidade: '))
            valor_bruto = valor_unitario * quantidade
            valor_b += valor_bruto 
            print(f'Valor Total: R$ {valor_bruto:.2f}\n')

            

        elif opcao == 2:
            

            if valor_bruto < 100:
                desconto_total = valor_b* 0
        
        
            elif valor_b >=100 and valor_b < 499.99:
                desconto_total= valor_b * 0.05
                valor_desconto = ('5%')

            elif valor_b >= 500 and valor_b < 999.99:
                desconto_total = valor_b * 0.10
                valor_desconto = ('10%')

            else:
                desconto_total = valor_b * 0.15
                valor_desconto = ('15%')
                
            
            valor_final = valor_b - desconto_total
            print(f'Total de vendas realizadas: {vendas}')
            print(f'Total bruto vendido: R$ {valor_b:.2f}')
            print(f'Total de descontos concedidos: R$ {desconto_total:.2f}')
            print(f'Total líquido vendido: R$ {valor_final:.2f}\n')
            

        
        elif opcao == 3:
            print('=== resumo final ===')
            print(f'Total de vendas realizadas: {vendas}')
            print(f'Total bruto vendido: R$ {valor_b:.2f}')
            print(f'Total de descontos concedidos: R$ {desconto_total:.2f}')
            print(f'Total líquido vendido: R$ {valor_final:.2f}\n')
            print('Encerrando sistema...')
            break
except ValueError:
    print('Opção inválida. Por favor, escolha uma opção válida.')