import React from 'react';
import 'antd/dist/antd.css';
import './index.css';
import { Row, Col } from 'antd';
import Tabframe from './components/TabFrame'

function App() {
  return (
    <div className="App">
      <Row>
        <Col span={12} offset={6}>
          col-12 col-offset-6
        </Col>
      </Row>
      <Row>
        <Col span={12} offset={6}>
          col-12 col-offset-6
        </Col>
      </Row>
      <Row>
        <Col span={12} offset={6}>
          <Tabframe></Tabframe>
        </Col>
      </Row>
      <Row>
        <Col span={12} offset={6}>
          col-12 col-offset-6
        </Col>
      </Row>
    </div>
  );
}

export default App;
