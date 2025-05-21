import React from 'react';
import { Container, Card, Row, Col } from 'react-bootstrap';

const InfoEnergia = () => {
  return (
    <Container className="my-5">
      <h1 className="text-center mb-4 text-success">Energías Renovables</h1>

      {/* ENERGÍA SOLAR */}
      <h2 className="text-center mb-4">Energía Solar</h2>
      <Row>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Img variant="top" src="img/energia-solar.jpg" />
            <Card.Body>
              <Card.Title>¿Qué es?</Card.Title>
              <Card.Text>
                La energía solar se obtiene del sol. Se aprovecha con paneles fotovoltaicos o térmicos para generar electricidad o calor. Es una fuente limpia, inagotable y abundante.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Body>
              <Card.Title>Ventajas</Card.Title>
              <ul>
                <li>Reduce la dependencia de combustibles fósiles.</li>
                <li>No emite gases contaminantes.</li>
                <li>Disponible en casi todo el planeta.</li>
                <li>Instalación modular y escalable.</li>
              </ul>
              <Card.Title>Aplicaciones</Card.Title>
              <ul>
                <li>Electricidad para hogares y empresas.</li>
                <li>Calentamiento de agua mediante termosifones.</li>
                <li>Electrificación en zonas rurales aisladas.</li>
              </ul>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* ENERGÍA EÓLICA */}
      <h2 className="text-center mb-4">Energía Eólica</h2>
      <Row>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Body>
              <Card.Title>Ventajas</Card.Title>
              <ul>
                <li>No produce emisiones contaminantes.</li>
                <li>Requiere poco mantenimiento.</li>
                <li>Compatible con actividades como la agricultura.</li>
                <li>Crecimiento acelerado en todo el mundo.</li>
              </ul>
              <Card.Title>Aplicaciones</Card.Title>
              <ul>
                <li>Parques eólicos terrestres y marinos.</li>
                <li>Generación eléctrica a gran escala.</li>
                <li>Sistemas autónomos para zonas rurales.</li>
              </ul>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Img variant="top" src="img/energia-eolica.jpg" />
            <Card.Body>
              <Card.Title>¿Qué es?</Card.Title>
              <Card.Text>
                La energía eólica se obtiene del viento, utilizando aerogeneradores que convierten la energía cinética del aire en electricidad. Es limpia y sostenible.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* ENERGÍA HIDROELÉCTRICA */}
      <h2 className="text-center mb-4">Energía Hidroeléctrica</h2>
      <Row>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Img variant="top" src="img/energia-hidroelectrica.jpg" />
            <Card.Body>
              <Card.Title>¿Qué es?</Card.Title>
              <Card.Text>
                La energía hidroeléctrica se genera a partir del movimiento del agua, usualmente con represas y turbinas. Es renovable y con alta capacidad de producción.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Body>
              <Card.Title>Ventajas</Card.Title>
              <ul>
                <li>Alta eficiencia energética.</li>
                <li>No produce emisiones directas.</li>
                <li>Provee estabilidad a la red eléctrica.</li>
                <li>Permite almacenamiento mediante embalses.</li>
              </ul>
              <Card.Title>Aplicaciones</Card.Title>
              <ul>
                <li>Centrales hidroeléctricas grandes y pequeñas.</li>
                <li>Control de inundaciones.</li>
                <li>Regulación del caudal de ríos.</li>
              </ul>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* ENERGÍA GEOTÉRMICA */}
      <h2 className="text-center mb-4">Energía Geotérmica</h2>
      <Row>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Body>
              <Card.Title>Ventajas</Card.Title>
              <ul>
                <li>Fuente constante y predecible.</li>
                <li>Bajas emisiones de gases contaminantes.</li>
                <li>Requiere poco espacio.</li>
                <li>Puede funcionar todo el año.</li>
              </ul>
              <Card.Title>Aplicaciones</Card.Title>
              <ul>
                <li>Generación eléctrica en zonas volcánicas.</li>
                <li>Calefacción de viviendas y edificios.</li>
                <li>Uso en procesos industriales.</li>
              </ul>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Img variant="top" src="img/energia-geotermica.jpg" />
            <Card.Body>
              <Card.Title>¿Qué es?</Card.Title>
              <Card.Text>
                La energía geotérmica se obtiene del calor almacenado en el interior de la Tierra. Se aprovecha mediante pozos geotérmicos para generar electricidad o calefacción.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* BIOCOMBUSTIBLES */}
      <h2 className="text-center mb-4">Biocombustibles</h2>
      <Row>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Img variant="top" src="img/biocombustibles.jpg" />
            <Card.Body>
              <Card.Title>¿Qué es?</Card.Title>
              <Card.Text>
                Los biocombustibles son combustibles líquidos o gaseosos obtenidos a partir de biomasa vegetal o animal. Son una alternativa renovable para el transporte y la generación de energía.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="mb-4 shadow">
            <Card.Body>
              <Card.Title>Ventajas</Card.Title>
              <ul>
                <li>Producidos a partir de materia orgánica renovable.</li>
                <li>Menor impacto ambiental que los combustibles fósiles.</li>
                <li>Compatibles con infraestructuras existentes.</li>
                <li>Generan empleo rural.</li>
              </ul>
              <Card.Title>Aplicaciones</Card.Title>
              <ul>
                <li>Combustibles para automóviles (biodiésel, bioetanol).</li>
                <li>Generación de electricidad y calor.</li>
                <li>Sustitución parcial de combustibles fósiles en industrias.</li>
              </ul>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default InfoEnergia;
