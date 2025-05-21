# generar_graficos.py
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

################################

def generar_grafico_barras_fuentes(output_path):
    fuentes = {
        'Eólica': ('csv/08 wind-generation.csv', 'Electricity from wind (TWh)'),
        'Solar': ('csv/12 solar-energy-consumption.csv', 'Electricity from solar (TWh)'),
        'Hidro': ('csv/05 hydropower-consumption.csv', 'Electricity from hydro (TWh)'),
        'Biocombustibles': ('csv/16 biofuel-production.csv', 'Biofuels Production - TWh - Total')
        # 'Geotérmica' excluida para evitar distorsión
    }

    data_frames = {}

    for nombre, (archivo, columna) in fuentes.items():
        df = pd.read_csv(archivo)

        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encontró en {archivo}")
        df = df[['Year', columna]]
        df = df.groupby('Year').mean().reset_index()
        df = df.rename(columns={columna: nombre})
        data_frames[nombre] = df

    df_combined = pd.DataFrame({'Year': range(1965, 2022)})

    for nombre, df in data_frames.items():
        df_combined = pd.merge(df_combined, df, on='Year', how='left')

    df_combined = df_combined.fillna(0)

    colores = {
        'Eólica': '#4f99ff',
        'Solar': '#ffc107',
        'Hidro': '#00c49a',
        'Biocombustibles': '#ff7043'
    }

    fig, ax = plt.subplots(figsize=(8, 6))

    def update(year):
        ax.clear()
        datos = df_combined[df_combined['Year'] == year].iloc[0]
        fuentes_ordenadas = list(fuentes.keys())
        valores = [datos[f] for f in fuentes_ordenadas]

        barras = ax.bar(fuentes_ordenadas, valores, color=[colores[f] for f in fuentes_ordenadas])
        ax.set_title(f"Producción de Energía Renovable por Fuente ({year})", fontsize=14)
        ax.set_ylabel("Producción (TWh)")
        ax.set_ylim(0, max(df_combined[fuentes_ordenadas].max()) * 1.1)
        ax.grid(True, which='major', axis='y', linestyle='--', alpha=0.7)

        for barra, valor in zip(barras, valores):
            ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height(),
                    f'{valor:.1f}', ha='center', va='bottom', fontsize=9)

    ani = FuncAnimation(fig, update, frames=df_combined['Year'], repeat=False, interval=700)

    os.makedirs(output_path, exist_ok=True)
    ani.save(os.path.join(output_path, 'grafico_barras_renovables.gif'), writer='pillow')

################################

def generar_grafico_torta_renovables(output_path):
    # Leer los archivos CSV
    df_total = pd.read_csv('csv/04 share-electricity-renewables.csv')
    df_wind = pd.read_csv('csv/11 share-electricity-wind.csv')
    df_solar = pd.read_csv('csv/15 share-electricity-solar.csv')
    df_hydro = pd.read_csv('csv/07 share-electricity-hydro.csv')

    # Eliminar filas con valores faltantes
    dfs = [df_total, df_wind, df_solar, df_hydro]
    for i in range(len(dfs)):
        dfs[i] = dfs[i].dropna(subset=[dfs[i].columns[-1]])

    df_total['Renewables'] = df_total[df_total.columns[-1]]
    df_wind['Wind'] = df_wind[df_wind.columns[-1]]
    df_solar['Solar'] = df_solar[df_solar.columns[-1]]
    df_hydro['Hydro'] = df_hydro[df_hydro.columns[-1]]

    # Años comunes
    years = sorted(set(df_total['Year']) & set(df_wind['Year']) &
                   set(df_solar['Year']) & set(df_hydro['Year']))
    years = [y for y in years if 1965 <= y <= 2021]

    # Crear la figura
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.axis('equal')  # Para que el gráfico sea circular
    title = ax.set_title('', fontsize=14)

    def get_avg(df, year, col):
        return df[df['Year'] == year][col].mean()

    def update(year):
        ax.clear()
        ax.axis('equal')

        wind = get_avg(df_wind, year, 'Wind')
        solar = get_avg(df_solar, year, 'Solar')
        hydro = get_avg(df_hydro, year, 'Hydro')
        total = get_avg(df_total, year, 'Renewables')
        others = max(0, total - (wind + solar + hydro))

        valores = [wind, solar, hydro, others]
        etiquetas = ['Eólica', 'Solar', 'Hidro', 'Otras']
        colores = ['#4f99ff', '#ffc107', '#00c49a', '#8884d8']

        ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', colors=colores, startangle=140)
        ax.set_title(f'Participación de Energías Renovables ({year})', fontsize=13)

    ani = FuncAnimation(fig, update, frames=years, repeat=False, interval=700)
    os.makedirs(output_path, exist_ok=True)
    gif_path = os.path.join(output_path, 'grafico_torta_renovables.gif')
    ani.save(gif_path, writer='pillow')

