{"changed":true,"filter":false,"title":"app.js","tooltip":"/chatbot2/app.js","value":"const express = require('express');\nconst fetch = require('node-fetch').default;\n\nconst app = express();\nconst PORT = 3000;\n\n// OpenAI API key setup\nconst api_key = \"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\";\n\n// FAQ data\nconst faq_data = [\n    {\n        \"question\": \"What is your return policy?\",\n        \"answer\": \"Our return policy lasts 30 days from the date of purchase...\"\n    },\n    {\n        \"question\": \"How do I track my order?\",\n        \"answer\": \"Once your order is shipped, you will receive a tracking link...\"\n    },\n    // Add more FAQ questions and answers here.\n];\n\n// Function to get GPT-3.5 answer\nasync function getGPTAnswer(question) {\n    const response = await fetch(\"https://api.openai.com/v1/engines/text-davinci-003/completions\", {\n        method: \"POST\",\n        headers: {\n            \"Content-Type\": \"application/json\",\n            \"Authorization\": `Bearer ${api_key}`\n        },\n        body: JSON.stringify({\n            prompt: question,\n            max_tokens: 100\n        })\n    });\n\n    const data = await response.json();\n    return data.choices[0].text.trim();\n}\n\n// Express middleware to parse JSON data\napp.use(express.json());\n\n// POST endpoint to handle chatbot responses\napp.post(\"/chatbot\", (req, res) => {\n    const user_input = req.body.user_input;\n    const faq_answer = faq_data.find(faq => faq.question.toLowerCase() === user_input.toLowerCase());\n\n    if (faq_answer) {\n        res.json({ response: `FAQ Bot: ${faq_answer.answer}` });\n    } else {\n        getGPTAnswer(user_input)\n            .then(gpt_answer => {\n                res.json({ response: `GPT-3.5: ${gpt_answer}` });\n            })\n            .catch(error => {\n                console.error(\"Error:\", error);\n                res.status(500).json({ error: \"Internal Server Error\" });\n            });\n    }\n});\n\n// Start the server\napp.listen(PORT, () => {\n    console.log(`Server is running on http://localhost:${PORT}`);\n});\n","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":0,"column":0},"end":{"row":48,"column":0},"action":"insert","lines":["from fastapi import FastAPI, File, UploadFile, Form","import openai","","app = FastAPI()","","# OpenAI API key setup","api_key = \"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\"","openai.api_key = api_key","","# FAQ data","faq_data = [","    {","        \"question\": \"What is your return policy?\",","        \"answer\": \"Our return policy lasts 30 days from the date of purchase...\"","    },","    {","        \"question\": \"How do I track my order?\",","        \"answer\": \"Once your order is shipped, you will receive a tracking link...\"","    },","    # Add more FAQ questions and answers here.","]","","def get_gpt_answer(question):","    # Use GPT-3.5 API to generate an answer for the question","    response = openai.Completion.create(","        engine=\"text-davinci-003\",","        prompt=question,","        max_tokens=100","    )","    return response.choices[0].text.strip()","","@app.post(\"/process_file\")","async def process_file(file: UploadFile = File(...)):","    # Read the content of the uploaded file","    file_content = await file.read()","","    # Process the file content and generate the answer","    user_input = file_content.decode(\"utf-8\")","    faq_answer = next((faq[\"answer\"] for faq in faq_data if faq[\"question\"].lower() == user_input.lower()), None)","","    if faq_answer:","        response_text = f\"FAQ Bot: {faq_answer}\"","    else:","        # If the question is not in the FAQ data, use GPT-3.5 for the answer","        gpt_answer = get_gpt_answer(user_input)","        response_text = f\"GPT-3.5: {gpt_answer}\"","","    return {\"response\": response_text}",""],"id":21}],[{"start":{"row":0,"column":0},"end":{"row":47,"column":38},"action":"remove","lines":["from fastapi import FastAPI, File, UploadFile, Form","import openai","","app = FastAPI()","","# OpenAI API key setup","api_key = \"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\"","openai.api_key = api_key","","# FAQ data","faq_data = [","    {","        \"question\": \"What is your return policy?\",","        \"answer\": \"Our return policy lasts 30 days from the date of purchase...\"","    },","    {","        \"question\": \"How do I track my order?\",","        \"answer\": \"Once your order is shipped, you will receive a tracking link...\"","    },","    # Add more FAQ questions and answers here.","]","","def get_gpt_answer(question):","    # Use GPT-3.5 API to generate an answer for the question","    response = openai.Completion.create(","        engine=\"text-davinci-003\",","        prompt=question,","        max_tokens=100","    )","    return response.choices[0].text.strip()","","@app.post(\"/process_file\")","async def process_file(file: UploadFile = File(...)):","    # Read the content of the uploaded file","    file_content = await file.read()","","    # Process the file content and generate the answer","    user_input = file_content.decode(\"utf-8\")","    faq_answer = next((faq[\"answer\"] for faq in faq_data if faq[\"question\"].lower() == user_input.lower()), None)","","    if faq_answer:","        response_text = f\"FAQ Bot: {faq_answer}\"","    else:","        # If the question is not in the FAQ data, use GPT-3.5 for the answer","        gpt_answer = get_gpt_answer(user_input)","        response_text = f\"GPT-3.5: {gpt_answer}\"","","    return {\"response\": response_text}"],"id":22},{"start":{"row":0,"column":0},"end":{"row":44,"column":38},"action":"insert","lines":["from fastapi import FastAPI","","import openai","","app = FastAPI()","","# OpenAI API key setup","api_key = \"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\"","openai.api_key = api_key","","# FAQ data","faq_data = [","    {","        \"question\": \"What is your return policy?\",","        \"answer\": \"Our return policy lasts 30 days from the date of purchase...\"","    },","    {","        \"question\": \"How do I track my order?\",","        \"answer\": \"Once your order is shipped, you will receive a tracking link...\"","    },","    # Add more FAQ questions and answers here.","]","","def get_gpt_answer(question):","    # Use GPT-3.5 API to generate an answer for the question","    response = openai.Completion.create(","        engine=\"text-davinci-003\",","        prompt=question,","        max_tokens=100","    )","    return response.choices[0].text.strip()","","@app.post(\"/chatbot\")","async def chatbot_response(user_input: str = Form(...)):","    # Process user input and generate the appropriate response","    faq_answer = next((faq[\"answer\"] for faq in faq_data if faq[\"question\"].lower() == user_input.lower()), None)","","    if faq_answer:","        response_text = f\"FAQ Bot: {faq_answer}\"","    else:","        # If the question is not in the FAQ data, use GPT-3.5 for the answer","        gpt_answer = get_gpt_answer(user_input)","        response_text = f\"GPT-3.5: {gpt_answer}\"","","    return {\"response\": response_text}"]}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":62},"action":"remove","lines":["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"],"id":23},{"start":{"row":7,"column":11},"end":{"row":7,"column":62},"action":"insert","lines":["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"]}],[{"start":{"row":32,"column":0},"end":{"row":44,"column":38},"action":"remove","lines":["@app.post(\"/chatbot\")","async def chatbot_response(user_input: str = Form(...)):","    # Process user input and generate the appropriate response","    faq_answer = next((faq[\"answer\"] for faq in faq_data if faq[\"question\"].lower() == user_input.lower()), None)","","    if faq_answer:","        response_text = f\"FAQ Bot: {faq_answer}\"","    else:","        # If the question is not in the FAQ data, use GPT-3.5 for the answer","        gpt_answer = get_gpt_answer(user_input)","        response_text = f\"GPT-3.5: {gpt_answer}\"","","    return {\"response\": response_text}"],"id":24},{"start":{"row":32,"column":0},"end":{"row":44,"column":38},"action":"insert","lines":["@app.post(\"/chatbot\")","async def chatbot_response(user_input: str = Form(...)):","    # Process user input and generate the appropriate response","    faq_answer = next((faq[\"answer\"] for faq in faq_data if faq[\"question\"].lower() == user_input.lower()), None)","","    if faq_answer:","        response_text = f\"FAQ Bot: {faq_answer}\"","    else:","        # If the question is not in the FAQ data, use GPT-3.5 for the answer","        gpt_answer = get_gpt_answer(user_input)","        response_text = f\"GPT-3.5: {gpt_answer}\"","","    return {\"response\": response_text}"]}],[{"start":{"row":32,"column":0},"end":{"row":44,"column":38},"action":"remove","lines":["@app.post(\"/chatbot\")","async def chatbot_response(user_input: str = Form(...)):","    # Process user input and generate the appropriate response","    faq_answer = next((faq[\"answer\"] for faq in faq_data if faq[\"question\"].lower() == user_input.lower()), None)","","    if faq_answer:","        response_text = f\"FAQ Bot: {faq_answer}\"","    else:","        # If the question is not in the FAQ data, use GPT-3.5 for the answer","        gpt_answer = get_gpt_answer(user_input)","        response_text = f\"GPT-3.5: {gpt_answer}\"","","    return {\"response\": response_text}"],"id":25},{"start":{"row":32,"column":0},"end":{"row":44,"column":38},"action":"insert","lines":["@app.post(\"/chatbot\")","async def chatbot_response(user_input: str):","    # Process user input and generate the appropriate response","    faq_answer = next((faq[\"answer\"] for faq in faq_data if faq[\"question\"].lower() == user_input.lower()), None)","","    if faq_answer:","        response_text = f\"FAQ Bot: {faq_answer}\"","    else:","        # If the question is not in the FAQ data, use GPT-3.5 for the answer","        gpt_answer = get_gpt_answer(user_input)","        response_text = f\"GPT-3.5: {gpt_answer}\"","","    return {\"response\": response_text}"]}],[{"start":{"row":0,"column":0},"end":{"row":45,"column":0},"action":"remove","lines":["from fastapi import FastAPI","","import openai","","app = FastAPI()","","# OpenAI API key setup","api_key = \"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\"","openai.api_key = api_key","","# FAQ data","faq_data = [","    {","        \"question\": \"What is your return policy?\",","        \"answer\": \"Our return policy lasts 30 days from the date of purchase...\"","    },","    {","        \"question\": \"How do I track my order?\",","        \"answer\": \"Once your order is shipped, you will receive a tracking link...\"","    },","    # Add more FAQ questions and answers here.","]","","def get_gpt_answer(question):","    # Use GPT-3.5 API to generate an answer for the question","    response = openai.Completion.create(","        engine=\"text-davinci-003\",","        prompt=question,","        max_tokens=100","    )","    return response.choices[0].text.strip()","","@app.post(\"/chatbot\")","async def chatbot_response(user_input: str):","    # Process user input and generate the appropriate response","    faq_answer = next((faq[\"answer\"] for faq in faq_data if faq[\"question\"].lower() == user_input.lower()), None)","","    if faq_answer:","        response_text = f\"FAQ Bot: {faq_answer}\"","    else:","        # If the question is not in the FAQ data, use GPT-3.5 for the answer","        gpt_answer = get_gpt_answer(user_input)","        response_text = f\"GPT-3.5: {gpt_answer}\"","","    return {\"response\": response_text}",""],"id":26}],[{"start":{"row":0,"column":0},"end":{"row":66,"column":0},"action":"insert","lines":["const express = require('express');","const fetch = require('node-fetch');","","const app = express();","const PORT = 3000;","","// OpenAI API key setup","const api_key = \"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\";","","// FAQ data","const faq_data = [","    {","        \"question\": \"What is your return policy?\",","        \"answer\": \"Our return policy lasts 30 days from the date of purchase...\"","    },","    {","        \"question\": \"How do I track my order?\",","        \"answer\": \"Once your order is shipped, you will receive a tracking link...\"","    },","    // Add more FAQ questions and answers here.","];","","// Function to get GPT-3.5 answer","async function getGPTAnswer(question) {","    const response = await fetch(\"https://api.openai.com/v1/engines/text-davinci-003/completions\", {","        method: \"POST\",","        headers: {","            \"Content-Type\": \"application/json\",","            \"Authorization\": `Bearer ${api_key}`","        },","        body: JSON.stringify({","            prompt: question,","            max_tokens: 100","        })","    });","","    const data = await response.json();","    return data.choices[0].text.trim();","}","","// Express middleware to parse JSON data","app.use(express.json());","","// POST endpoint to handle chatbot responses","app.post(\"/chatbot\", (req, res) => {","    const user_input = req.body.user_input;","    const faq_answer = faq_data.find(faq => faq.question.toLowerCase() === user_input.toLowerCase());","","    if (faq_answer) {","        res.json({ response: `FAQ Bot: ${faq_answer.answer}` });","    } else {","        getGPTAnswer(user_input)","            .then(gpt_answer => {","                res.json({ response: `GPT-3.5: ${gpt_answer}` });","            })","            .catch(error => {","                console.error(\"Error:\", error);","                res.status(500).json({ error: \"Internal Server Error\" });","            });","    }","});","","// Start the server","app.listen(PORT, () => {","    console.log(`Server is running on http://localhost:${PORT}`);","});",""],"id":27}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":68},"action":"remove","lines":["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"],"id":28},{"start":{"row":7,"column":17},"end":{"row":7,"column":68},"action":"insert","lines":["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"]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":44},"action":"insert","lines":["const fetch = require('node-fetch').default;"],"id":29}],[{"start":{"row":2,"column":44},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":30}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":36},"action":"remove","lines":["const fetch = require('node-fetch');"],"id":31},{"start":{"row":0,"column":35},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":420,"scrollleft":0,"selection":{"start":{"row":21,"column":0},"end":{"row":21,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":23,"state":"start","mode":"ace/mode/javascript"}},"timestamp":1690447212306}