import React from 'react';
import 'antd/dist/antd.css';
import './index.css';
import js_logo from './img/js_logo.png'
import Row from 'antd/lib/row';
import Col from 'antd/lib/col';
import Divider from 'antd/lib/divider';
import Tabframe from './components/TabFrame'
import Status from './components/Status'


function App() {
  return (
    <div className="App">
      <Row>
        <Col span={18} offset={3} >
          <h1 style={{ float: 'left' }}>氮氧化物自动进样系统</h1>
          <img style={{ float: 'right', marginTop: '10px'}}src={ js_logo } alt={"Logo"} width={100}/>
        </Col>
      </Row>
      <Row>
        <Col span={18} offset={3}>
          <Status/>
        </Col>
      </Row>
      <Row>
        <Col span={18} offset={3}>
          <Tabframe/>
        </Col>
      </Row>
      <Row>
        <Col span={18} offset={3}>
          <Divider orientation="left"></Divider>
          <p style={{ textAlign: 'center', fontSize: '8px', marginTop: '30px' }}>
            © Copyright 2021. All Rights Reserved.
            <br></br>北京嘉时高科科技发展有限公司
          </p>
        </Col>
      </Row>
    </div>
  );
}

export default App;