################################

def generar_grafico_lineas_capacidad(output_path):
    # Archivos fuente
    fuentes = {
        'Eólica': ('csv/09 cumulative-installed-wind-energy-capacity-gigawatts.csv', 'Wind Capacity'),
        'Solar': ('csv/13 installed-solar-PV-capacity.csv', 'Solar Capacity'),
        'Geotérmica': ('csv/17 installed-geothermal-capacity.csv', 'Geothermal Capacity'),
    }

    dfs = {}

    # Leer y procesar cada archivo
    for nombre, (archivo, columna) in fuentes.items():
        df = pd.read_csv(archivo)
        df_filtrado = df[['Year', columna]].groupby('Year').mean().reset_index()
        dfs[nombre] = df_filtrado

    # Base final unificada
    df_final = pd.DataFrame({'Year': dfs['Eólica']['Year']})
    for nombre in ['Eólica', 'Solar', 'Geotérmica']:
        df_final[nombre] = dfs[nombre][dfs[nombre].columns[1]]

    df_final = df_final[(df_final['Year'] >= 1965) & (df_final['Year'] <= 2021)].fillna(0)

    # Configurar gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    colores = {
        'Eólica': '#4f99ff',
        'Solar': '#ffc107',
        'Geotérmica': "#b02727"
    }

    def update(year):
        ax.clear()
        df_parcial = df_final[df_final['Year'] <= year]
        for fuente in ['Eólica', 'Solar', 'Geotérmica']:
            ax.plot(df_parcial['Year'], df_parcial[fuente], label=fuente, color=colores[fuente], marker='o')
        ax.set_title(f"Capacidad Instalada de Energías Renovables ({year})", fontsize=13)
        ax.set_ylabel("Capacidad Instalada (GW)", fontsize=11)
        ax.set_xlabel("Año", fontsize=11)
        ax.set_xlim(df_final['Year'].min(), df_final['Year'].max())
        ax.set_ylim(0, df_final[['Eólica', 'Solar', 'Geotérmica']].max().max() * 1.1)
        ax.grid(True, which='major', axis='y', linestyle='--', alpha=0.7)
        ax.legend(fontsize=10)

    ani = FuncAnimation(fig, update, frames=df_final['Year'], repeat=False, interval=700)

    # Guardar como GIF
    os.makedirs(output_path, exist_ok=True)
    gif_path = os.path.join(output_path, 'grafico_lineas_capacidad.gif')
    ani.save(gif_path, writer='pillow')

################################

def generar_grafico_area_comparativo(output_path):
    df_renovable = pd.read_csv('csv/02 modern-renewable-energy-consumption.csv')

    # Extraer columnas relevantes
    columnas_renovables = df_renovable.columns[-4:]  # Últimas 4 columnas: Geo Biomass, Solar, Wind, Hydro
    df_renovable = df_renovable[['Year'] + list(columnas_renovables)]

    # Agrupar por año y sumar fuentes renovables
    df_agrupado = df_renovable.groupby('Year').sum().reset_index()
    df_agrupado = df_agrupado[(df_agrupado['Year'] >= 1990) & (df_agrupado['Year'] <= 2022)].fillna(0)

    # Animación de gráfico de área
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ['#a4de6c', '#00c49a', '#ffc658', '#4f99ff']  # Biomasa, Solar, Wind, Hydro

    def update(year):
        ax.clear()
        df_parcial = df_agrupado[df_agrupado['Year'] <= year]
        ax.stackplot(
            df_parcial['Year'],
            df_parcial[columnas_renovables[0]],
            df_parcial[columnas_renovables[1]],
            df_parcial[columnas_renovables[2]],
            df_parcial[columnas_renovables[3]],
            labels=['Biomasa / Geo / Otras', 'Solar', 'Eólica', 'Hidroeléctrica'],
            colors=colors,
            alpha=0.8
        )
        ax.set_title(f"Comparativo de Energía Renovable por Fuente - {year}", fontsize=14)
        ax.set_ylabel("Consumo de Energía Renovable (TWh)")
        ax.set_xlabel("Año")
        ax.set_xlim(df_agrupado['Year'].min(), df_agrupado['Year'].max())
        ax.set_ylim(0, df_agrupado[columnas_renovables].sum(axis=1).max() * 1.1)
        ax.legend(loc='upper left')

    ani = FuncAnimation(fig, update, frames=df_agrupado['Year'], repeat=False, interval=700)
    ani.save(os.path.join(output_path, 'grafico_area_renovables.gif'), writer='pillow')
