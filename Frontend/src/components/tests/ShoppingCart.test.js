import React from 'react';
import { shallow, mount, render } from '../../enzyme';
import ShoppingCart from '../ShoppingCart'



    it('renders without crashing', () => {
        shallow(<ShoppingCart />);
    });

describe('ShoppingCart Test Suite', () => {

    // checking if the form elements exist and renders all elements
    it('should render the form', () => {
        const wrapper = shallow(<ShoppingCart />);  // shallow renders a single component each time. In other words, Enzyme won’t consider the child elements for the test.


    })
});