/*
 About.js

 This file defines the About component for the TrueVision application. 
 It provides information about the tool, including its purpose, development context, 
 and the developer behind it.
  
 */



import React from "react";

function About() {
  return (
    <section className="intro">
      <div className="content-wrapper">
        <div className="intro-text">
          <h1>About True<span style={{ color: "#00f0ff" }}>Vision</span></h1>
          <p>
            TrueVision is an advanced tool for detecting deepfakes. It was developed for OlympAI Hackathon.
          </p>
          <p>
            Developer: <span style={{ color: "#00f0ff" }}>Kaveesh Krishna Pandey</span>
          </p>
        </div>

        <div className="intro-image">
          <img
            src={`${process.env.PUBLIC_URL}/TrueVision Logo.png`}
            alt="About Logo"
          />
        </div>
      </div>
    </section>
  );
}

export default About;
