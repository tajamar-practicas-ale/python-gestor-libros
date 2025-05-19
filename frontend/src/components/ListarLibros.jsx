import React, { useState, useEffect } from 'react';
import { getLibros, eliminarLibro } from '../services/api';
import { useNavigate } from 'react-router-dom';

const ListarLibros = () => {
    const [libros, setLibros] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        getLibros().then(data => setLibros(data));
    }, []);

    const handleDelete = (id) => {
        eliminarLibro(id).then(() => {
            setLibros(libros.filter(libro => libro.id !== id));
            alert("Libro eliminado correctamente");
        }).catch(() => alert("Error al eliminar libro"));
    };

    return (
        <div>
            <h2>Lista de Libros</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Título</th>
                        <th>Autor</th>
                        <th>Precio</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {libros.map(libro => (
                        <tr key={libro.id}>
                            <td>{libro.id}</td>
                            <td>{libro.titulo}</td>
                            <td>{libro.autor}</td>
                            <td>{libro.precio}</td>
                            <td>
                                <button onClick={() => navigate(`/editar/${libro.id}`)}>Editar</button>
                                <button onClick={() => handleDelete(libro.id)}>Borrar</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ListarLibros;