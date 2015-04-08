(function() {
  (function($) {
    return $.widget("IKS.externallink", {
      options: {
        uuid: '',
        editable: null
      },
      getEnclosingLink: function() {
        var node = this.options.editable.getSelection().commonAncestorContainer;
        return $(node).parents('a').get(0);
      },
      hasExternalRelAttr: function() {
        var enclosingLink = this.getEnclosingLink();
        var attr = $(enclosingLink).attr('rel');

        if (typeof attr !== typeof undefined && attr !== false && attr === 'external') {
          return true;
        }
        return false;
      },
      populateToolbar: function(toolbar) {
        var widget = this;
        var button = $('<span></span>');

        button.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'External link',
          icon: 'icon-redirect',
          command: null,
          queryState: function(event) {
            return button.hallobutton('checked', widget.hasExternalRelAttr());
          }
        });

        toolbar.append(button);

        button.on('click', function(event) {
          var enclosingLink = widget.getEnclosingLink();

          if (enclosingLink) {
            if (widget.hasExternalRelAttr()) {
              $(enclosingLink).removeAttr('rel');
              return widget.options.editable.element.trigger('change');
            } else {
              $(enclosingLink).attr('rel', 'external');
              return widget.options.editable.element.trigger('change');
            }
          } else {
            return;
          }
        });
      }
    });
  })(jQuery);

}).call(this);
