const loginForm = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    try {
        const username = usernameInput.value.trim();
        if (!username) {
            throw new Error("Username is required.");
        }

        try {
            // Replace with your actual Llama model credentials
            const response = await fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password }),
            });

            if (response.ok) {
                console.log('Login successful!');
                location.reload();
            } else {
                throw new Error(`Invalid username or password`);
            }
        } catch (error) {
            console.error(error);
            alert('Error occurred while processing your request');
        }
    } catch (error) {
        console.error(error);
        alert('Chat connection failed. Please try again.');
    }
});
