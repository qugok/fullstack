import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom'
import MainRouter from './routes';
import { storeFactory } from './reducers';
import C from './constants';
import axios from 'axios';


// ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();

// httpClient = axios.create({
//     baseURL: `http://${this.client.host}:${this.client.port}/`,
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     timeout: this.client.timeout,
//     transformRequest: [
//         (data) => {
//             return JSON.stringify(data);
//         }
//     ],
//     responseType: 'json',
// });

// const initialState = {
//     registerActive: {
//         active: false
//     },
//     registerStatus: C.REGISTER_STATUS.NOT_YET,
//     registerForm: {
//         teamName: '',
//         people: [
//             {
//                 email: '',
//                 name: '',
//                 phone: '',
//                 univercity: ''
//             },
//             {
//                 email: '',
//                 name: '',
//                 phone: '',
//                 univercity: ''
//             },
//             {
//                 email: '',
//                 name: '',
//                 phone: '',
//                 univercity: ''
//             },
//             {
//                 email: '',
//                 name: '',
//                 phone: '',
//                 univercity: ''
//             }
//         ],
//         skills: [
//             {
//                 skill: 'Machine learning',
//                 status: false
//             },
//             {
//                 skill: 'React',
//                 status: false
//             },
//             {
//                 skill: 'SMM',
//                 status: false
//             }
//         ],
//         anotherSkills: '',
//         advice: ''
//     }
// };

const initialState = {
    username: '',
    is_logged_in: false,
    session_id: '',
    player_number : 0,
    game_status: C.GAME.NO_GAME,
    game_table: {},
};

const store = storeFactory(initialState);


const render = () =>
    ReactDOM.render(
        <Provider store={ store }>
            <BrowserRouter>
                <MainRouter/>
            </BrowserRouter>
        </Provider>,
        document.getElementById('root'));

store.subscribe(render);
render();



// registerServiceWorker();