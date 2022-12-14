import React from 'react';
import {Outlet} from "react-router-dom";
import Header from "../components/Header";

const Layout = () => {
    const pages = [{
        name: 'Home',
        path: '/'
    }, {
        name: 'Transferir',
        path: '/transfer'
    },
    {
        name: "Agregar Moneda",
        path: '/add-moneda'
    }
]


    return (
        <div className="layout">
            <Header pages={pages}/>
            <Outlet/>
        </div>
    );
}

export default Layout;