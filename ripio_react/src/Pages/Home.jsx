import React, {useEffect, useState} from 'react';
import Api from "../Api";
import {useNavigate} from "react-router-dom";
import Table from "../components/Table";

const Home = () => {
    const navigate = useNavigate();
    const [loaded, setLoaded] = useState(false)

    useEffect(() => {
        Api.fetch('/api/token/validate/').then((response) => {
            if (!response) {
                navigate('/login');
            } else {
                setLoaded(true)
            }
        })
    }, [])

    return (
        <div>
            {loaded ? <Table /> : <h1>Cargando...</h1>}
        </div>
    )
}

export default Home;