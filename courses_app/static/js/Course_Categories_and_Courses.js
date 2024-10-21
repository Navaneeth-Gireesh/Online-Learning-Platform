document.addEventListener('DOMContentLoaded', function() {
    function setButtonHeight() {
        const courseItems = document.querySelectorAll('.course-item');
        if (courseItems.length > 0) {
            const courseItemHeight = courseItems[0].offsetHeight;
            document.documentElement.style.setProperty('--button-height', `${courseItemHeight}px`);
        }
    }

    function toggleButtonsVisibility() {
        document.querySelectorAll('.courses-slider').forEach(slider => {
            const coursesList = slider.querySelector('.courses-list');
            const courseItems = coursesList.querySelectorAll('.course-item');
            const leftBtn = slider.querySelector('.left-btn');
            const rightBtn = slider.querySelector('.right-btn');
            
            if (courseItems.length > 3) {
                leftBtn.style.display = 'block';
                rightBtn.style.display = 'block';
            } else {
                leftBtn.style.display = 'none';
                rightBtn.style.display = 'none';
            }
        });
    }

    // Set initial button height and visibility
    setButtonHeight();
    toggleButtonsVisibility();

    // Adjust button height and visibility on window resize
    window.addEventListener('resize', function() {
        setButtonHeight();
        toggleButtonsVisibility();
    });
});

// Function to scroll the courses container
function scrollCourses(direction, categoryId) {
    const container = document.getElementById('courses-list-' + categoryId);
    if (container) {
        const scrollAmount = container.offsetWidth / 1; // Adjust this value to control the scroll amount based on visible courses
        if (direction === 'right') {
            container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        } else {
            container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        }
    }
}
