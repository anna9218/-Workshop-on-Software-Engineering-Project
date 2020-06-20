import React, {useState} from 'react';
import {Table} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as theService from '../../services/communication';


function DisplayNotifications(props) {
    const [notifications, setNotifications] = useState([]);

    function addNotification(notification){
        setNotifications(notifications.concat(notification));
    }

    // notifications = [ 
    //                     {'notification_type': str, 'msg': str },
    //                     {'notification_type': str, 'msg': str },
    //                     {'notification_type': str, 'msg': str },
    //                     {'notification_type': str, 'msg': str },
    //                     {'notification_type': str, 'msg': str },
    //                     {'notification_type': str, 'msg': str },
    //                 ]

    return(
        <div >
            <p1>Notifications</p1>
            {/* display notifications */}
            <Table striped bordered hover >
                <thead>
                    <tr>
                        <th>Notification</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        {
                        notifications.length === 0 ?
                            <td>No New Notifications</td>
                            :
                            notifications.map((notification) => (
                                <td>{notification}</td>
                            ))
                        }
                    </tr> 
                </tbody>
            </Table>
        </div> 
    )
}


// exports.Notifications = {
//     addNotification: (notification) => {
//         DisplayNotifications.addNotification(notification)
//     }
// }

export default DisplayNotifications;