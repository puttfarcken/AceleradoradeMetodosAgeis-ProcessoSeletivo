valorUnitario = 4.50
icms = 18 / 100
ipi = 4 / 100
pis = 1.86 / 100
cofins = 8.54 / 100

qtdempresasfaturadas = int (input('Quantidade de empresas a serem a faturadas:'))

while qtdempresasfaturadas > 0:
    empresa = str (input("Nome da empresa: "))
    qtd = int (input("Quantidade de energéticos a ser faturada: "))
    
    mercadorias = qtd * valorUnitario

    valorIcms = mercadorias * icms
    valorIpi = mercadorias * ipi
    valorPis = mercadorias * pis
    valorCofins = mercadorias * cofins

    impostos = valorIcms + valorIpi + valorPis + valorCofins

    total = mercadorias + impostos

    print ('-----ENERGÉTICOS ACCELERATOR-----')
    print ('Cliente: {}'.format(empresa))
    print ('ICMS: R$ {}; IPI: R$ {}; PIS: R$ {:.2f}; COFINS: R$ {:.2f}'.format(valorIcms, valorIpi, valorPis, valorCofins))
    print ('Impostos: R$ {:.2f} \nMercadorias: R$ {:.2f} \nTotal: R$ {:.2f}'.format(impostos, mercadorias, total))
    
    qtdempresasfaturadas -= 1

    totalMercadorias = mercadorias + mercadorias
    totalImpostos = impostos + impostos
    totalGeral = total + total

print ('----------Total Nota----------')
print ('Total Impostos: R$ {:.2f} \nTotal Mercadorias: R$ {:.2f} \nTotal Geral: R$ {:.2f}'.format(totalImpostos, totalMercadorias, totalGeral))