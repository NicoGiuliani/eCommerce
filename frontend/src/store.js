import { combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";
import { productListReducer } from "./reducers/productReducers";
import { configureStore } from "@reduxjs/toolkit";

const reducer = combineReducers({
  productList: productListReducer,
});

const initialState = {};

const middleware = [thunk];

const store = configureStore({
  reducer: reducer,
  middleware: middleware,
  preloadedState: initialState,
});

export default store;
