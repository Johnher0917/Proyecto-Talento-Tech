import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Graficos = () => {
  const [graficos, setGraficos] = useState([]);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    const fetchGraficos = async () => {
      try {
        await axios.get('http://localhost:8000/generar-graficos');

        const graficosDisponibles = [
          {
            titulo: 'Producción de Energía Renovable por Fuente',
            url: 'http://localhost:8000/graphics/grafico_barras_renovables.gif',
          },
          {
            titulo: 'Participación de Energías Renovables',
            url: 'http://localhost:8000/graphics/grafico_torta_renovables.gif',
          },
          {
            titulo: 'Tendencia en la Capacidad Instalada',
            url: 'http://localhost:8000/graphics/grafico_lineas_capacidad.gif',
          },
          {
            titulo: 'Comparación entre Consumo de Energía Renovable y Convencional',
            url: 'http://localhost:8000/graphics/grafico_area_renovables.gif',
          },
        ];

        setGraficos(graficosDisponibles);
      } catch (error) {
        console.error("Error obteniendo los gráficos:", error);
      } finally {
        setCargando(false);
      }
    };

    fetchGraficos();
  }, []);

  return (
    <div className="container py-4">
      <h1 className="text-center mb-4 text-success">
        Visualización de Gráficos de Energía Renovable
      </h1>

      {cargando ? (
        <div className="text-center text-secondary fs-5">Cargando gráficos...</div>
      ) : (
        <div id="carouselGraficos" className="carousel slide p-3" data-bs-ride="carousel" style={{ backgroundColor: 'rgba(0, 240, 209, 0.4)', padding: '20px', borderRadius: '12px' }}>
          <div className="carousel-inner">
            {graficos.map((grafico, index) => (
              <div
                key={index}
                className={`carousel-item ${index === 0 ? 'active' : ''}`}
              >
                <div className="card h-100 shadow-sm mx-auto  p-3" style={{ backgroundColor: '#00C0F0', width: '80%', maxWidth: '600px' }}>
                  <img
                    src={grafico.url}
                    className="d-block"
                    alt={grafico.titulo}
                    style={{maxHeight: '400px', objectFit: 'contain' }}
                  />
                  <div className="mt-3 text-center">
                    <h5>{grafico.titulo}</h5>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Controles del carrusel */}
          <button
            className="carousel-control-prev"
            type="button"
            data-bs-target="#carouselGraficos"
            data-bs-slide="prev"
          >
            <span className="carousel-control-prev-icon" aria-hidden="true" style={{ backgroundColor: 'rgba(0, 0, 0, 0.4)', padding: '20px', borderRadius: '12px' }}></span>
            <span className="visually-hidden">Anterior</span>
          </button>
          <button
            className="carousel-control-next"
            type="button"
            data-bs-target="#carouselGraficos"
            data-bs-slide="next"
          >
            <span className="carousel-control-next-icon" aria-hidden="true" style={{ backgroundColor: 'rgba(0, 0, 0, 0.4)', padding: '20px', borderRadius: '12px' }}></span>
            <span className="visually-hidden">Siguiente</span>
          </button>
        </div>
      )}
    </div>
  );
};

export default Graficos;