const express = require('express');
const app = express();
const port = 8080;

app.use(express.static(__dirname + '/public'));

// Handle login request
app.post('/login', async (req, res) => {
    try {
        const username = req.body.username;
        const password = req.body.password;
        // Replace with your actual Llama model credentials
        if (username === 'llama' && password === 'password') {
            console.log('Login successful!');
            res.send(`Welcome, ${username}!`);
        } else {
            console.error('Invalid username or password');
            res.status(401).send('Invalid username or password');
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Error occurred while processing your request');
    }
});

// Create the client-side code (index.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Llama Chat</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Login to get connected to our chat platform.</h1>
    <form id="login-form">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>

    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@3.13.0/dist/tf.min.js"></script>
    <script src="index.js"></script>
</body>
</html>
