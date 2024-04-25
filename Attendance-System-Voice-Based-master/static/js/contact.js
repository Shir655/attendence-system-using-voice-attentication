// Get the form elements
const form = document.getElementById('contact-form');
const email = document.getElementById('email');
const message = document.getElementById('message');
// Get the close button element
const closeButton = document.querySelector('.icon-close');

// Add event listener for click event
closeButton.addEventListener('click', function() {
    // Redirect to the front page
    window.location.href = './';
});


// Function to validate email
function validateEmail(email) {
    const regex = /\S+@\S+\.\S+/;
    return regex.test(email);
}

// Function to handle form submission
function handleSubmit(event) {
    event.preventDefault();

    // Check if email is valid
    if (!validateEmail(email.value)) {
        alert('Please enter a valid email address');
        email.focus();
        return false;
    }

    // Check if message is empty
    if (message.value.trim() === '') {
        alert('Please enter your message');
        message.focus();
        return false;
    }

    // Submit the form if validation passes
    alert('Message sent successfully!');
    form.reset();
}

// Event listener for form submission
form.addEventListener('submit', handleSubmit);

