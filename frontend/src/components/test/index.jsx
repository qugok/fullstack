import React from "react";
import passed from "../../media/passed-exam.png";
import diht from "../../media/diht.png";
import board from  "../../media/checkers-table.png";
import "./styles.css";
import axios from 'axios';

import {host, port, way} from "../../constants";
import {CheckLogIn, CreateGame, GetAllTable} from "../../actions/register";
import {connect} from "react-redux";
import {GamePageCheckersClass} from "../game";

const http = axios.create({
    baseURL: `http://${host}:${port}/${way}`,
    // withCredentials: true,
});



let test = () => {
    return http.post('get_all_table', {session_id : localStorage.getItem('session_id'), username : localStorage.getItem('username'), player_number : localStorage.getItem('player_number')})
        .then(({data}) =>{
            localStorage.setItem("table", JSON.stringify(data));
})
        .catch((e) => {
            localStorage.setItem("status", "error: " + e.toString())
        }).finally(() => {
        localStorage.setItem("finally", "request is done")
    });
};

export class TestClass extends React.Component {
    constructor(props) {
        super(props);
    };


    render() {
        const store = this.props.store;
        return (
            <>
                <div className="login-part">
                    <div className={"login-text"}>
                        {JSON.stringify(store)} <br/>
                    </div>
                </div>
            </>
        )
    }
}

const mapStateToProps = store => {
    console.log(store); // посмотрим, что же у нас в store?
    return {
        // is_logged_in: store.is_logged_in,
        store: store,
    }
};


const mapDispatchToProps = dispatch => {
    return {

    }
};

export const Test = connect(mapStateToProps, mapDispatchToProps)(TestClass);
