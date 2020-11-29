/* global module */

import React from 'react';
import { MemoryRouter } from "react-router";
import { storiesOf } from '@storybook/react';
import Header from './Header';

import data from './Header.data.js';

storiesOf('Components|Header', module)
    .add('with data', () => <MemoryRouter initialEntries={['/']}><Header {...data} /></MemoryRouter>)
    .add('without data', () => <MemoryRouter initialEntries={['/']}><Header /></MemoryRouter>);
