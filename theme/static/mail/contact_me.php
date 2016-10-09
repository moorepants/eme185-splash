<?php

if(!defined('STDOUT')) define('STDOUT', fopen('php://stdout', 'w'));

// Check for empty fields
if(empty($_POST['name']) ||
   empty($_POST['org']) ||
   empty($_POST['email']) ||
   empty($_POST['phone']) ||
   empty($_POST['title']) ||
   empty($_POST['message']) ||
   !filter_var($_POST['email'],FILTER_VALIDATE_EMAIL))
   {
   echo "No arguments Provided!";
   return false;
   }

$name = $_POST['name'];
$org = $_POST['org'];
$email_address = $_POST['email'];
$phone = $_POST['phone'];
$title = $_POST['title'];
$message = $_POST['message'];

//Get the uploaded file information
$name_of_uploaded_file = basename($_FILES['file']['name']);

//get the file extension of the file
$type_of_uploaded_file =
    substr($name_of_uploaded_file,
    strrpos($name_of_uploaded_file, '.') + 1);

$size_of_uploaded_file =
    $_FILES["file"]["size"]/1024;//size in KBs

//Settings
$max_allowed_file_size = 5000; // size in KB
$allowed_extensions = array("txt", "rst", "md", "pdf", "odt", "doc", "docx");

$errors = "";

//Validations
if($size_of_uploaded_file > $max_allowed_file_size )
{
  $errors .= "\n Size of file should be less than $max_allowed_file_size";
}

//------ Validate the file extension -----
$allowed_ext = false;
for($i=0; $i<sizeof($allowed_extensions); $i++)
{
  if(strcasecmp($allowed_extensions[$i],$type_of_uploaded_file) == 0)
  {
    $allowed_ext = true;
  }
}

if(!$allowed_ext)
{
  $errors .= "\n The uploaded file is not supported file type. ".
  " Only the following file types are supported: ".implode(',',$allowed_extensions);
}

//copy the temp. uploaded file to uploads folder
$home = getenv("HOME");
$upload_folder = "$home/eme185-uploads/";
if (!file_exists($upload_folder)) {
    mkdir($upload_folder, 0777, true);
}
$path_of_uploaded_file = $upload_folder . $name_of_uploaded_file;
$tmp_path = $_FILES["file"]["tmp_name"];
 
if(is_uploaded_file($tmp_path))
{
  if(!copy($tmp_path,$path_of_uploaded_file))
  {
    $errors .= '\n error while copying the uploaded file';
  }
}

// Create the email and send the message
// Add your email address inbetween the '' replacing yourname@yourdomain.com - This is where the form will send a message to.
$to = 'jkm@ucdavis.edu';
$email_subject = "[MECH-CAP Proposal]:  $name, $org";
$email_body = <<<EOT
  You have received a new message from your website contact form.\n\n
  Here are the details:\n\n
  Name: $name\n\n
  Organization: $org\n\n
  Email: $email_address\n\n
  Phone: $phone\n\n
  Title: $title\n\n
  Message:\n$message
  Attachment:\n$name_of_uploaded_file
EOT;

require 'PHPMailerAutoload.php';
//Create a new PHPMailer instance
$mail = new PHPMailer;
// Set PHPMailer to use the sendmail transport
$mail->isSendmail();
//Set who the message is to be sent from
$mail->setFrom('noreply@ucdavis.edu', 'MECHCAP Website');
//Set an alternative reply-to address
$mail->addReplyTo($email_address, $name);
//Set who the message is to be sent to
$mail->addAddress($to, 'Jason K. Moore');
//Set the subject line
$mail->Subject = $email_subject;
$mail->Body = $email_body;
$mail->AltBody = $email_body;
//Attach an image file
$mail->addAttachment($path_of_uploaded_file);
//send the message, check for errors
if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
}

return true;
?>
