$(document).ready(function () {

    // Materialize version 1.0.0 JS
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.sidenav').sidenav();

    // get current year
    var currYear = (new Date()).getFullYear();

    $('.datepicker').datepicker({
        defaultDate: currYear,
        format: "dd/mm/yyyy"
    });


})
