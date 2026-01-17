const labArea = document.getElementById("labArea");
const explanation = document.getElementById("explanationText");
const tabs = document.querySelectorAll(".tab");
const leftPanel = document.getElementById("leftPanel");

/* Utility */
function setActiveTab(tabClass) {
    tabs.forEach(tab => tab.classList.remove("active"));
    document.querySelector(tabClass).classList.add("active");
}

/* LOGIN LAB */
function loadLoginLab() {
    setActiveTab(".login-tab");

    leftPanel.className = "left-panel login-theme";

    labArea.innerHTML = `
        <h2>Login Lab</h2>
        <input type="text" id="username" placeholder="Username">
        <input type="password" id="password" placeholder="Password">
        <button onclick="submitLogin()">Login</button>
        <div id="result"></div>
    `;

    explanation.innerHTML = "Try SQL injection payloads like <code>' OR '1'='1</code>";
}

function submitLogin() {
    const u = document.getElementById("username").value;
    const p = document.getElementById("password").value;
    const result = document.getElementById("result");

    if (u.includes("'") || p.includes("'")) {
        result.innerHTML = "⚠️ Possible SQL Injection detected";
        result.style.color = "red";

        explanation.innerHTML = `
        <strong>Attack:</strong> SQL Injection<br><br>
        Special characters modify SQL queries, potentially bypassing authentication.<br><br>
        <strong>Impact:</strong> Unauthorized access to accounts or databases.
        `;
    } else {
        result.innerHTML = "❌ Login failed";
        result.style.color = "black";
        explanation.innerHTML = "No malicious pattern detected.";
    }
}

/* COMMENT LAB */
function loadCommentLab() {
    setActiveTab(".comment-tab");

    leftPanel.className = "left-panel comment-theme";

    labArea.innerHTML = `
        <h2>Comment Lab</h2>
        <textarea id="comment" placeholder="Write a comment..."></textarea>
        <button onclick="submitComment()">Post</button>
        <div id="result"></div>
    `;

    explanation.innerHTML = "Try XSS payloads like <code>&lt;script&gt;alert(1)&lt;/script&gt;</code>";
}


function submitComment() {
    const c = document.getElementById("comment").value;
    const result = document.getElementById("result");

    if (c.includes("<script>")) {
        result.innerHTML = "⚠️ Potential XSS detected";
        result.style.color = "red";

        explanation.innerHTML = `
        <strong>Attack:</strong> Cross-Site Scripting (XSS)<br><br>
        Injected scripts execute in victims’ browsers.<br><br>
        <strong>Impact:</strong> Session hijacking, defacement, data theft.
        `;
    } else {
        result.innerHTML = "💬 Comment posted";
        result.style.color = "green";
        explanation.innerHTML = "No malicious script detected.";
    }
}

/* LOAD DEFAULT LAB */
loadLoginLab();
