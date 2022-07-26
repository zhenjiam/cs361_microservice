// use requested data from CalcBudget.py to retrieve budget goal and preferred interval

'use strict';

const express = require("express");
const { send } = require("express/lib/response");

const app = express();
const PORT = 5000
app.use(express.json())

function Url(req, res, next) {
    console.log(`URL = ${req.originalUrl}`);
    next();
}

app.get('/:id', Url, (req, res, next) => {
    res.status(201).json(req.originalUrl);
})

app.listen(PORT, () => {
    console.log(`Server Started and Listening on ${PORT}...`)
})
