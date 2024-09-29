meta = 50000
qtd_venda = 150000

if qtd_venda >= meta:
    print(f'Vendemos muito bem, o total é {float(qtd_venda)} unidade!')
else:
    print(f'Não conseguimos vender bem! Força e Continue.')

meta = 20000
vendas_realizadas = 25000


if vendas_realizadas < meta:
    print('não ganhou o bonus')
elif vendas_realizadas > (meta * 2):
    bonus = 0.07 * vendas_realizadas 
    print(f'Ganhou {bonus} de bonus')
else:
    bonus = 0.03 * vendas_realizadas
    print(f'ganhou {bonus} de bonus')