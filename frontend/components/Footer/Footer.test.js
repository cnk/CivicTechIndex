import React from 'react';
import {
    shallow,
    // mount
} from 'enzyme';

import Footer from './';
// import data from './Footer.data';

describe('<Footer />', () => {
    it('Renders an empty Footer', () => {
        const component = shallow(<Footer />);
        expect(component).toBeTruthy();
    });

    // it('Renders Footer with data', () => {
    //     const component = mount(<Footer {...data} />);
    //     expect(component).toMatchSnapshot();
    // });
});
