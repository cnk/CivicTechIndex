import BasePage from './BasePage';
import Footer from '../../components/Footer';
import React from 'react';

export const basePageWrap = (Component) => (props) => {
    return (
        <BasePage {...props} _class={Component.name}>
            <Component {...props} />
            <Footer {...props} />
        </BasePage>
    );
};

export default BasePage;
