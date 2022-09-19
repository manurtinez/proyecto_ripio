import React from "react";
import {FormContainer, TextFieldElement} from "react-hook-form-mui";
import {Box, Button, Stack, Typography} from "@mui/material";

// eslint-disable-next-line react/prop-types
const LoginForm = ({handleSuccess}) => {
    return (
        <Box p={10}>
            <FormContainer
                className="login-form"
                defaultValues={{name: ''}}
                onSuccess={(data) => handleSuccess(data)}
            >
                <Stack spacing={2} direction={'column'}>
                    <Typography variant={'h4'}>Login</Typography>
                    <TextFieldElement style={{backgroundColor: "white"}} name="username" label="Usuario" required/>
                    <TextFieldElement style={{backgroundColor: "white"}} name="password" label="Contraseña" required/>
                    <Button variant={"contained"} type="submit">Aceptar</Button>
                </Stack>
            </FormContainer>
        </Box>
    )
}

export default LoginForm;