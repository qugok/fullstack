const constants = {
    GAME : {
        SET_STATUS : 'SET_STATUS',
        NO_GAME: 'NO_GAME',
        CREATING: 'CREATING',
        FINDING_OPPONENT: 'FINDING_OPPONENT',
        OPPONENT_IS_FOUNT: 'OPPONENT_IS_FOUNT',
        OPPONENTS_TURN: 'OPPONENTS_TURN',
        CLIENT_TURN: 'CLIENT_TURN',
        ENDED: 'ENDED',
    },
    SET_PLAYER_NUMBER: 'SET_PLAYER_NUMBER',
    LOGIN : {
        SET_LOGGED_IN : 'SET_LOGGED_IN',
        SET_LOGGED_OUT : 'SET_LOGGED_OUT',
    },
    TABLE : {
        SET_TABLE : 'SET_TABLE',
        CHANGE_TABLE : 'CHANGE_TABLE',
    }
};

export const host = 'localhost';
export const port = '25001';
export const way = 'my_api';

export default constants;