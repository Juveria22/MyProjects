const API_URL = "http://127.0.0.1:8000/chat"; //Local FastAPI endpoint 
const session_id = "user_" +Math.floor(Math.random()* 10000); //Temp user session

//toggle shows chatbot UI on the right hand side 
function toggleChat(){
    const chat = document.getElementById("chatWidget");
    chat.style.display = chat.style.display === "flex"? "none": "flex"; 
} 

//Allows user to press enter to send their query 
document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

//appending the chat to the chatbox
//makes a bubble in ur chatbox ui and auto scrolls down as more messages are sent 
function appendMessage(role, text) {
    const box = document.getElementById("chatBody"); // was chatBox
    const msg = document.createElement("div");
    msg.innerHTML = `<strong>${role}:</strong> ${text}`;
    msg.style.margin = "6px 0";
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight; 
}


async function sendMessage(){
    const input = document.getElementById("userInput");
    const text = input.value.trim(); 
    if(!text) return;

    appendMessage("You", text); 
    input.value = "";

    try{
        const res = await fetch(API_URL, {
            method: "POST",
            headers: {"Content-Type":  "application/json"},
            body: JSON.stringify({ session_id, query: text}),
        });

        const data = await res.json();
        appendMessage("Bot", data.response);
    }catch(err) {
        appendMessage("Bot", "Oops! Something went wrong."); 
    }
}