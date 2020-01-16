import React from "react";
import "./styles.css";
import axios from 'axios';

import {host, port, way} from "../../constants";

const http = axios.create({
    baseURL: `http://${host}:${port}/${way}`,
    // withCredentials: true,
    // validateStatus : status => true,
});


let login = (username, password) => {
    return http.post('login', {username: username, password : password})
        .then(({data}) =>{
            try {
                console.log(data);
                if (data.status.toString() === 'LOGGED IN'){
                    return {is_logged_in : true, username : data.username.toString(), session_id : data.session_id.toString()};
                }
            }
            catch (e) {
                return {is_logged_in : false, username : null, session_id : null};
            }
})
};

export class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {login : "Login"};
        this.Submit = this.Submit.bind(this);
        this.SetUsername = this.SetUsername.bind(this);
        this.SetPassword = this.SetPassword.bind(this);
    };

    Submit = (e) => {

        login(this.state.username, this.state.password)
            .then(({is_logged_in, username, session_id}) => {
                if (is_logged_in) {
                    console.log(username, session_id);
                    this.props.OnLogin(username, session_id);
                }
                else {
                    this.props.Logout();
                }
            });
    };
    SetPassword = (e) => {
        this.setState({password : e.target.value});
    };
    SetUsername = (e) => {
        this.setState({username : e.target.value});
    };


    render() {
        return (

            <>
                <div className="login-part">
                    Login <br/>
                    <form title={"login"}>
                        Username <br/>
                        <input title={"username"} type={"login"} placeholder={"Enter username"} onChange={this.SetUsername}/> <br/>
                        Password <br/>
                        <input title={"password"} type="password" placeholder={"Password"} onChange={this.SetPassword} onDragEnter={this.Submit}/> <br/>
                        <input title={"submit"} type={"button"} value={"submit"} onClick={this.Submit}/>
                    </form>
                </div>
            </>
        )
    }
}