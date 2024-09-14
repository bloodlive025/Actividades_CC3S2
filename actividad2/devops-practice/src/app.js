const express = require('express');
const app = express();
const client = require('prom-client'); // Importa prom-client

client.collectDefaultMetrics();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});


app.get('/metrics', async (req, res) => {
    try {
        res.set('Content-Type', client.register.contentType); // Establece el tipo de contenido correcto
        res.end(await client.register.metrics()); // Devuelve las métricas
    } catch (err) {
        res.status(500).end(err); // Si hay un error, responde con un código 500
    }
});

module.exports = app;

if (require.main === module) {
    const port = process.env.PORT || 3000; 
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}
