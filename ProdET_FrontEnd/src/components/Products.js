import {
  Grid,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@material-ui/core";
import React, { useState, useEffect } from "react";
import { connect } from "react-redux";
import * as actions from "../actions/product";

const Products = (props) => {
  //const [x,setX] = useState(0)
  //setX(5)

  useEffect(() => {
    props.fetchAllProducts();
  }, [props]); //componentDidMount equivalent with hooks

  //product grid
  return (
    <Paper>
      <Grid container>
        <Grid item>
          <TableContainer>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>Product Name</TableCell>
                  <TableCell>Price</TableCell>
                  <TableCell>Emission Score</TableCell>
                  <TableCell>EM Score/Price Ratio</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {props.productList.map((record, index) => {
                  return (
                    <TableRow key={index}>
                      <TableCell>{record.ItemName}</TableCell>
                      <TableCell>{record.Price}</TableCell>
                      <TableCell>{record.BrandName}</TableCell>
                      <TableCell>{record.Retailer}</TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          </TableContainer>
        </Grid>
      </Grid>
    </Paper>
  );
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
