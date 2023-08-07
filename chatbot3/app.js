const chatboxMessages = document.getElementById('chatboxMessages');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');

function addMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender === 'user' ? 'message--user' : 'message--chatbot');
    messageElement.innerText = message;
    chatboxMessages.appendChild(messageElement);
}

function sendMessage() {
    const userMessage = userInput.value.trim();
    if (userMessage !== '') {
        addMessage('user', userMessage);
        userInput.value = '';

        fetch(`/get-answer/?question=${encodeURIComponent(userMessage)}`)
            .then(response => response.json())
            .then(data => {
                const chatbotResponse = data.response;
                addMessage('chatbot', chatbotResponse);
            })
            .catch(error => console.error(error));
    }
}

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', event => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
