document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.querySelector(".sidebar");
    const caretBtn = document.querySelector(".sidebar-btn i");
    const header = document.querySelector(".sidebar-header");

    caretBtn.addEventListener("click", function () {
        sidebar.classList.toggle("collapsed");

        if (sidebar.classList.contains("collapsed")) {
            header.innerHTML = '<img src="/app/static/images/dms.png"></img>';
            caretBtn.classList.remove("fa-caret-left");
            caretBtn.classList.add("fa-caret-right");
        } else {
            header.innerHTML = "<h1>Document</h1><h1>Management System</h1>";
            caretBtn.classList.remove("fa-caret-right");
            caretBtn.classList.add("fa-caret-left");
        }
    });
});