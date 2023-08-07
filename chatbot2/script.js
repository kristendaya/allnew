async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const chatBox = document.getElementById("chatBox");
    

    if (userInput.trim() === "") {
        return;
    }

    const response = await fetch("/chatbot", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "user_input": userInput }),
    });

    if (!response.ok) {
        alert("Error sending the message.");
        return;
    }

    const data = await response.json();
    displayChatBotResponse(chatBox, userInput, data.response);
    document.getElementById("userInput").value = "";
}

function displayChatBotResponse(chatBox, userMessage, botMessage) {
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.textContent = "You: " + userMessage;

    const botDiv = document.createElement("div");
    botDiv.className = "bot-message";
    botDiv.textContent = botMessage;

    chatBox.appendChild(userDiv);
    chatBox.appendChild(botDiv);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}
