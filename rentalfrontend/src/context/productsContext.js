import React, { createContext, useState } from "react";
import { ApiTopPropduct } from "../Api/TopProductsApi";
export const productsContext = createContext();
export const ProductProvider = ({ children }) => {
  /*  console.log(ApiTopPropduct); */
  const [products, setProducts] = useState([
    ApiTopPropduct.map((product) => product),
  ]);
  /*  console.log(products); */
  return (
    <productsContext.Provider value={[products, setProducts]}>
      {children}
    </productsContext.Provider>
  );
};