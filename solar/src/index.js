import React from "react";
import { createRoot } from "react-dom/client";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../client/src/css/opManager.css'
import App from "./App";

const root = createRoot(document.getElementById("app"));
root.render(<App />);