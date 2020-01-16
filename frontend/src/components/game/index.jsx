import React from "react";
import passed from "../../media/passed-exam.png";
import diht from "../../media/diht.png";
import "./styles.css";
import {MakeTurn} from "../make_turn";
import {Test} from "../test";
import {Table} from "../my_board";
import {CheckLogIn, CreateGame, GetAllTable, MakeMove} from "../../actions/register";
import {connect} from "react-redux";

const Header = () => (
    <div className="black-back main-page-header">
        <img className="sponsor-img" src={passed} alt="passed-exam"/>
        <img className="sponsor-img" src={diht} alt="diht"/>
    </div>
);

// const LogoPart = () => (
//     <div className="main-page-logo-part">
//         {/*<Board/>*/}
//     </div>
// );

const RulesPart = ({onClick = f => f}) => (
    <div className="black-back main-page-about">
        <div className="main-page-section-title">
            Правила
        </div>
        <div className="main-page-about-text">
            Существует много разных вариаций правил шашек.
            <p>Основные правила игры, которые действуют во всех вариантах шашек:
            </p>
            <ul>
                <li>Все шашки, участвующие в партии, выставляются перед началом игры на доску. Далее они передвигаются
                    по полям доски и могут быть сняты с неё в случае боя шашкой противника.
                </li>
                <li>Брать шашку, находящуюся под боем, обязательно. Исключение: "Сибирские шашки".</li>
                <li>Существует только два вида шашек: простые и дамки. В начале партии все шашки простые. Простая шашка
                    может превратиться в дамку, если она достигнет последнего противоположного горизонтального ряда
                    доски (дамочного поля).
                </li>
                <li>Простые шашки ходят только вперёд на следующее поле. Дамки могут ходить и вперёд и назад.
                </li>
            </ul>
        </div>
        <a className="more-rules-button" href={'https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D1%88%D0%BA%D0%B8'}>
            Узнать больше о правилах
        </a>
    </div>
);


export class GamePageCheckersClass extends React.Component {
    constructor(props) {
        super(props);
    };

    render() {
        const {username, session_id, player_number, table, GetAllTableAction, MakeMoveAction} = this.props;
        return (
            <div>
                <div className="main-page-back">

                </div>
                <div className="main-page-front">
                    <Header/>
                    {/*<LogoPart/>*/}
                    <MakeTurn MakeMove={(fro, to) => MakeMoveAction(username, session_id, player_number, fro, to)}/>
                    <Table GetAllTable={() => GetAllTableAction(username, session_id, player_number)} table={table}/>
                    {/*<Test/>*/}
                    <RulesPart/>
                </div>
            </div>
        )
    }
}


const mapStateToProps = store => {
    console.log(store); // посмотрим, что же у нас в store?
    return {
        // is_logged_in: store.is_logged_in,
        username: store.username,
        session_id: store.session_id,
        player_number: store.player_number,
        table: store.game_table,
    }
};


const mapDispatchToProps = dispatch => {
    return {
        CheckLogInAction: (username, session_id) => CheckLogIn(dispatch, username, session_id),
        CreateGameAction: (username, session_id) => CreateGame(dispatch, username, session_id),
        GetAllTableAction: (username, session_id, player_number) => GetAllTable(dispatch, username, session_id, player_number),
        MakeMoveAction: (username, session_id, player_number, fro, to) => MakeMove(dispatch, username, session_id, player_number, fro, to),

    }
};

export const GamePageCheckers = connect(mapStateToProps, mapDispatchToProps)(GamePageCheckersClass);
