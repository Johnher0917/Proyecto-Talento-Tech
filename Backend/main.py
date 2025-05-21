from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import os
from typing import List
from generar_graficos import generar_grafico_torta_renovables, generar_grafico_barras_fuentes, generar_grafico_lineas_capacidad, generar_grafico_area_comparativo
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/graphics", StaticFiles(directory="graphics"), name="graphics")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

CSV_DIR = "csv"

# Todos los archivos disponibles (los mantendremos cargados para usarlos luego)
csv_files = {
    "solar": "12 solar-energy-consumption.csv",
    "wind": "08 wind-generation.csv",
    "hydro": "05 hydropower-consumption.csv",
    "geothermal": "17 installed-geothermal-capacity.csv",
    "renovables_porcentaje": "04 share-electricity-renewables.csv"  # NUEVO
}

data = {}

# Cargar todos los archivos
for key, filename in csv_files.items():
    path = os.path.join(CSV_DIR, filename)
    try:
        df = pd.read_csv(path)
        data[key] = df
    except Exception as e:
        print(f"Error cargando {filename}: {e}")

# Modelo de entrada y salida
class CalculoInput(BaseModel):
    pais: str
    anio: int
    consumo_kwh: float

class CalculoOutput(BaseModel):
    proporcion_renovable: float  # en decimal (ej: 0.42)
    consumo_renovable_estimado: float
    porcentaje_estimado: float   # en %

# Endpoint para obtener lista de países (basado en el CSV principal de renovables)
@app.get("/paises", response_model=List[str])
def listar_paises():
    df = data.get("renovables_porcentaje")
    if df is None:
        raise HTTPException(status_code=500, detail="Datos de países no disponibles")
    
    if "Entity" not in df.columns:
        raise HTTPException(status_code=500, detail="Columna 'Entity' no encontrada")
    
    paises = df["Entity"].dropna().unique()
    return sorted(paises)

# Endpoint para calcular proporción de renovables
@app.post("/calcular-renovable", response_model=CalculoOutput)
def calcular_renovable(datos: CalculoInput):
    df = data.get("renovables_porcentaje")
    if df is None:
        raise HTTPException(status_code=500, detail="Datos de renovables no disponibles")

    if not {"Entity", "Year", "Renewables (% electricity)"}.issubset(df.columns):
        raise HTTPException(status_code=500, detail="Faltan columnas necesarias en el CSV")

    df_filtrado = df[(df["Entity"] == datos.pais) & (df["Year"] == datos.anio)]

    if df_filtrado.empty:
        raise HTTPException(status_code=404, detail="No se encontraron datos para ese país y año")

    porcentaje = df_filtrado["Renewables (% electricity)"].values[0]
    if pd.isna(porcentaje):
        raise HTTPException(status_code=404, detail="Porcentaje de renovables no disponible")

    proporcion = porcentaje / 100
    consumo_renovable = proporcion * datos.consumo_kwh

    return CalculoOutput(
        proporcion_renovable=proporcion,
        consumo_renovable_estimado=consumo_renovable,
        porcentaje_estimado=porcentaje
    )


@app.get("/generar-graficos")
def generar_graficos():
    try:
        output_path = os.path.join(os.getcwd(), "graphics")
        os.makedirs(output_path, exist_ok=True)

        archivos = {
            'grafico_torta_renovables.gif': generar_grafico_torta_renovables,
            'grafico_barras_renovables.gif': generar_grafico_barras_fuentes,
            'grafico_lineas_capacidad.gif': generar_grafico_lineas_capacidad,
            'grafico_area_renovables.gif': generar_grafico_area_comparativo,
        }

        for nombre_archivo, funcion in archivos.items():
            ruta = os.path.join(output_path, nombre_archivo)
            if not os.path.exists(ruta):
                funcion(output_path)

        return {"message": "Gráficos disponibles o generados correctamente."}

    except Exception as e:
        
        raise HTTPException(status_code=500, detail=str(e))