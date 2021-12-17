import React from "react";
import "./App.css";
import { store } from "./actions/store";
import { Provider } from "react-redux";
import Products from "./components/Products";
import { Container } from "@material-ui/core";

function App() {
  return (
    <Provider store={store}>
      <Container>
        <Products />
      </Container>
    </Provider>
  );
}

export default App;
