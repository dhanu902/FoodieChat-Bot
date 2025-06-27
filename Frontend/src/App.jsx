import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Layout from './Components/Layout';
import Home from './Pages/Home';
import ChatPage from './Pages/ChatPage';

import './App.css'

const App = () => {
  return (
    <Router>
          <Routes>
            <Route element={<Layout />}>
              <Route path="/" element={<Home />} />
              <Route path="/chat" element={<ChatPage />} />
              {/* add more routes */}  
            </Route>
          </Routes>
    </Router>
  );
};

export default App;