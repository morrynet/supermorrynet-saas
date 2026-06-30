import express from 'express';
import cors from 'cors';
import path from 'path';
import { fileURLToPath } from 'url';
import apiRouter from './backend/api.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Enable CORS and body parsers
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Mount backend API routes under /api
app.use('/api', apiRouter);

// Serve static assets for the entire root directory (all 151 folders, design systems, scripts)
app.use(express.static(__dirname));

// Route root path to index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log(`================================================================`);
    console.log(`  PRECISION SNIPER ICT - INSTITUTIONAL GRADED DASHBOARD SERVER  `);
    console.log(`================================================================`);
    console.log(`  Local Access: http://localhost:${PORT}`);
    console.log(`  API Status:   Active`);
    console.log(`  Static Pages: Serving 151 modular subdirectories`);
    console.log(`================================================================`);
});
