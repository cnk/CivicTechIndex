/* global module */

import React from 'react';
import { MemoryRouter } from "react-router";
import { storiesOf } from '@storybook/react';
import HomePage from './HomePage';

import data from './HomePage.data';

storiesOf('Containers|HomePage', module)
    .add('without data', () => <MemoryRouter initialEntries={['/']}><HomePage /></MemoryRouter>)
    .add('with data', () => <MemoryRouter initialEntries={['/']}><HomePage {...data} /></MemoryRouter>);
