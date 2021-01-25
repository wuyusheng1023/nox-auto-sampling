import React from 'react';
import 'antd/dist/antd.css';
import List from 'antd/lib/list';
import EditableTagGroup from './EditableTagGroup'


export default function SettingList() {
  let settingData = [
    { 'name': '类型', 'tags': ['校准', '质控', '样品'] },
    { 'name': '偏差', 'tags': ['0.1 %', '0.5 %', '1 %'] },
    { 'name': '气瓶类型',
      'tags': ['美托 2 升', '美托 4 升', '美托 8 升', '科金 2 升', '科金 4 升', '科金 8 升'] 
    },
    { 'name': '气瓶压力', 'tags': ['11.0 MPa', '10.9 MPa', '10.8 MPa', '10.7 MPa'] },
    { 'name': '检测人员', 'tags': ['倪才倩,', '范洁'] },
  ]

  const onUpdate = function(name, tags) {
    settingData = settingData.map(
        item => item['name'] !== name ? item : {name : name, 'tags': tags }
     )
  };

  return (
    <>
      '保存设置', '恢复默认设置',
      <List
        itemLayout="horizontal"
        dataSource={ settingData }
        renderItem={ item => (
          <List.Item>
            <List.Item.Meta
              title={ item.name }
              description=<EditableTagGroup
                name={ item.name } 
                tags={ item.tags}  
                onUpdate = { onUpdate }
              />
            />
          </List.Item>
        )}
      />
    </>
  )
}
