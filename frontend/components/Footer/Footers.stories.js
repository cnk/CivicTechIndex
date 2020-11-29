/* global module */

import React from 'react';
import { MemoryRouter } from "react-router";
import { storiesOf } from '@storybook/react';
import Footer from './Footer';

import data from './Footer.data.js';

storiesOf('Components|Footer', module)
    .add('with data', () => <MemoryRouter initialEntries={['/']}><Footer {...data} /></MemoryRouter>)
    .add('without data', () => <MemoryRouter initialEntries={['/']}><Footer /></MemoryRouter>);
