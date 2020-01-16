import React from "react";
import "./styles.css";
import axios from 'axios';

import {host, port, way} from "../../constants";
import {Register} from "../register";
import {Login} from "../login";
import {connect} from "react-redux";

import {Logout} from "../logout";
import {setLoggedIn, setLogout} from "../../actions/register";

export class HelloPageClass extends React.Component {
    constructor(props) {
        super(props);
        this.state = {register: false};
    };

    render() {
        const {username, is_logged_in, setLoggedInAction, setLogoutAction} = this.props;
        if (is_logged_in) {
            return (<>
                <div className="hello-part">
                    <div className={"hello-text"}>
                        Hello {username}! <br/>
                        You are logged in.
                    </div>
                    <Logout Logout={setLogoutAction} username={username}/>
                </div>
            </>)
        } else if (this.state.register) {
            return (
                <>
                    <div className="hello-part">
                        <Register OnLogin = {setLoggedInAction} Logout={setLogoutAction}/>
                        <form title={"log in"}>
                            <input title={"log in"} type={"button"} value={"log in"}
                                   onClick={() => this.setState({register: false})}/>
                        </form>
                    </div>
                </>)
        } else {
            return (
                <>
                    <div className="hello-part">
                        <Login OnLogin = {setLoggedInAction} Logout={setLogoutAction}/>
                        <form title={"register"}>
                            <input title={"register"} type={"button"} value={"register"}
                                   onClick={() => this.setState({register: true})}/>
                        </form>
                    </div>
                </>)
        }
    }
}


const mapStateToProps = store => {
    console.log(store); // посмотрим, что же у нас в store?
    return {
        is_logged_in: store.is_logged_in,
        username: store.username,
    }
};


const mapDispatchToProps = dispatch => {
    return {
        setLoggedInAction: (username, session_id) => dispatch(setLoggedIn(username, session_id)),
        setLogoutAction: () => dispatch(setLogout()),
    }
};

export const HelloPage = connect(mapStateToProps, mapDispatchToProps)(HelloPageClass);