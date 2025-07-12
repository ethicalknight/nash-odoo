// 🔐 Auto-fill current user if logged in
async function loadUserInfo() {
  const res = await fetch("/api/me");
  if (res.ok) {
    const user = await res.json();
    document.querySelector("#nav-profile").textContent = user.name || "Profile";
  }
}

// 🔍 Search Handler
async function searchUsers(query = "", filter = "") {
  const res = await fetch("/api/feed");
  const users = await res.json();
  const filtered = users.filter(u =>
    u.name.toLowerCase().includes(query.toLowerCase())
  );
  renderUserCards(filtered);
}

// 🧩 Render profile cards dynamically
function renderUserCards(users) {
  const container = document.querySelector("#user-feed");
  container.innerHTML = "";
  users.forEach(user => {
    const div = document.createElement("div");
    div.className = "profile-card";
    div.innerHTML = `
      <div>
        <p class="font-bold text-[#0F172A] text-sm">Name: ${user.name}</p>
        <p class="text-xs">Skills Offered: Cooking, Content Creation</p>
        <p class="text-xs">Skills Wanted: Cycling, Writing</p>
      </div>
      <div class="text-center">
        <div class="profile-pic"></div>
        <button class="skill-tag mt-2">Request</button>
      </div>
    `;
    container.appendChild(div);
  });
}

// 📤 Handle profile form submission
async function saveProfile(e) {
  e.preventDefault();
  const formData = new FormData(document.querySelector("#profileForm"));
  await fetch("/api/me", {
    method: "POST",
    body: formData,
  });
  alert("Profile Updated!");
}

// ⭐ Render skill selection UI
function setupSkillPicker() {
  const skills = document.querySelectorAll(".skill-pill");
  const selectedContainer = document.querySelector("#selectedSkills");

  skills.forEach(skill => {
    skill.addEventListener("click", () => {
      const label = skill.textContent;
      const span = document.createElement("span");
      span.className = "selected-skill";
      span.innerHTML = `${label}<span class="skill-x">x</span>`;
      span.querySelector(".skill-x").addEventListener("click", () => {
        span.remove();
      });
      selectedContainer.appendChild(span);
    });
  });
}

window.onload = () => {
  if (document.querySelector("#user-feed")) searchUsers();
  if (document.querySelector("#profileForm")) {
    document.querySelector("#profileForm").addEventListener("submit", saveProfile);
  }
  if (document.querySelector("#selectedSkills")) {
    setupSkillPicker();
  }
  loadUserInfo();
};
// 🌙 Toggle Dark Mode
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("toggle-dark");
  if (toggle) {
    toggle.addEventListener("click", () => {
      document.documentElement.classList.toggle("dark");
      localStorage.setItem("theme", document.documentElement.classList.contains("dark") ? "dark" : "light");
      toggle.textContent = document.documentElement.classList.contains("dark") ? "☀️ Light" : "🌙 Dark";
    });

    // Set on load
    const saved = localStorage.getItem("theme");
    if (saved === "dark") {
      document.documentElement.classList.add("dark");
      toggle.textContent = "☀️ Light";
    }
  }
});
