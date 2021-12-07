import { ACTION_TYPES } from "../actions/product";

const initialState = {
  list: [],
};

export const product = (state = initialState, action) => {
  switch (action.type) {
    case ACTION_TYPES.FETCH_ALL:
      return {
        ...state,
        list: [...action.payload],
      };

    default:
      return state;
  }
};
