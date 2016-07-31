
$(document).ready(function () {
    //Dojobeheer menufunctie
    $('#events').hide();
    $('#trainings').hide();
    $('#competitions').hide();
    $('#dojo-management-first-button').click(function () {
        event.preventDefault();
        $('#members').show();
        $('#events').hide();
        $('#trainings').hide();
        $('#competitions').hide();
    });
    $('#dojo-management-second-button').click(function () {
        event.preventDefault();
        $('#members').hide();
        $('#events').show();
        $('#trainings').hide();
        $('#competitions').hide();
    });
    $('#dojo-management-third-button').click(function () {
        event.preventDefault();
        $('#members').hide();
        $('#events').hide();
        $('#trainings').show();
        $('#competitions').hide();
    });
    $('#dojo-management-fourth-button').click(function () {
        event.preventDefault();
        $('#members').hide();
        $('#events').hide();
        $('#trainings').hide();
        $('#competitions').show();
    });

    //Ledenlijst togglefunctie
    $('.member-entry-name').click(function () {
        event.preventDefault();
        $(this).parent().find('.member-entry-info').stop(true, true).slideToggle(400);
    });

    //Toevoegen van lid togglefunctie
    $('#add-member-button').click(function () {
        event.preventDefault();
        $('#add-member-form-wrap').stop(true, true).slideToggle(400);
    });
});