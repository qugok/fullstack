import C, {host, port, way} from '../constants';
import axios from "axios";

const http = axios.create({
    baseURL: `http://${host}:${port}/${way}`,
    // withCredentials: true,
    // validateStatus : status => true,
});


export const setLoggedIn = (username, session_id) => {
    return ({
        type: C.LOGIN.SET_LOGGED_IN,
        payload: {username: username, session_id: session_id},
    });
};


export const setLogout = () =>
    ({
        type: C.LOGIN.SET_LOGGED_OUT,
    });

export const GameStatus = (status) =>
    ({
        type: C.GAME.SET_STATUS,
        status: status,
    });
export const PlayerNumber = (number) =>
    ({
        type: C.SET_PLAYER_NUMBER,
        number: number
    });
export const SetTable = (table) =>
    ({
        type: C.TABLE.SET_TABLE,
        table: table
    });

export const CreateGame = (dispatch, username, session_id) => {
    dispatch(GameStatus(C.GAME.CREATING));
    http.post('create_game', {username: username, session_id : session_id})
        .then(({data}) =>{
            if (data.status.toString() === "CREATED"){
                dispatch(GameStatus(C.GAME.OPPONENTS_TURN));
                dispatch(PlayerNumber(2));
            }
            else if (data.status.toString() === "PENDING"){
                dispatch(GameStatus(C.GAME.FINDING_OPPONENT));
                dispatch(PlayerNumber(1));
            }})
        .catch(() => {
            dispatch(GameStatus(C.GAME.NO_GAME));
        });
};

export const CheckLogIn = (dispatch, username, session_id) => {
    http.post('is_logged_in', {username: username, session_id: session_id})
        .then(({data}) => {
            console.log(data);
            if (data.status.toString() === "OK") {
                dispatch(setLoggedIn(username, session_id));
            }
            else{
                dispatch(setLogout())
            }
        });
};

export const GetAllTable = (dispatch, username, session_id, player_number) => {
    http.post('get_all_table', {session_id : session_id, username : username, player_number : player_number}).then(({data}) =>{
        if (data.status.toString() === 'OK') {
            dispatch(SetTable(data.table))
        }
    })
};


export const MakeMove = (dispatch, username, session_id, player_number, fro, to) => {
    http.post('make_turn', {
        username: username,
        session_id: session_id,
        player_number: player_number,
        fro : fro,
        to : to
    }).then(({data}) => {
        if (data.status.toString() === 'OK'){
            dispatch(GameStatus(C.GAME.OPPONENTS_TURN));
            GetAllTable(dispatch, username, session_id, player_number);
        }
    });
};
