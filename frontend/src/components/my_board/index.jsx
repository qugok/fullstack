import React from "react";
import "./styles.css";

export class Table extends React.Component {
    constructor(props) {
        super(props);
    };

    render() {
        const getAllTable = this.props.GetAllTable;
        const table = this.props.table;
        return (

            <>
                <div className="login-part">
                    <div className={"login-text"}>
                        {JSON.stringify(table)} <br/>
                    </div>
                    <form title={"login"} onDragEnter={this.Submit}>
                        <input title={"submit"} type={"button"} value={"get_all_table"} onClick={getAllTable}/>
                    </form>
                </div>
            </>
        )
    }
}