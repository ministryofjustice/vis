modal.ajaxifyForm($('form.search-form', modal.body));

var searchUrl = $('form.search-form', modal.body).attr('action');

function search() {
    $.ajax({
        url: searchUrl,
        data: {q: $('#id_q', modal.body).val(), 'results_only': true},
        success: function(data, status) {
            $('.page-results', modal.body).html(data);
            ajaxifySearchResults();
        }
    });
    return false;
}

$('#id_q', modal.body).on('input', function() {
    clearTimeout($.data(this, 'timer'));
    var wait = setTimeout(search, 200);
    $(this).data('timer', wait);
});

function showHideResults(show) {
    if (show) {
        $('#choosen-result').show();
        $('#chooser').hide();
    } else {
        $('#choosen-result').hide();
        $('#chooser').show();
    }
}

function ajaxifySearchResults() {

    $('a.choose-page', modal.body).click(function() {
        showHideResults(true);

        var data = $(this).data();
        $('#id_choosen-page').data(data).val(data.title);
    });

    $('a.cancel-choosen', modal.body).click(function() {
        showHideResults();
    });

    $('#choosen-result form', modal.body).submit(function() {
        var pageData = $('#id_choosen-page').data();
        var anchor = $('#id_anchor').val();

        pageData.anchor = anchor;
        pageData.parentId = {{ parent_page.id }};
        modal.respond('pageChosen', pageData);
        modal.close();

        return false;
    });

    showHideResults();
}

ajaxifySearchResults();
$('#id_q', modal.body).focus();
