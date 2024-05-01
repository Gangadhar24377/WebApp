document.getElementById("openSidebarBtn").addEventListener("click", function() {
    document.querySelector(".sidebar").classList.add("show"); // Show sidebar
});

document.getElementById("closeSidebarBtn").addEventListener("click", function() {
    document.querySelector(".sidebar").classList.remove("show"); // Hide sidebar
});
