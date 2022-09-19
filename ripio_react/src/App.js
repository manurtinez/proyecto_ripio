import React from 'react';
import './App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Login from "./Pages/Login";
import Layout from "./Pages/Layout";
import Home from "./Pages/Home";
import Transfer from "./Pages/Transfer";


function App() {
    return (
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Layout/>}>
                        <Route index path="/" element={<Home />} />
                        <Route path="/login" element={<Login/>}/>
                        <Route path="/transfer" element={<Transfer/>}/>
                    </Route>
                </Routes>
            </BrowserRouter>
    );
}

export default App;
