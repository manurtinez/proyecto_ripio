import React, {createContext} from 'react';
import './App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Login from "./Pages/Login";
import Layout from "./Pages/Layout";
import Home from "./Pages/Home";

export const UserContext = createContext();

function App() {
    return (
        <UserContext.Provider value={'hola'}>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Layout/>}>
                        <Route index path="/home" element={<Home />} />
                        <Route path="/login" element={<Login/>}/>
                    </Route>
                </Routes>
            </BrowserRouter>
        </UserContext.Provider>
    );
}

export default App;
