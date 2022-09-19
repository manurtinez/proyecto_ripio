import React, {useEffect} from 'react';
import {Table as TableMUI, TableBody, TableCell, TableHead, TableRow} from '@mui/material';
import Row from "./Row";
import Api from "../Api";

const Table = () => {
    const [rows, setRows] = React.useState([]);

    useEffect(() => {
        Api.fetch('/balances').then(async response => {
            const data = await response.json();
            setRows(data.map((row) => ({
                nombre: row.usuario.username,
                email: row.usuario.email,
                moneda: row.moneda.nombre,
                codigo: row.moneda.codigo,
                cantidad: row.cantidad
            })))
        })
    }, [])

    return <TableMUI sx={{minWidth: 650}} aria-label="simple table">
        <TableHead>
            <TableRow>
                <TableCell>Usuario</TableCell>
                <TableCell align="right">Email</TableCell>
                <TableCell align="right">Moneda</TableCell>
                <TableCell align="right">Codigo</TableCell>
                <TableCell align="right">Cantidad</TableCell>
            </TableRow>
        </TableHead>
        <TableBody>
            {rows.map((row, i) => (
                <Row key={i} row={row}/>
            ))}
        </TableBody>
    </TableMUI>
}

export default Table;