document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.getElementById("menu-btn");
    const navbar = document.getElementById("navbar");

    menuBtn.addEventListener("click", () => {
        // CSSで定義しているクラス名（active または show）に合わせてください
        navbar.classList.toggle("active");
    });
});
