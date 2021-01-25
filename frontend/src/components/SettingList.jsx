import React from 'react';
import 'antd/dist/antd.css';
import { List } from 'antd';
import EditableTagGroup from './EditableTagGroup'

export default function SettingList() {
  const data = [
    { 'name': '类型', 'content': <EditableTagGroup></EditableTagGroup>},
    { 'name': '偏差', 'content': 'Japanese princess to wed commoner.'},
    { 'name': '气瓶类型', 'content': 'Japanese princess to wed commoner.' },
    { 'name': '气瓶压力', 'content': 'Japanese princess to wed commoner.' },
    { 'name': '检测人员', 'content': 'Japanese princess to wed commoner.' },
  ];

  return (
    <List
      bordered
      dataSource={data}
      renderItem={item => (
        <List.Item>
          <List.Item.Meta
            title = {item['name']}
            description = {item['content']}
          />
        </List.Item>
      )}
    />
  )
}
