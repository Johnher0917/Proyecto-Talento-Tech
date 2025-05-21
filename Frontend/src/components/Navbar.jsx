import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => (
    <nav class="navbar sticky-top sticky-top bg-success">
    <form class="container-fluid justify-content-end bg-success">
      <Link className="nav-link" to="/">
      <button class="btn btn-sm btn-outline-light me-2" type="button">Inicio</button></Link>
      <Link className="nav-link" to="/graficos">
      <button class="btn btn-sm btn-outline-light me-2" type="button">Gráficos</button></Link>
      <Link className="nav-link" to="/estimador">
      <button class="btn btn-sm btn-outline-light me-2" type="button">Estimación Renovable</button></Link>
    </form>
    </nav>
);

export default Navbar;