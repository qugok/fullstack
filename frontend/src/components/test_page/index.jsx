import React from "react";
import passed from "../../media/passed-exam.png";
import diht from "../../media/diht.png";
import board from  "../../media/checkers-table.png";
import "./styles.css";
import {Test} from "../test";

const Header = () => (
    <div className="black-back main-page-header">
        <img className="sponsor-img" src={passed} alt="passed-exam"/>
        <img className="sponsor-img" src={diht} alt="diht"/>
    </div>
);


export class TestPageCheckers extends React.Component {
    constructor(props) {
        super(props);
    };

    render() {
        return (
            <div>
                <div className="main-page-back">

                </div>
                <div className="main-page-front">
                    <Header/>
                    <Test/>
                </div>
            </div>
        )
    }
}