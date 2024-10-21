function loadVideo(videoUrl, posterUrl) {
    const videoPlayer = document.querySelector('.video-player');
    const videoSource = document.getElementById('videoSource');

    // Log the video and poster URLs for debugging
    console.log("Loading video:", videoUrl);
    console.log("Setting poster:", posterUrl);

    // Set the poster image
    videoPlayer.setAttribute('poster', posterUrl);

    // Load the video source
    videoSource.src = videoUrl;
    videoPlayer.load(); // Load the new source

    // Play the video after a short delay for better user experience
    setTimeout(() => {
        videoPlayer.play();
    }, 500); // Adjust time as necessary
}

function toggleContent(element) {
    const nextElement = element.nextElementSibling;
    const arrow = element.querySelector('.arrow');

    // Toggle the display of the sub-sections and arrow direction
    if (nextElement.style.display === 'none' || nextElement.style.display === '') {
        nextElement.style.display = 'block';
        arrow.innerHTML = '&#9650;'; // Up arrow
    } else {
        nextElement.style.display = 'none';
        arrow.innerHTML = '&#9660;'; // Down arrow
    }
}

function toggleTrailers() {
    const trailersContainer = document.querySelector('.trailers-container');
    trailersContainer.style.display = trailersContainer.style.display === 'none' ? 'block' : 'none';
}

function toggleSubContent(element) {
    const quizzes = element.nextElementSibling; // Quizzes div
    const videos = quizzes.nextElementSibling; // Videos div
    const arrow = element.querySelector('.arrow');

    // Toggle visibility of quizzes and videos
    const quizzesVisible = quizzes.style.display === 'block';
    const videosVisible = videos.style.display === 'block';

    quizzes.style.display = quizzesVisible ? 'none' : 'block';
    videos.style.display = videosVisible ? 'none' : 'block';

    // Update arrow direction based on visibility
    arrow.innerHTML = (quizzes.style.display === 'block' || videos.style.display === 'block') ? 
                      '&#9650;' : '&#9660;'; // Up or Down arrow
}
