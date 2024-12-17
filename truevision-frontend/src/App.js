/*
App.js

This is the main frontend component of the TrueVision application. It defines the structure of the app, including routing to different pages (Home, About, Contact) and the navigation menu. It serves as the entry point for rendering the React components and provides a consistent layout and styling for the entire application.
*/


// Necessary Imports
import React from "react"; // Import React library
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"; // Import routing components
import Home from "./Home"; // Import Home component
import About from "./About"; // Import About component
import Contact from "./Contact"; // Import Contact component
import "./App.css"; // Import CSS for styling the app

// Main App component
function App() {
  return (
    <Router> {/* Wrap the application in a Router component to enable routing */}
      <div className="app"> {/* Main container for the app */}
        <div className="background"></div> {/* Background element for styling */}

        {/* Header section with logo and navigation */}
        <header>
          <div className="logo" style={{ fontSize: "28px" }}>
            True<span style={{ fontSize: "28px" }}>Vision</span> {/* Logo with dynamic font size */}
          </div>
          <nav>
            <ul style={{ fontSize: "18px" }}> {/* Navigation menu */}
              <li><Link to="/">Home</Link></li>
              <li><Link to="/about">About</Link></li>
              <li><Link to="/contact">Contact</Link></li>
            </ul>
          </nav>
        </header>

        {/* Main content area */}
        <main style={{ fontSize: "20px", padding: "20px" }}>
          <Routes> {/* Define application routes */}
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App; // Export the App component
