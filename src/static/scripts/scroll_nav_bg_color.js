

    // Change navbar color on scroll
    window.addEventListener('scroll', function () {
        var navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.backgroundColor = 'rgba(34, 34, 34, 0.7)';
        } else {
            navbar.style.backgroundColor = 'transparent'; // Change to your initial color
        }
    });
