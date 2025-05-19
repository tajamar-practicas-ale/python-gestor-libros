import React, { useState } from 'react';
import { login } from '../services/api';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('usuario');
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        login({ username, password, role })
            .then(data => {
                localStorage.setItem('token', data.token);
                navigate('/libros');
            })
            .catch(() => alert("Credenciales incorrectas"));
    };

    return (
        <div>
            <h2>Iniciar sesión</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Usuario:
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                </label>
                <label>
                    Contraseña:
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </label>
                <label>
                    Rol:
                    <select value={role} onChange={(e) => setRole(e.target.value)}>
                        <option value="usuario">Usuario</option>
                        <option value="moderador">Moderador</option>
                        <option value="admin">Admin</option>
                    </select>
                </label>
                <button type="submit">Iniciar sesión</button>
            </form>
        </div>
    );
};

export default Login;