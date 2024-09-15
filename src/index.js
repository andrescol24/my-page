import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import HomePage from './page/HomePage';
import MinecraftPage from './page/MinecraftPage';
import Header from './component/Header';
import Footer from './component/Footer';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';

const root = ReactDOM.createRoot(document.getElementById('root'));
const router = createBrowserRouter([
  {
    path: '/',
    element: <HomePage/>
  },
  {
    path: 'minecraft',
    element: <MinecraftPage/>
  }
]);
root.render(
  <React.StrictMode>
    <Header/>
    <RouterProvider router={router}/>
    <Footer/>
  </React.StrictMode>
);