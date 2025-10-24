// Optional JavaScript to scroll updates vertically
let index = 0;
function scrollUpdates() {
    const updates = document.querySelectorAll('.update');
    updates.forEach((u, i) => {
        u.style.display = i === index ? 'block' : 'none';
    });
    index = (index + 1) % updates.length;
}
setInterval(scrollUpdates, 2500);
window.onload = scrollUpdates;
