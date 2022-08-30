import React, {useState} from 'react';
import data from "../../utils/data.js";
import {Typography, TextField} from '@mui/material';
import {search} from '../../actions/Search.js';
import {useDispatch} from 'react-redux';

const Searchbar = () => {
    const dispatch = useDispatch();
    const [arr, setArr] = useState([])
    const [query, setQuery] = useState("");
    const [loading, setLoading] = useState(false);

    function handleSubmit(e){
        e.preventDefault();
        dispatch(search(query)).then(() => setLoading(false));
    }
    function handleChange(e){
        setQuery(e.target.value)
        setArr(data.anime.filter(x => x[1].toLowerCase().includes(e.target.value.toLowerCase())))
    }

    function handleClick(e){
        setQuery(e.target.name)
        setArr([])
        setLoading(true);
        dispatch(search(e.target.value)).then(()=>{
            setLoading(false);
        })        
    }

    return (
        <>

            <form onSubmit={handleSubmit}>
                <TextField disabled={loading} fullWidth label="Search" id="fullWidth" onChange={handleChange}/>
            </form>
            {
                arr.map(x => (
                    <>

                        <button key={x[1]} name={x[1]} value={x[0]} onClick={handleClick}>
                            {x[1]}
                        </button>
                        <br/>
                    </>

                ))
            }
            {
                loading?(
                    <Typography>Loading</Typography>
                ):(
                    <></>
                )
            }
        </>
    );
};
export default Searchbar;


