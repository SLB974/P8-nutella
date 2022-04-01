/*!
* Start Bootstrap - Creative v7.0.5 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }
    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

    const NutriA = '#0e8c4f';
    const NutriB ='#7ec247';
    const NutriC ='#fbcb29';
    const NutriD ='#fb7f1d';
    const NutriE ='#f13c1d';
    const badges = document.body.querySelectorAll('#pscore');
    
    var Nutriscore = function (element) {
        var color = ''
        switch (element.textContent) {
            case 'A':
                color = NutriA;
                enability = false;
                break;
            case 'B':
                color= NutriB;
                break;
            case 'C':
                color= NutriC;
                break;
            case 'D':
                color= NutriD;
                break;
            case 'E':
                color= NutriE;
        }
        element.style.backgroundColor = color;
        element.parentNode.style.backgroundColor = color;
        element.parentNode.parentNode.style.backgroundColor = color;
    };
    
    badges.forEach(Nutriscore);
});
