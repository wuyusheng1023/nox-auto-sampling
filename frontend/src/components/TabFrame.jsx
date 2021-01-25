import React from 'react';
import { Tabs } from 'antd';
import SettingList from './SettingList'

const { TabPane } = Tabs;

export default function Tabframe() {
  return(
    <Tabs defaultActiveKey="1">
      <TabPane tab="Tab 1" key="1">
        Content of Tab Pane 1
      </TabPane>
      <TabPane tab="Tab 2" key="2">
        Content of Tab Pane 2
      </TabPane>
      <TabPane tab="设置" key="3">
        <SettingList></SettingList>
      </TabPane>
    </Tabs>
  );
}
