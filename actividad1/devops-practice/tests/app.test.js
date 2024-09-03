const request = require('supertest');//Importa la biblioteca supertest para simular solicitudes HTTPS
const app = require('../src/app');//Importa la aplicacion Express app.js, lo que permitira realizar pruebas sobre la aplicacion

let server;

beforeAll((done) => {
    server = app.listen(() => {
        console.log(`Server is running on port ${server.address().port}`);
        done();
    });
});

afterAll((done) => {
    server.close(done);
});

describe('GET /', () => {

	it('should return Hello, World!', async () => {
	const res = await request(app).get('/');
	expect(res.statusCode).toEqual(200);
	expect(res.text).toBe('Hello, World!');
	});
});
