import {SEARCH} from "../constants/actions.js";
import data from "../utils/data.js";

const PdfReducer = (state = {results: []},action) => {
    switch (action.type) {
    case SEARCH:
        const arr = JSON.parse(action.payload).map(x => [x[0], data.anime.find(y => y[0] == x[1])[1]])
        return {...state, results: arr};
    default:
        return state;
    }
};

export default PdfReducer;
