import React, { useState, useEffect } from "react";
import { connect } from "react-redux";
import * as actions from "../actions/product";

const Products = (props) => {
  //const [x,setX] = useState(0)
  //setX(5)

  useEffect(() => {
    props.fetchAllProducts();
  }, []); //componentDidMount equivalent with hooks

  return <div>from Products</div>;
};

const mapStateToProps = (state) => {
  return {
    productList: state.product.list,
  };
};

const mapActionToProps = {
  fetchAllProducts: actions.fetchAll,
};

//connect is a function that returns another function,
//we pass Products in as param
export default connect(mapStateToProps, mapActionToProps)(Products);
