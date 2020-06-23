import React, {useState} from 'react';
import {Table} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as theService from '../../services/communication';

window.$id = 0

window.$notifications = []

export async function addNotification(notification, msg_type){
    var ls = window.$notifications
    window.$notifications = ls.concat([{'id': window.$id, 'msg': notification, 'msg_type': msg_type}])
    window.$id = window.$id + 1
}

export async function removeNotification(notification_id){
    var new_ls = []
    window.$notifications.array.forEach(noti => {
        if(noti['id'] !== notification_id)
        new_ls.push(noti)
    });
    window.$notifications = new_ls
}

export async function sendAgreementAnswer(notification_dict, answer){

}
