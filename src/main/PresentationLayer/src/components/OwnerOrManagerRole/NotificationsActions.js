import React, {useState} from 'react';
import {Table} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as theService from '../../services/communication';

window.$id = 0

window.$notifications = [
    {'id': 0, 'msg': "sdfdddddddddddddddddddddffffffff", 'msg_type': 'regular'},
    {'id': 1, 'msg': "sdfdddddddddddddddddddddffffffff", 'msg_type': 'agreement'},
    {'id': 2, 'msg': "sdfdddddddddddddddddddddffffffff", 'msg_type': 'agreement'},
    {'id': 3, 'msg': "sdfdddddddddddddddddddddffffffff", 'msg_type': 'agreement'}
]

export async function addNotification(notification, msg_type){
    var ls = window.$notifications
    window.$notifications = ls.concat([{'id': window.$id, 'msg': notification, 'msg_type': msg_type}])
    window.$id = window.$id + 1
}

export  function removeNotification(notification_id){
    var new_ls = []
    window.$notifications.forEach(noti => {

        if(noti['id'] !== notification_id)
            new_ls.push(noti)
    });
    window.$notifications = new_ls

}

export  function sendAgreementAnswer(event, notification_dict, answer){

    removeNotification(notification_dict['id'])
}
