const burger = document.getElementById('burger');
const nav = document.getElementById('nav');
const submenuToggle = document.getElementById('submenu-toggle');
const submenu = document.getElementById('submenu');

if (burger && nav) {
	burger.addEventListener('click', () => {
	    burger.classList.toggle('active');
	    nav.classList.toggle('active');
	});
}


if (submenuToggle && submenu) {
	submenuToggle.addEventListener('click', (e) => {
		e.preventDefault();
	    submenu.classList.toggle('open');
	});
}
