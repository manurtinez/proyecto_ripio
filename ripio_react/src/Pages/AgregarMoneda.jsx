import React from 'react';
import {FormContainer, TextFieldElement} from "react-hook-form-mui";
import {Box, Button, Stack, Typography} from "@mui/material";
import Api from "../Api";
import {useNavigate} from "react-router-dom";

const AgregarMoneda = () => {
    const navigate = useNavigate()

    const handleSubmit = (data) => {
        Api.fetch('/monedas/', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(async (response) => {
            if (response) {
                alert("Moneda agregada con exito")
                navigate('/')
            }
        })
    }

    return (

        <Box p={10} style={{maxWidth: '50%'}}>
            <FormContainer
                className="login-form"
                defaultValues={{usuario_destino: '', moneda: '', cantidad: 0}}
                onSuccess={(data) => handleSubmit(data)}
            >
                <Stack spacing={2} direction={'column'}>
                    <Typography variant={'h4'}>Agregar Moneda</Typography>
                    <TextFieldElement style={{backgroundColor: "white"}} name="nombre" label="Nombre" required/>
                    <TextFieldElement style={{backgroundColor: "white"}} name="codigo" label="Codigo" required/>
                    <Button variant={"contained"} type="submit">Aceptar</Button>
                </Stack>
            </FormContainer>
        </Box>
    )
}

export default AgregarMoneda