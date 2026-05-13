
sistema_vendas = True
while sistema_vendas:
    print ('=== Sistema de vendas ===')
    print ('1 - registrar venda')
    print ('2 - ver resumo parcial')
    print ('3 - Encerrar sistema')
    opcao = int(input('Escolha uma opção: '))
    
    vendas = opcao == 1
    bruto_total = 0
    desconto_total = 0
    final_total = 0     

    if opcao == 1 :
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
          
        vendas += 1
        bruto_total += valor_bruto
        desconto_total += desconto  
        final_total += valor_final
      
    
        print(f'Desconto aplicado: R$ {desconto: .2f}')
        print(f'valor do desconto: R$ {valor_desconto}')
        print(f'valor final da venda: R$ {valor_final:.2f}')
        

    elif opcao == 2:
        print(f'Total de vendas realizadas: {vendas}')
        print(f'Total bruto vendido: R$ {bruto_total:.2f}')
        print(f'Total de descontos concedidos: R$ {desconto_total:.2f}')
        print(f'Total líquido vendido: R$ {final_total:.2f}')

        