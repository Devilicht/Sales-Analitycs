import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import numpy as np


def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format


class Search:
    def __init__(self) -> pd.DataFrame : 
        self.df = pd.read_csv('./data/dataset.csv')

    def city_sales_value_by_category(self) -> str:

        filter_category = self.df[self.df['Categoria'] == 'Office Supplies']
        city_sale = filter_category.groupby('Cidade')['Valor_Venda'].sum().sort_values()
        top_city_sale = city_sale.idxmax()
        print("A cidade com maior valor de vendas de produtos na categoria 'Materiais de escritório' é",top_city_sale)


    def total_sales_by_order_date(self):
        group_data_value = self.df.groupby('Data_Pedido')['Valor_Venda'].sum()
        plt.figure(figsize = (20, 6))
        group_data_value.plot(color = 'green')
        plt.xlabel('Data Pedido'),plt.ylabel('Valor Vendas'),plt.title('Total de vendas por data')
        plt.show()

    def total_sales_by_state(self):   
        group_state_value = self.df.groupby('Estado')['Valor_Venda'].sum().reset_index()
        plt.figure(figsize = (16, 6))
        sea.barplot(data = group_state_value, 
                    y = 'Valor_Venda', 
                    x = 'Estado').set(title = 'Vendas por ano')   
        plt.xticks(rotation = 80)
        plt.show()

    def top_10_cities_by_sales(self):
        group_city_value = self.df.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False).head(10)        
        sea.set_palette('coolwarm')
        plt.figure(figsize = (16, 6))
        sea.barplot(data = group_city_value, 
                    y = 'Valor_Venda', 
                    x = 'Cidade').set(title = 'As 10 Cidades com Maior Total de Vendas ')
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

    def total_sales_by_segment_and_year(self):
        self.df['Data_Pedido'] = pd.to_datetime(self.df['Data_Pedido'], dayfirst = True)  
        self.df['Ano'] = self.df['Data_Pedido'].dt.year
        set_group = self.df.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
        df_plot = set_group.unstack('Segmento')

        df_plot.plot(kind='bar', stacked=True)

        plt.title('Vendas por ano e segmento')
        plt.xlabel('Ano')
        plt.ylabel('Valor de vendas')

        plt.show()

    def sales_discount(self):
        self.df['Desconto'] = np.where(self.df['Valor_Venda'] > 1000, 0.15, 0.10)
    
        self.df['Valor_Venda_Desconto'] = self.df['Valor_Venda'] - (self.df['Valor_Venda'] * self.df['Desconto'])
        sales_before = self.df.loc[self.df['Desconto'] == 0.15, 'Valor_Venda']
        sales_after = self.df.loc[self.df['Desconto'] == 0.15, 'Valor_Venda_Desconto']
        mean_before = round(sales_before.mean(), 2)
        mean_after = round(sales_after.mean(), 2)
        mean_values = [mean_before, mean_after]

        labels = ['Antes', 'Depois']

        plt.bar(labels, mean_values)

        plt.title('Comparação de vendas antes e depois do desconto')
        plt.xlabel('Desconto')
        plt.ylabel('Valor médio de venda')

        plt.show()

    def sales_average_by_segment_year_month(self):
        self.df['Data_Pedido'] = pd.to_datetime(self.df['Data_Pedido'], dayfirst=True)
        self.df['Mes'] = self.df['Data_Pedido'].dt.month
        self.df['Ano'] = self.df['Data_Pedido'].dt.year
        group = self.df.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])
        years = group.index.get_level_values(0)
        month = group.index.get_level_values(1)
        seg = group.index.get_level_values(2)
        sea.relplot(kind = 'line',
                        data = group, 
                        y = 'mean', 
                        x = month,
                        hue = seg, 
                        col = years,
                        col_wrap = 4)
        plt.show()

    def total_sales_by_subcategory_top12(self):
        df_dsa_p10 = self.df.groupby(['Categoria','SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda',ascending = False).head(12)
        df_dsa_p10 = df_dsa_p10[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()
        df_dsa_p10_cat = df_dsa_p10.groupby('Categoria').sum(numeric_only = True).reset_index()
        color_category = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']
        cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']
        
        fig, ax = plt.subplots(figsize = (18,12))

        p1 = ax.pie(df_dsa_p10_cat['Valor_Venda'], 
                    radius = 1,
                    labels = df_dsa_p10_cat['Categoria'],
                    wedgeprops = dict(edgecolor = 'white'),
                    colors = color_category)

        p2 = ax.pie(df_dsa_p10['Valor_Venda'],
                    radius = 0.9,
                    labels = df_dsa_p10['SubCategoria'],
                    autopct = autopct_format(df_dsa_p10['Valor_Venda']),
                    colors = cores_subcategorias, 
                    labeldistance = 0.7,
                    wedgeprops = dict(edgecolor = 'white'), 
                    pctdistance = 0.53,
                    rotatelabels = True)

        centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')

        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(df_dsa_p10['Valor_Venda']))), xy = (-0.2, 0))
        plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')
        plt.show()


