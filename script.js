// HTMLの読み込みが完了してから実行
document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.getElementById("menu-btn");
    const navbar = document.getElementById("navbar");

    // ボタンがクリックされた時の処理
    menuBtn.addEventListener("click", () => {
        // navbarに "show" クラスを付け外しする
        navbar.classList.toggle("show");
    });
});
