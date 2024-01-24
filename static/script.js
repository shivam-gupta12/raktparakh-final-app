// script.js

console.log("This is javascript code")
var hidden = true

// document.querySelectorAll('.open-cam').forEach(function (btn) {
//     btn.addEventListener('click', function () {
//         capturePhoto();
//     });
// });

// function capturePhoto() {
//     // Access the user's camera
//     navigator.mediaDevices.getUserMedia({ video: true })
//         .then(function (stream) {
//             // Create a video element to display the camera feed
//             var video = document.createElement('video');
//             document.body.appendChild(video);

//             // Set the width and height of the video element
//             video.width = 0.5 * window.innerWidth;  // 50vw
//             video.height = 0.4 * window.innerHeight;  // 40vw

//             video.srcObject = stream;
//             video.play();

//             // Create a canvas to capture the photo
//             var canvas = document.getElementById('canvas');
//             var context = canvas.getContext('2d');

//             // Capture a photo after 2 seconds (adjust as needed)
//             setTimeout(function () {
//                 context.drawImage(video, 0, 0, video.width, video.height);
//                 // Stop the camera stream
//                 stream.getTracks().forEach(track => track.stop());

//                 // Convert the canvas content to base64 data URL
//                 var imageDataURL = canvas.toDataURL('image/png');

//                 // Pass the captured image data to a function to submit to the server
//                 submitPhoto(imageDataURL);

//                 document.querySelectorAll('.open-cam').forEach(function (btn) {
//                     btn.innerText = "Uploaded"
//                 });

//             }, 10000);
//         })
//         .catch(function (error) {
//             console.error('Error accessing camera: ', error);
//         });
// }

// function submitPhoto(imageDataURL) {
//     // Send the captured image data to the server using an AJAX request
//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/upload', true);
//     xhr.setRequestHeader('Content-Type', 'application/json');

//     xhr.onreadystatechange = function () {
//         if (xhr.readyState == 4 && xhr.status == 200) {
//             console.log('Image submitted successfully');
//         }
//     };

//     xhr.send(JSON.stringify({ image: imageDataURL }));
// }

document.querySelectorAll('.predictBtn').forEach(function (btn) {
    btn.addEventListener('click', function () {
        var contentDiv = document.querySelector('.hidden');
        contentDiv.classList.add("prediction");
        }
    )}
);