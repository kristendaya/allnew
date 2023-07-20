// Wait for the document to load
document.addEventListener("DOMContentLoaded", function () {
  // Get references to DOM elements
  const dashboardSection = document.getElementById("dashboardSection");
  const membersSection = document.getElementById("membersSection");
  const memberCount = document.getElementById("memberCount");
  const questionsSolvedCount = document.getElementById("questionsSolvedCount");
  const memberTableBody = document.getElementById("memberTableBody");
  const memberVisitChart = document.getElementById("memberVisitChart").getContext("2d");

  // Add event listeners to the navigation buttons
  const dashboardBtn = document.getElementById("dashboardBtn");
  dashboardBtn.addEventListener("click", function (event) {
    event.preventDefault();
    dashboardSection.style.display = "block";
    membersSection.style.display = "none";
    // Update dashboard data (e.g., total member count and questions solved count)
    updateDashboardData();
  });

  const membersBtn = document.getElementById("membersBtn");
  membersBtn.addEventListener("click", function (event) {
    event.preventDefault();
    dashboardSection.style.display = "none";
    membersSection.style.display = "block";
    // Load member data
    loadMemberData();
  });

  // Function to update dashboard data
  function updateDashboardData() {
    // Simulated data for demonstration purposes
    const totalMembers = 1234;
    const questionsSolved = 56789;

    memberCount.textContent = totalMembers;
    questionsSolvedCount.textContent = questionsSolved;
  }

  // Function to load member data
  function loadMemberData() {
    // Simulated data for demonstration purposes
    const members = [
      { name: "John Doe", email: "john@example.com", joinedDate: "2023-01-01", visits: 10 },
      { name: "Jane Smith", email: "jane@example.com", joinedDate: "2023-02-01", visits: 15 },
      // Add more member data as needed
    ];

    // Clear existing table rows
    memberTableBody.innerHTML = "";

    // Loop through the member data and generate table rows dynamically
    members.forEach(function (member) {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${member.name}</td>
        <td>${member.email}</td>
        <td>${member.joinedDate}</td>
      `;
      memberTableBody.appendChild(row);
    });

    // Generate member visit graph
    const memberNames = members.map(member => member.name);
    const memberVisits = members.map(member => member.visits);

    new Chart(memberVisitChart, {
      type: "bar",
      data: {
        labels: memberNames,
        datasets: [{
          label: "Number of Visits",
          data: memberVisits,
          backgroundColor: "rgba(54, 162, 235, 0.8)",
          borderColor: "rgba(54, 162, 235, 1)",
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            stepSize: 1
          }
        }
      }
    });
  }

  // Initial setup when the page loads
  dashboardSection.style.display = "block";
  membersSection.style.display = "none";
  updateDashboardData();
});
