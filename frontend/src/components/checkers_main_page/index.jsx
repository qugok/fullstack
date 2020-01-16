import React from "react";
import passed from "../../media/passed-exam.png";
import diht from "../../media/diht.png";
import board from  "../../media/checkers-table.png";
import "./styles.css";
import {HelloPage} from "../hello_page";
import {CheckLogIn, CreateGame} from "../../actions/register";
import {connect} from "react-redux";

const Header = () => (
    <div className="black-back main-page-header">
        <img className="sponsor-img" src={passed} alt="passed-exam"/>
        <img className="sponsor-img" src={diht} alt="diht"/>
    </div>
);


const LogoPart = ({onClick=f=>f}) => (
    <div className="main-page-logo-part">
        <img className="logo-img" src={board} alt="checkers-board"/>
        <div className="logo-text">
            Шашки
        </div>
        <div className="logo-info-text">
            Логическая настольная игра для двух игроков, заключающаяся в передвижении определённым образом фишек-шашек по клеткам шашечной доски.
            {/*<br/> Существует несколько вариантов шашек, отличающихся правилами и размерами игрового поля.*/}
        </div>
        <button className="new-game-button" onClick={() => onClick()}>
            Новая игра
        </button>
    </div>
);

const RulesPart = () => (
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


export class MainPageCheckersClass extends React.Component {
    constructor(props) {
        super(props);
    };

    render() {
        const {username, session_id, CreateGameAction} = this.props;
        return (
            <div>
                <div className="main-page-back">

                </div>
                <div className="main-page-front">
                    <Header/>
                    <HelloPage/>
                    <LogoPart onClick={() => {this.props.history.push('/game'); CreateGameAction(username, session_id)}}/>
                    <RulesPart />
                </div>
            </div>
        )
    }

    componentDidMount() {
        const {username, session_id, CheckLogInAction} = this.props;
        CheckLogInAction(username, session_id);
    }
}


const mapStateToProps = store => {
    console.log(store); // посмотрим, что же у нас в store?
    return {
        username: store.username,
        session_id: store.session_id,
    }
};


const mapDispatchToProps = dispatch => {
    return {
        CheckLogInAction: (username, session_id) => CheckLogIn(dispatch, username, session_id),
        CreateGameAction: (username, session_id) => CreateGame(dispatch, username, session_id),
    }
};

export const MainPageCheckers = connect(mapStateToProps, mapDispatchToProps)(MainPageCheckersClass);


