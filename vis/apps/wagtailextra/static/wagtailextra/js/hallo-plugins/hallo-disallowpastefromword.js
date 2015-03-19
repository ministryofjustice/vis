(function(jQuery) {
  return jQuery.widget('IKS.disallowpastefromword', {
    _create: function() {
      var editor = this.element;
      var isWordContent = function(content) {
        return (
        (/<font face="Times New Roman"|class="?Mso|style="[^"]*\bmso-|style='[^'']*\bmso-|w:WordDocument/i).test(content) ||
        (/class="OutlineElement/).test(content) ||
        (/id="?docs\-internal\-guid\-/.test(content))
        );
      };
      return editor.bind('paste', this, (function(_this) {
        return function(event) {
          var lastContent;
          lastContent = editor.html();
          return setTimeout(function() {
            var pasted;
            pasted = editor.html();
            if (isWordContent(pasted)) {
              alert('Pasting content from Microsoft Word has been disallowed because'+
              ' it causes problems with formatting on the web.');
              editor.html(lastContent);
            }
          }, 4);
        };
      })(this));
    }
  });
})(jQuery);

