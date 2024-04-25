<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form data
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Set admin email
    $admin_email = "ranjeetsingh@kccemsr.edu.in"; // Replace with your admin email

    // Subject and email content
    $subject = "New message from contact form";
    $email_content = "Email: $email\n\nMessage:\n$message";

    // Send email to admin
    $headers = "From: $email";
    mail($admin_email, $subject, $email_content, $headers);

    // Send a response back to the user
    echo "Message sent successfully!";
} else {
    // If not submitted via POST method, redirect to the contact page
    header("Location: contact.html");
}
?>


