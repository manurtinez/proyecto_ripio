import React from 'react';
// eslint-disable-next-line no-unused-vars
import {AppBar, Box, Button, Container, Menu, MenuItem, Toolbar, Typography} from "@mui/material";
import {Link} from "react-router-dom";

// eslint-disable-next-line react/prop-types
const Header = ({pages}) => {
    return (
        <AppBar position="static">
            <Container maxWidth="xl">
                <Toolbar disableGutters>
                    {/* eslint-disable-next-line react/prop-types */}
                    {pages.map((page, i) => (
                        <Box key={i} mr={3}>

                            <Button to={page.path} component={Link} color={'warning'} variant={'outlined'}
                                    key={i}>{page.name}</Button>
                        </Box>
                    ))}
                </Toolbar>
            </Container>
        </AppBar>
    )
}

export default Header