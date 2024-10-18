// Function to update user activity
function updateActivity() {
    fetch('/update_activity', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        if (data.status !== 'success') {
            console.error('Failed to update activity');
        }
    })
    .catch(error => {
        console.error('Error updating activity:', error);
    });
}

// Update activity every 10 seconds
let interval = setInterval(updateActivity, 10000);

// Also update when the page loads
document.addEventListener('DOMContentLoaded', updateActivity);

// Clear interval when page is unloaded
window.addEventListener('beforeunload', () => {
    clearInterval(interval);
    updateActivity(); // One final update before leaving
});