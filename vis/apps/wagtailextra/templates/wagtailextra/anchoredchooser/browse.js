function(modal) {
    $('a.navigate-pages, .link-types a', modal.body).click(function() {
        modal.loadUrl(this.href);
        return false;
    });

    {% include 'wagtailextra/anchoredchooser/_search_behaviour.js' %}
}
