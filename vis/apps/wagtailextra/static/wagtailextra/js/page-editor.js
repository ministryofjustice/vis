"use strict";

function makeAndConfigureRichTextEditable(id, plugins) {
    function disableShortcuts(e){
       var ret=true;
        if(e.ctrlKey || e.metaKey){
            switch(e.keyCode){
                case 66: //ctrl+B or ctrl+b
                case 98: ret=false;
                         break;
                case 73: //ctrl+I or ctrl+i
                case 105: ret=false;
                          break;
                case 85: //ctrl+U or ctrl+u
                case 117: ret=false;
                          break;
            }
        }
        return ret;
    }

    var input = $('#' + id);
    var richText = $('<div class="richtext"></div>').html(input.val());
    richText.insertBefore(input);
    richText.on('keydown', disableShortcuts);
    input.hide();

    var removeStylingPending = false;
    function removeStyling() {
        /* Strip the 'style' attribute from spans that have no other attributes.
        (we don't remove the span entirely as that messes with the cursor position,
        and spans will be removed anyway by our whitelisting)
        */
        $('span[style]', richText).filter(function() {
            return this.attributes.length === 1;
        }).removeAttr('style');
        removeStylingPending = false;
    }

    richText.hallo({
        toolbar: 'halloToolbarFixed',
        toolbarCssClass: (input.closest('.object').hasClass('full')) ? 'full' : '',
        plugins: plugins
    }).bind('hallomodified', function(event, data) {
        input.val(data.content);
        if (!removeStylingPending) {
            setTimeout(removeStyling, 100);
            removeStylingPending = true;
        }
    }).bind('paste', function(event, data) {
        setTimeout(removeStyling, 1);
    });
}
