import React from "react";
import "./styles.css";
import axios from 'axios';

import {host, port, way} from "../../constants";

const http = axios.create({
    baseURL: `http://${host}:${port}/${way}`,
    // withCredentials: true,
    // validateStatus : status => true,
});


let logout = (username) => {
    return http.post('logout', {username: username})
};

export class Logout extends React.Component {
    constructor(props) {
        super(props);
        this.Submit = this.Submit.bind(this);
    };

    Submit = (e) => {
        logout(this.props.username).then(this.props.Logout).catch(this.props.Logout);
    };

    render() {
        return (
            <>
                <div className="logout-part">
                    Username: {this.props.username} <br/>
                    <form title={"login"} >
                        <input title={"submit"} type={"button"} value={"logout"} onClick={this.Submit}/>
                    </form>
                </div>
            </>
        )
    }
}