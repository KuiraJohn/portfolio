document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
 
    function getCSRFToken() {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith('csrftoken=')) {
                return cookie.substring('csrftoken='.length, cookie.length);
            }
        }
        return '';
    }
 
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone_number: document.getElementById('phone_number').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value
    };
 
    console.log(formData);
 
    fetch('/contactme/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Get CSRF token from cookies
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message); // Show success message
        } else {
            alert('Error: ' + JSON.stringify(data.errors)); // Show errors
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error submitting form');
    });
});