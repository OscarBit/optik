import React from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      <div
        style={{
          display: "flex",
          marginLeft: "10%",
          marginRight: "10%",
          alignItems: "stretch",
          flexWrap: "wrap",
        }}
      >
        <div
          className="info-panel"
          style={{
            backgroundColor: "red",
            textAlign: "justify",
            flex: "1 1 20%",
            padding: "40px",
          }}
        >
          <h1>Reflectance Calculator</h1>
          <p>
            Calculate reflectance due to thin-film interference by entering your
            films below. Reflectance at wavelengths from 200 nm to 2000 nm may
            be calculated. Up to 20 films may be entered. Our Reflectance
            Calculator uses the same calculation engine that our thin-film
            measurement systems do, which is based on the complex-matrix form of
            the Fresnel equations.
          </p>
        </div>
        <div
          id="plot-panel"
          style={{
            backgroundColor: "green",
            textAlign: "justify",
            flex: "1 1 60%",
            padding: "20px",
            display: "flex",
            flexDirection: "column",
          }}
        >
          <div
            id="plot"
            style={{
              backgroundColor: "black",
              flex: "1",
              padding: "20px",
            }}
          ></div>
          <div
            style={{
              display: "flex",
            }}
          >
            <div
              style={{
                flex: "1 1 auto",
              }}
            >
              <input
                type="radio"
                id="transpitance"
                name="plot-kind"
                value="transmitance"
              />
              <label for="transpitance">Transpitance</label>
            </div>
            <div
              style={{
                flex: "1 1 auto",
              }}
            >
              <input
                type="radio"
                id="reflectance"
                name="plot-kind"
                value="reflectance"
              />
              <label for="reflectance">Reflectance</label>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
