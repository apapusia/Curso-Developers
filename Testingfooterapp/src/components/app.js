
import React, { Component } from 'react';
import { footer } from 'devcamp-js-footer';

export default class App extends Component {
  render() {
    return (
      <div>
        <h1>DevCamp React Starter</h1>
        { footer('DevCamp') }
      </div>
    );
  }
}