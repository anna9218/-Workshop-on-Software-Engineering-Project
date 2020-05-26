import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'


function Nav(){
  return (
      <nav>
          <h3>Logo</h3>
          <ul className="nav-links">
              <Link to='/guest'>
                <li>Link1-guest</li>
              </Link>
              <Link to='/register'>
                <li>Link2-register</li>
              </Link>
          </ul>
      </nav>
  );
}

export default Nav;