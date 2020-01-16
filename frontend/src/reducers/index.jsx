import { createStore, combineReducers, applyMiddleware } from 'redux';
import C from "../constants";


const logger = store => next => action => {
    let result;
    console.groupCollapsed("dispatching", action.type);
    console.log('prev state', store.getState());
    console.log('action', action);
    result = next(action);
    console.log('next state', store.getState());
    console.groupEnd();
    return result;
};

const saver = store => next => action => {
    let result = next(action);
    localStorage['redux-store'] = JSON.stringify(store.getState());
    return result;
};

function rootReducer(state, action) {
    switch (action.type) {
        case C.LOGIN.SET_LOGGED_IN:
            return { ...state,
                username: action.payload.username,
                is_logged_in: true,
                session_id: action.payload.session_id,
            };
        case C.LOGIN.SET_LOGGED_OUT:
            return { ...state,
                username: '',
                is_logged_in: false,
                session_id: '',
            };
        case C.SET_PLAYER_NUMBER:
            return { ...state,
                player_number : action.number,
            };
        case C.TABLE.SET_TABLE:
            return { ...state,
                game_table: action.table,
            };
        case C.GAME.SET_STATUS:
            return { ...state,
                game_status: action.status,
            };

        default:
            return state
    }
}

export const storeFactory = (initialState = {}) => (
    applyMiddleware(logger, saver) (createStore)(
    // createStore(
        // combineReducers({
            // rootReducer: rootReducer,
            // rootReducer,
            // rootReducer
        // }),
        rootReducer,
        (localStorage['redux-store']) ? JSON.parse(localStorage['redux-store']) : initialState
        // initialState
    )
);