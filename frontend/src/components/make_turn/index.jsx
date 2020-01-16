import React from "react"
import "./styles.css";



export class MakeTurn extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
        this.SetFrom = this.SetFrom.bind(this);
        this.SetTo = this.SetTo.bind(this);
    };

    SetFrom = (e) => {
        this.setState({fro : e.target.value});
    };
    SetTo = (e) => {
        this.setState({to : e.target.value});
    };

    render() {
        const {MakeMove} = this.props;
        const move = () => MakeMove(this.state.fro, this.state.to);
        return (

            <>
                <div className="login-part">
                    <div className={"login-text"}>
                        {this.state.fro} {this.state.to} <br/>
                    </div>
                    <form title={"login"} onDragEnter={move}>
                        From <br/>
                        <input title={"from"} type={"text"} placeholder={"from x:y"} onChange={this.SetFrom}/> <br/>
                        To <br/>
                        <input title={"to"} type="text" placeholder={"to x:y"} onChange={this.SetTo}/> <br/>
                        <input title={"submit"} type={"button"} value={"Turn"}  onClick={move}/>
                    </form>
                </div>
            </>
        )
    }
}