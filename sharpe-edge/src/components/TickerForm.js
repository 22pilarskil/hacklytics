import { useState, useEffect } from 'react';
import axios from 'axios';
import { API_URL, STATIC_URL } from "../constants/Constants";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

function TickerForm() {

    const [inputs, setInputs] = useState({});

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}))
        console.log(value + name);
    }


    const handleSubmit = (event) => {
        event.preventDefault();

        const formData = new FormData();

        formData.append('ticker1', inputs.ticker1);
        formData.append('ticker2', inputs.ticker2);

        const config = {
            config: {
            'content-type': 'multipart/form-data',
            },
        };
        axios.post(API_URL + "sendTickers", formData, config).then(response => {
            console.log(response.data.success)
        });

    }

    var width = 400;
    var width_space = 10;
    var width_box = width / 2 - width_space / 2;
    width = width + "px";
    width_space = width_space + "px";
    width_box = width_box + "px";

    const center = {
        'margin':'0 auto',
        'width':width,
        'gridTemplateColums':'1fr',
    }
    const blocks = {
        "display": "flex",
        "width": width,
        "height": "auto",
        "marginTop":"5px"
      }


    return (
        <div style={center}>
            <form onSubmit={handleSubmit}>
                <div style={blocks}>
                    <TextField type="text" name="ticker1" onChange={handleChange} label="Ticker 1" style={{"width":width_box}}/>
                    <div style={{"width":width_space}}></div>
                    <TextField type="text" name="ticker2" onChange={handleChange} label="Ticker 2" style={{"width":width_box}}/>
                </div>
            <Button variant="contained" style={blocks} type="submit">Upload</Button>
            </form>
        </div>
    )
}

export default TickerForm;