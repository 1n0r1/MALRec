import express from 'express';
const router = express.Router();
import {search} from '../controllers/search.js';

router.post('/', search);

export default router;
