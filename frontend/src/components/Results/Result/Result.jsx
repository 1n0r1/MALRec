import React, {useState} from 'react';
import {Typography} from '@mui/material';
import PropTypes from 'prop-types';


export default function Result({value}) {
    return (
        <>
            <Typography variant="h6">{value[0]}</Typography>
            <Typography variant="h6">{value[1]}</Typography>
        </>
    );
};


Result.propTypes = {
    value: PropTypes.object,
};
