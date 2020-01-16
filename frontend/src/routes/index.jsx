import React from 'react';
import {Route, Switch} from 'react-router';
import {MainPageCheckers} from "../components/checkers_main_page"
import {GamePageCheckers} from "../components/game"

const MainRouter = () => (
    <Switch>
        {/*необходимо полное совпадение*/}
        <Route exact path='/' component={ MainPageCheckers } />
        {/*необходимо только совпадение префикса*/}
        {/*ролучить можно как this.props.match.params.id*/}
        <Route path='/checkers' component={ MainPageCheckers } />
        <Route path='/game' component={ GamePageCheckers } />
    </Switch>
);
export default MainRouter;