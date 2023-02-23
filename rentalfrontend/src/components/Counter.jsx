import React from "react";
import { CartContext } from "../context/cartContext";

function Counter() {
  const items = CartContext.items;
  /* console.log(items); */
  return (
    <div className="flex flex-col justify-center items-center">
      <div className="counter flex items-center text-2xl justify-start">
        Quantity
        <div className="ml-5 shadow-md flex">
          <div className="bg-[#8a4af3] text-white w-8 flex items-center justify-center rounded-l-lg cursor-pointer">
            -
          </div>
          <div className="w-8 flex items-center justify-center border-[1px] border-[#8a4af3]">

          </div>
          <div className="bg-[#8a4af3] text-white w-8 flex items-center justify-center rounded-r-lg cursor-pointer">
            +
          </div>
        </div>
      </div>
      <div className="counter flex items-center text-2xl justify-start mt-2">
        Months
        <div className="ml-5 shadow-md flex">
          <div className="bg-[#8a4af3] text-white w-8 flex items-center justify-center rounded-l-lg cursor-pointer">
            -
          </div>
          <div className="w-8 flex items-center justify-center border-[1px] border-[#8a4af3]">
            1
          </div>
          <div className="bg-[#8a4af3] text-white w-8 flex items-center justify-center rounded-r-lg cursor-pointer">
            +
          </div>
        </div>
      </div>
    </div>
  );
}

export default Counter;
