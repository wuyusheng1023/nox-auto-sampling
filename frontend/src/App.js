import React from 'react';
import 'antd/dist/antd.css';
import './index.css';
import Row from 'antd/lib/row';
import Col from 'antd/lib/col';
import Tabframe from './components/TabFrame'

function App() {
  return (
    <div className="App">
      <Row>
        <Col span={16} offset={4}>
          <h1>氮氧化物自动进样系统</h1>
        </Col>
      </Row>
      <Row>
        <Col span={16} offset={4}>
          col-12 col-offset-6
        </Col>
      </Row>
      <Row>
        <Col span={16} offset={4}>
          <Tabframe></Tabframe>
        </Col>
      </Row>
      <Row>
        <Col span={16} offset={4}>
          col-12 col-offset-6
        </Col>
      </Row>
    </div>
  );
}

export default App;
