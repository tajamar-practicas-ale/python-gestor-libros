import React from 'react';
import { BrowserRouter, Routes, Route, useNavigate } from 'react-router-dom';
import Login from './components/Login';
import ListarLibros from './components/ListarLibros';
import FormularioLibro from './components/FormularioLibro';

const ProtectedRoute = ({ element }) => {
  const token = localStorage.getItem('token');
  const navigate = useNavigate();
  if (!token) {
    navigate('/login');
    return null;
  }
  return element;
};

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/libros" element={<ProtectedRoute element={<ListarLibros />} />} />
        <Route path="/nuevo" element={<ProtectedRoute element={<FormularioLibro />} />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;