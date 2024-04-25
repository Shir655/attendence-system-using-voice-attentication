// document.getElementById("contact-form").addEventListener("submit", function(event) {
//     event.preventDefault(); // Prevent default form submission

//     // Get form data
//     var formData = new FormData(this);

//     // Send form data to the server
//     fetch("send_email.php", {
//         method: "POST",
//         body: formData
//     })
//     .then(response => {
//         if (response.ok) {
//             return response.text(); // If response is successful, return the response text
//         }
//         throw new Error("Network response was not ok.");
//     })
//     .then(data => {
//         console.log(data); // Log the response data
//         // You can display a success message or perform other actions here
//     })
//     .catch(error => {
//         console.error("There was a problem with the fetch operation:", error);
//         // Handle errors here
//     });
// });



// document.getElementById("loginForm").addEventListener("submit", function(event) {
//     event.preventDefault(); // Prevent form submission
    
//     // Get input values
//     var email = document.getElementById("email").value;
//     var password = document.getElementById("password").value;

//     // Example of login validation logic
//     if (email === "example@example.com" && password === "password") {
//         // Redirect to the attendance system page if login is successful
//         window.location.href = "index.html";
//     } else {
//         // Show error message if login fails
//         alert("Invalid email or password. Please try again.");
//     }
// });