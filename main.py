"""Arquivo principal que será interpretado pelo interpretador."""
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    import math
    area=input(' tamanho em metros quadrados da área a ser pintada: ')
    area=float(area)
    area_total=area + 0.1*area
    litros=area_total/6
    apenas_18=(litros/18)
    apenas_18=float(apenas_18)
    apenass_18=int(math.ceil(apenas_18))
    apenass_18=int(apenass_18)
    apenasss_18=apenass_18*80
    apenas_36=(litros/3.6)
    apenas_36=float(apenas_36)
    apenass_36=int(math.ceil(apenas_36))
    apenass_36=int(apenass_36)
    apenasss_36=apenass_36*25
    economia=litros/3.6
    economia=float(economia)
    economiax=economia/5
    economiax=float(economiax)
    qt_latas=math.floor(economiax)
    qt_latas=int(qt_latas)
    sqt_latas=qt_latas*80
    sqt_latas=float(sqt_latas)
    economiaxx=economia - (qt_latas*5)
    economiaxx=float(economiaxx)
    qt_galoes=int(math.ceil(economiaxx))
    qt_galoes=int(qt_galoes)
    sqt_galoes=qt_galoes*25
    sqt_galoes=float(sqt_galoes)
    sqt_galoeslatas=sqt_galoes+sqt_latas
    print(f'O valor gasto comprando apenas latas é de R$ {apenasss_18:.2f}.')
    print(f'Serão necessárias {apenass_18} latas.')
    print(f'O valor gasto comprando apenas galões é de R$ {apenasss_36:.2f}.')
    print(f'Serão necessários {apenass_36} galões.')
    print(f'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ {sqt_galoeslatas:.2f}.')
    print(f'Serão necessárias {qt_latas} latas e {qt_galoes} galões.')
   



if __name__ == '__main__':
    main()
