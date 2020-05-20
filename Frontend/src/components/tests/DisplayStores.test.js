import React from 'react';
import { shallow, mount, render } from '../../enzyme';
import DisplayStores from '../Actions/DisplayStores'



    it('renders without crashing', () => {
        shallow(<DisplayStores />);
    });

describe('DisplayStores Test Suite', () => {

    // checking if the form elements exist and renders all elements
    it('should render the form', () => {
        const wrapper = shallow(<DisplayStores />);  // shallow renders a single component each time. In other words, Enzyme won’t consider the child elements for the test.


    })
});