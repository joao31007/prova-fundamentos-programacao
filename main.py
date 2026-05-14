
sistema_vendas = True
while sistema_vendas:
    print ('=== Sistema de vendas ===')
    print ('1 - registrar venda')
    print ('2 - ver resumo parcial')
    print ('3 - Encerrar sistema')
    opcao = int(input('Escolha uma opção: '))
    
    registro_vendas = []  

    if opcao == 1 :
        vendas = 0
        bruto_total = 0
        desconto_total = 0
        final_total = 0 

        nome = input('Nome do produto: ')
        valor_unitario = float(input('Valor unitario: '))
        quantidade = int(input('Quantidade: '))

        valor_bruto = valor_unitario * quantidade
        print(f'Valor: R$ {valor_bruto:.2f}')

        if valor_bruto < 100:
            desconto = valor_bruto * 0
       
    
        elif valor_bruto >=100 and valor_bruto < 499.99:
            desconto = valor_bruto * 0.05
            valor_desconto = ('5%')

        elif valor_bruto >= 500 and valor_bruto < 999.99:
            desconto = valor_bruto * 0.10
            valor_desconto = ('10%')

        else:
            desconto = valor_bruto * 0.15
            valor_desconto = ('15%')
            
        
        valor_final = valor_bruto - desconto
          
        registro_vendas.append((nome, quantidade, valor_bruto, desconto, valor_final))
        
    
        print(f'Desconto aplicado: R$ {desconto: .2f}')
        print(f'valor do desconto: R$ {valor_desconto}')
        print(f'valor final da venda: R$ {valor_final:.2f} \n')
        

    elif opcao == 2:
        registro_vendas = opcao == 1 
       
        vendas = len(registro_vendas)
        bruto_total = sum(venda[2] for venda in registro_vendas)
        desconto_total = sum(venda[3] for venda in registro_vendas)
        final_total = sum(venda[4] for venda in registro_vendas)
      
        print(f'Total de vendas realizadas: {vendas}')
        print(f'Total bruto vendido: R$ {bruto_total:.2f}')
        print(f'Total de descontos concedidos: R$ {desconto_total:.2f}')
        print(f'Total líquido vendido: R$ {final_total:.2f}')
    
    elif opcao == 3:
        print('=== resumo final ===')
        registro_vendas = opcao == 2
       
        vendas = len(registro_vendas)
        bruto_total = sum(venda[2] for venda in registro_vendas)
        desconto_total = sum(venda[3] for venda in registro_vendas)
        final_total = sum(venda[4] for venda in registro_vendas)
      

        