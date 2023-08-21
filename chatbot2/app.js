const express = require('express');
const fetch = require('node-fetch').default;

const app = express();
const PORT = 3000;

// OpenAI API key setup
const api_key = "";

// FAQ data
const faq_data = [
    {
        "question": "What is your return policy?",
        "answer": "Our return policy lasts 30 days from the date of purchase..."
    },
    {
        "question": "How do I track my order?",
        "answer": "Once your order is shipped, you will receive a tracking link..."
    },
    // Add more FAQ questions and answers here.
];

// Function to get GPT-3.5 answer
async function getGPTAnswer(question) {
    const response = await fetch("https://api.openai.com/v1/engines/text-davinci-003/completions", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${api_key}`
        },
        body: JSON.stringify({
            prompt: question,
            max_tokens: 100
        })
    });

    const data = await response.json();
    return data.choices[0].text.trim();
}

// Express middleware to parse JSON data
app.use(express.json());

// POST endpoint to handle chatbot responses
app.post("/chatbot", (req, res) => {
    const user_input = req.body.user_input;
    const faq_answer = faq_data.find(faq => faq.question.toLowerCase() === user_input.toLowerCase());

    if (faq_answer) {
        res.json({ response: `FAQ Bot: ${faq_answer.answer}` });
    } else {
        getGPTAnswer(user_input)
            .then(gpt_answer => {
                res.json({ response: `GPT-3.5: ${gpt_answer}` });
            })
            .catch(error => {
                console.error("Error:", error);
                res.status(500).json({ error: "Internal Server Error" });
            });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
