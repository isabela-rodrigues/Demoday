const navSlide = () => {
    const menu = document.querySelector('.menu');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');


    menu.addEventListener('click', () => {
        //tooggle nav
        nav.classList.toggle('nav-active');

        //animate links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = ' navLinkFade 0.5 ease forwards ${index / 7 = 1.5} s';
                console.log(index / 7);
            }

        });

        //menu animation
        menu.classList.toggle('toggle');
    });
}

navSlide();