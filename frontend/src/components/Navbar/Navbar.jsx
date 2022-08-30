import React, {useState, useEffect} from "react";
import {useNavigate, useLocation} from "react-router";
import {useDispatch} from "react-redux";
import { Menu, MenuItem, Typography, Toolbar, AppBar, Box, Button, Avatar, IconButton } from "@mui/material";
import {Link } from "react-router-dom";
import SearchIcon from '@mui/icons-material/Search';
import Searchbar from "../Searchbar/Searchbar.jsx";

function Navbar(){
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const location = useLocation();

    return(
        <>
            <AppBar position="fixed" variant="dense">
                <Toolbar>
                    <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "flex" } }}>
                        <MenuItem key="pdf" onClick={() => {navigate("/");}}>
                            <Typography variant="h6" textAlign="center">Myanimelist Recommendation system</Typography>
                        </MenuItem>
                    </Box>
                </Toolbar>
            </AppBar>
            <Toolbar/>
        </>
    );
}

export default Navbar;
