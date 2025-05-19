import React, { useState } from 'react';
import { crearLibro } from '../services/api';
import { useNavigate } from 'react-router-dom';

const FormularioLibro = () => {
    const [titulo, setTitulo] = useState('');
    const [autor, setAutor] = useState('');
    const [precio, setPrecio] = useState('');
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (precio < 0) {
            alert("El precio debe ser mayor o igual a 0");
            return;
        }

        crearLibro({ titulo, autor, precio })
            .then(() => {
                alert("Libro creado correctamente");
                navigate('/libros');
            })
            .catch(() => alert("Error al crear libro"));
    };

    return (
        <div>
            <h2>Nuevo Libro</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Título:
                    <input type="text" value={titulo} onChange={(e) => setTitulo(e.target.value)} />
                </label>
                <label>
                    Autor:
                    <input type="text" value={autor} onChange={(e) => setAutor(e.target.value)} />
                </label>
                <label>
                    Precio:
                    <input type="number" value={precio} onChange={(e) => setPrecio(e.target.value)} />
                </label>
                <button type="submit">Crear Libro</button>
            </form>
        </div>
    );
};

export default FormularioLibro;