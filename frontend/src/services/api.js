const BASE = 'http://localhost:5000/api';

export const getLibros = () => {
    return fetch(`${BASE}/libros/`)
        .then(r => r.json())
        .catch(error => console.error("Error al obtener libros:", error));
};

export const crearLibro = (data) => {
    return fetch(`${BASE}/libros/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(r => r.json())
        .catch(error => console.error("Error al crear libro:", error));
};

export const actualizarLibro = (id, data) => {
    return fetch(`${BASE}/libros/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(r => r.json())
        .catch(error => console.error("Error al actualizar libro:", error));
};

export const eliminarLibro = (id) => {
    return fetch(`${BASE}/libros/${id}`, {
        method: 'DELETE',
    }).then(r => r.json())
        .catch(error => console.error("Error al eliminar libro:", error));
};

// export const login = (creds) => {
//     return fetch(`${BASE}/login`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(creds)
//     }).then(r => r.json())
//         .catch(error => console.error("Error al iniciar sesión:", error));
// };

export const login = (creds) => {
    return fetch(`${BASE}/login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(creds)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Credenciales incorrectas');
            }
            return response.json();
        })
        .then(data => {
            console.log("Login exitoso", data); // Para ver el contenido de la respuesta
            return data;
        })
        .catch(error => {
            console.error("Error al iniciar sesión:", error);
            throw error; // Esto se captura en el componente Login  
        });
};
