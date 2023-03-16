import React, { Component } from 'react';
import { render } from "react-dom"
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import HomePage from '../client/src/pages/home';
import SignUp from '../client/src/pages/signUp';
import Login from '../client/src/pages/login';
import SalesRep from '../client/src/pages/salesRep';
// import { Navbar } from 'react-bootstrap';
import Navbar from '../client/src/pages/navbar'
import UserRequestForm from '../client/src/pages/UserRequestForm';
import {ToastContainer, toast} from 'react-toastify'

export default class App extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return(
        <>
        <ToastContainer
            position="top-right"
            autoClose={1500}
            closeOnClick
            />
        <Router>
            <Routes>
                <Route exact path='/' element={<HomePage />}/>
                <Route exact path='/login' element={<Login />}/>
                <Route exact path='/signup' element={<SignUp />}/>
                <Route exact path='/salesrep' element={<SalesRep />}/>
                <Route exact path='/userReq' element={<UserRequestForm />}/>
                {/* <Route exact path='/nav' element={<Navbar />}/> */}
            </Routes>
        </Router>
        </>
        )
    }
}
const appDiv = document.getElementById("app")
render(<App/>, appDiv);