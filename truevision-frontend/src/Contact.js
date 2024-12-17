import React from "react";

function Contact() {
  return (
    <section className="intro">
      <div className="content-wrapper">
        <div className="intro-text">
          <h1><p>Contact <span style={{ color: "#00f0ff" }}>Us</span></p></h1>
          <p>Email: <span style={{ color: "#00f0ff" }}>truevision.deepfake@gmail.com</span></p>
          <p>Phone: <span style={{ color: "#00f0ff" }}>+91 942XXXXXXX</span></p>
        </div>

        <div className="intro-image">
          <img
            src={`${process.env.PUBLIC_URL}/TrueVision Logo.png`}
            alt="Contact Logo"
          />
        </div>
      </div>
    </section>
  );
}

export default Contact;
