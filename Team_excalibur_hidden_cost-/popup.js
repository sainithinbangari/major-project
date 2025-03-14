// popup.js

document.addEventListener('DOMContentLoaded', async function () {
    const user = JSON.parse(localStorage.getItem('user'));
    const welcomeMessage = document.getElementById('welcome-message');
    const logoutButton = document.getElementById('logout-button');

    if (user) {
        // Fetch username from Firestore using the email stored in localStorage
        const userDoc = await db.collection("users").doc(user.email).get();

        if (userDoc.exists) {
            const username = userDoc.data().username; // Fetch the username
            welcomeMessage.innerHTML = `<img src="D:/GitHub/Team_excalibur_hidden_cost-main/Team_excalibur_hidden_cost-/hi-there.gif" alt="Welcome" style="width: 30px; height: 30px;"> ${username}`; // Display username with GIF
        } else {
            welcomeMessage.innerHTML = `<img src="D:/GitHub/Team_excalibur_hidden_cost-main/Team_excalibur_hidden_cost-/hi-there.gif" alt="Welcome" style="width: 30px; height: 30px;"> User`; // Fallback if no username found
        }

        logoutButton.style.display = 'block';
    } 
    // Logout functionality
    logoutButton.addEventListener('click', function () {
        firebase.auth().signOut().then(() => {
            localStorage.removeItem('user'); // Clear user session
             // Redirect to login page
        }).catch((error) => {
            console.error('Error during logout:', error);
            alert("Error during logout: " + error.message);
        });
    });

    // Existing code for submitUrl button
    document.getElementById('submitUrl').addEventListener('click', function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            const url = tabs[0].url;
            chrome.runtime.sendMessage({ action: 'openNewTab', url: url });
        });
    });
});


