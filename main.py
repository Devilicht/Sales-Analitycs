
from features.data_query import Search
from os import system as cmd, name as osname
from time import sleep

def clearScreen():
    cmd('cls' if osname == 'nt' else 'clear')

search = Search()

while True:
    choice = int(input("Escolha uma opção:\n"
                    "1 - Cidade com maior valor de vendas de produtos na categoria 'Materiais de escritório\n"
                    "2 - Total de vendas por data\n3 - Vendas por estado\n"
                    "4 - As 10 cidades com maior total de vendas\n"
                    "5 - Total de vendas por segmento\n"
                    "6 - Total de vendas por segmento e ano\n"
                    "7 - Desconto em vendas\n"
                    "8 - Média de vendas por segmento, ano e mês\n"
                    "9 - Total de vendas por subcategoria (top 12)\n"
                    "0 - Sair\n"
                    "Opção: "))

    if choice == 1:
        search.city_sales_value_by_category()
        sleep(3)
        clearScreen()
        
    elif choice == 2:
        search.total_sales_by_order_date()
        clearScreen()

    elif choice == 3:
        search.total_sales_by_state()
        clearScreen()

    elif choice == 4:
        search.top_10_cities_by_sales()
        clearScreen()

    elif choice == 5:
        search.segment_with_highest_sales()
        clearScreen()

    elif choice == 6:
        search.total_sales_by_segment_and_year()
        clearScreen()

    elif choice == 7:
        search.sales_discount()
        clearScreen()

    elif choice == 8:
        search.sales_average_by_segment_year_month()
        clearScreen()

    elif choice == 9:
        search.total_sales_by_subcategory_top12()
        clearScreen()

    elif choice == 0:
        break

    else:
        print("Opção inválida.")
        sleep(3)
        clearScreen()
