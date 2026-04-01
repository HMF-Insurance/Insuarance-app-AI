const express = require('express');
const app = express();
const mongoose = require('mongoose');
const cors = require('cors');

app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://127.0.0.1:27017/insurance_enterprise');

app.use('/auth', require('./routes/auth'));
app.use('/claim', require('./routes/claim'));
app.use('/accident', require('./routes/accident'));

app.listen(5000, () => console.log('Server running'));