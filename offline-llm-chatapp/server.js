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

app.get('/chat', async (req, res) => {
    try {
        const username = req.query.username;
        if (!username) {
            res.status(400).send('Username is required.');
            return;
        }

        // Replace with your actual Llama model credentials
        const llamaModel = require('./llama3.2.1b');
        console.log(`Using ${username}'s Llama model version 1B`);
        let output = '';
        while (true) {
            try {
                const response = await new Promise((resolve, reject) => {
                    const input = 'Hello, ' + username + '! What do you want to say?';
                    llamaModel.generateText(input).then(response => {
                        resolve(response);
                    }).catch(error => {
                        reject(error);
                    });
                });

                output += response + '\n\n';

                // Display the user's message
                console.log(output.trim());
            } catch (error) {
                res.status(500).send('Error occurred while processing your request');
            }
        }

        res.send(`Welcome, ${username}! You have been successfully connected to our chat platform.`);
    } catch (error) {
        console.error(error);
        res.status(404).send('Chat connection failed. Please try again.');
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
