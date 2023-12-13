const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;

// Read the fake results from the file
const data = JSON.parse(fs.readFileSync('fakeResult.json', 'utf8'));

app.get('/search', (req, res) => {
    const query = req.query.q;
    // This is where you'd implement search logic. For now, return all data.
    res.json(data.filter(item => item.toLowerCase().includes(query.toLowerCase())));
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
