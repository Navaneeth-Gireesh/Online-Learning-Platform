// JavaScript to show the loader during page transitions
window.addEventListener('beforeunload', function () {
    document.getElementById('loader').style.display = 'block'; // Show loader
});

window.addEventListener('load', function () {
    document.getElementById('loader').style.display = 'none'; // Hide loader once the new page is loaded
});
