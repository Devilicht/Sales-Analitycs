import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import datetime as dt


def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format


class Search:
    def __init__(self) -> pd.DataFrame : 
        self.df = pd.read_csv('../data/dataset.csv')

    def city_sales_value_by_category(self) -> str:

        filter_category = self.df[self.df['Categoria'] == 'Office Supplies']
        city_sale = filter_category.groupby('Cidade')['Valor_Venda'].sum().sort_values()
        top_city_sale = city_sale.idxmax()
        print("City with the Highest Sales Value for Products in the 'Office Supplies' Category is",top_city_sale)


    def total_sales_by_order_date(self):
        group_data_value = self.df.groupby('Data_Pedido')['Valor_Venda'].sum()
        print(group_data_value)
        plt.figure(figsize = (20, 6))
        group_data_value.plot(color = 'green')
        plt.xlabel('Order Date'),plt.ylabel('Sales Value'),plt.title('Total sales by order date')
        plt.show()

    def total_sales_by_state(self):   
        group_state_value = self.df.groupby('Estado')['Valor_Venda'].sum().reset_index()
        plt.figure(figsize = (16, 6))
        sea.barplot(data = group_state_value, 
                    y = 'Valor_Venda', 
                    x = 'Estado').set(title = 'Sales by State')   
        plt.xticks(rotation = 80)
        plt.show()

    def top_10_cities_by_sales(self):
        group_city_value = self.df.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False).head(10)        
        sea.set_palette('coolwarm')
        plt.figure(figsize = (16, 6))
        sea.barplot(data = group_city_value, 
                    y = 'Valor_Venda', 
                    x = 'Cidade').set(title = 'Top 10 Cities by Sales')
        plt.show()

    def segment_with_highest_sales(self):
        group_seg_sales = self.df.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda',ascending = False)
        plt.figure(figsize = (16, 6))

        plt.pie(group_seg_sales['Valor_Venda'], 
                labels = group_seg_sales['Segmento'],
                autopct = autopct_format(group_seg_sales['Valor_Venda']),
                startangle = 90)

        centre_circle = plt.Circle((0, 0), 0.82, fc = 'white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(group_seg_sales['Valor_Venda']))), xy = (-0.25, 0))
        plt.title('Total de Vendas Por Segmento')
        plt.show()

    #Total de Vendas Por Segmento e Por Ano
    def total_sales_by_segment_and_year(self):
        self.df['Ano'] = pd.to_datetime(self.df['Data_Pedido'], format='%d/%m/%Y').dt.year
        group = self.df.groupby(['Segmento', 'Ano'])['Valor_Venda'].sum().reset_index()
        print(group)

s = Search()

s.total_sales_by_order_date()