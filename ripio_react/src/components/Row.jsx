import React from 'react';
import {
    TableRow,
    TableCell,
} from "@mui/material";


const Row = ({row}) => {
    return (
        <>
            <TableRow>
                <TableCell component="th" scope="row">
                    {row.nombre}
                </TableCell>
                <TableCell align="right">{row.email}</TableCell>
                <TableCell align="right">{row.moneda}</TableCell>
                <TableCell align="right">{row.codigo}</TableCell>
                <TableCell align="right">{row.cantidad}</TableCell>
            </TableRow>
        </>
    )
}

export default Row;