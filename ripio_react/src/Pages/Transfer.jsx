import React, {useEffect, useState} from 'react';
import {FormContainer, TextFieldElement, SelectElement} from "react-hook-form-mui";
import {Box, Button, Stack, Typography} from "@mui/material";
import Api from "../Api";
import {useNavigate} from "react-router-dom";

const Transfer = () => {
    const navigate = useNavigate();

    const [userList, setUserList] = useState([]);
    const [monedasList, setMonedasList] = useState([]);

    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        async function fetchData() {
            const usersResponse = await Api.fetch('/users/')
            const monedasResponse = await Api.fetch('/monedas/')
            const users = await usersResponse.json();
            const monedas = await monedasResponse.json();
            setUserList(users.map(user => ({id: user.id, label: user.username})))
            setMonedasList(monedas.map(monedas => ({id: monedas.id, label: monedas.nombre})))
            setLoaded(true)
        }

        fetchData();
    }, [])

    const handleSubmit = (data) => {
        const isValid = data.cantidad > 0
        if (!isValid) {
            alert("La cantidad debe ser mayor a 0")
            return
        } else {
            Api.fetch('/users/transfer_to_user/', {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(async (response) => {
                if (response) {
                    alert("Transferencia realizada con exito")
                    navigate('/')
                }
            })
        }
    }

    if (!loaded) return <div>Cargando...</div>

    return (
        <Box p={10}>
            <FormContainer
                className="login-form"
                defaultValues={{usuario_destino: '', moneda: '', cantidad: 0}}
                onSuccess={(data) => handleSubmit(data)}
            >
                <Stack spacing={2} direction={'column'}>
                    <Typography variant={'h4'}>Transferir</Typography>
                    <SelectElement options={userList}
                                   style={{backgroundColor: "white"}} name="usuario_destino" label="Transferir a"
                                   required/>
                    <SelectElement options={monedasList} style={{backgroundColor: "white"}} name="moneda" label="Moneda"
                                   required/>
                    <TextFieldElement style={{backgroundColor: "white"}} name="cantidad" label="Cantidad" required/>
                    <Button variant={"contained"} type="submit">Aceptar</Button>
                </Stack>
            </FormContainer>
        </Box>
    );
}

export default Transfer;