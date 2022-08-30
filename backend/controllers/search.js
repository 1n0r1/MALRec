import express from 'express';
import Pdf from '../models/pdf.js';
import PdfImg from '../models/pdfImg.js';
import Embed from '../models/embed.js';
import {spawn} from 'node:child_process';
import {Base64} from 'js-base64';
import {writeFile} from 'node:fs';
import fs from 'fs';
const router = express.Router();


export const search = async (req,res) =>{
    try{
        const query = req.body.query;
        const python = await spawn('python3', ['./python/input.py', query, '10']);
        var results = '';
        python.stdout.on('data', function(data) {
            results += data.toString()
            console.log(data.toString())
        })
        python.stderr.on('data', function(data) {
            console.log(`${data}`)
        })
        await new Promise( (resolve) => {
            python.on('close', resolve);
        });
        res.status(200).json(results);
    } catch(err) {
        console.log(err)
        res.status(400).json("error: " + err);
    }
};
