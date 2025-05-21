import './App.css';
import InfoEnergia from './components/InfoEnergia';
import Estimador from './components/EstimadorRenovable';
import Graficos from './components/Graficos';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<InfoEnergia />} />
        <Route path="/estimador" element={<Estimador />} />
        <Route path="/graficos" element={<Graficos />} />
      </Routes>
    </Router>
  );
}

export default App;

