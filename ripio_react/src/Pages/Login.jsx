import React from 'react';
import LoginForm from "../components/LoginForm";
import {useNavigate} from "react-router-dom";
import Api from "../Api";

const Login = () => {
    const navigate = useNavigate();

    const handleSuccess = (data) => {
        Api.fetch('/api/token/', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(async (response) => {
            try {
                const data = await response.json();
                localStorage.setItem('token', data.access);
                localStorage.setItem('refresh', data.refresh);
                navigate('/');
            } catch (e) {
                alert("credenciales incorrectas")
            }
        })
    }

    return (
        <LoginForm handleSuccess={handleSuccess}/>
    )
}

export default Login;