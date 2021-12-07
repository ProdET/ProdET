import React from "react";
import "./App.css";
import { store } from "./actions/store";
import { Provider } from "react-redux";
import Products from "./components/Products";

function App() {
  return (
    <Provider store={store}>
      <Products />
    </Provider>
  );
}

export default App;
