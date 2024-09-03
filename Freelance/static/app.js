// scripts.js
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('open-popup').onclick = function() {
        document.getElementById('popup').style.display = "block";
    }

    document.getElementById('open-signup-popup').onclick = function() {
        document.getElementById('signup-popup').style.display = "block";
    }
    
    document.getElementById('close-popup').onclick = function() {
        document.getElementById('popup').style.display = "none";
    }

    document.getElementById('close-signup-popup').onclick = function() {
        document.getElementById('signup-popup').style.display = "none";
    }
    
    // Close the pop-up if the user clicks anywhere outside of it
    window.onclick = function(event) {
        if (event.target == document.getElementById('popup')) {
            document.getElementById('popup').style.display = "none";
        }
    }

    window.onclick = function(event) {
        if (event.target == document.getElementById('signup-popup')) {
            document.getElementById('signup-popup').style.display = "none";
        }
    }
});
