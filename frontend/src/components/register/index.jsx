import React from "react";
import passed from "../../media/passed-exam.png";
import diht from "../../media/diht.png";
import board from "../../media/checkers-table.png";
import "./styles.css";
import axios from 'axios';

import {host, port, way} from "../../constants";
import {connect} from "react-redux";

const http = axios.create({
    baseURL: `http://${host}:${port}/${way}`,
    // withCredentials: true,
    // validateStatus : status => true,
});


let register = (username, password) => {
    return http.post('register', {username: username, password: password})
        .then(({data}) => {
            try {
                if (data.status.toString() === 'REGISTERED AND LOGGED IN') {
                    return {is_logged_in : true, username : data.username, session_id : data.session_id};
                }
            } catch (e) {
                return {is_logged_in : false, username : null, session_id : null};
            }
        })
};

export class Register extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
        this.Submit = this.Submit.bind(this);
        this.SetUsername = this.SetUsername.bind(this);
        this.SetPassword = this.SetPassword.bind(this);
    };

    Submit = (e) => {

        register(this.state.username, this.state.password)
            .then(({is_logged_in, username, session_id}) => {
                if (is_logged_in) {
                    this.props.OnLogin(username, session_id);
                }
                else {
                    this.props.Logout();
                }
            });
    };
    SetPassword = (e) => {
        this.setState({password: e.target.value});
    };
    SetUsername = (e) => {
        this.setState({username: e.target.value});
    };

    render() {
        return (

            <>
                <div className="login-part">
                    Register <br/>
                    <form title={"login"} onDragEnter={this.Submit}>
                        Username <br/>
                        <input title={"username"} type={"login"} placeholder={"Enter username"}
                               onChange={this.SetUsername}/> <br/>
                        Password <br/>
                        <input title={"password"} type="password" placeholder={"Password"} onChange={this.SetPassword}/>
                        <br/>
                        <input title={"submit"} type={"button"} value={"register"} onSubmit={this.Submit}
                               onDrag={this.Submit} onClick={this.Submit}/>
                    </form>
                </div>
            </>
        )
    }
}