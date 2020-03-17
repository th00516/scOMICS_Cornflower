/*jQuery*/

$(document).ready(function () {

    $("#year").html(function () {

        const thisYear = new Date();

        return thisYear.getFullYear();

    });

});