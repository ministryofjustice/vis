(function () {
  'use strict';

  vis.Modules.zendesk = {
    selector: 'form.Feedback-form',

    init: function () {
      _.bindAll(this, 'submit');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$form = $(this.selector);
    },

    bindEvents: function () {
      this.$form.on('submit', this.submit);
    },

    submit: function(evt){
      evt.preventDefault();
      var formData = new FormData(this.$form[0]);
      formData.append('user_agent', window.navigator.userAgent);
      formData.append('url', window.location.href);
      var jqXHR = $.ajax({
        method: 'POST',
        url: this.$form.attr('action'),
        data: formData,
        processData: false,
        contentType: false,
        headers: {'X-Requested-With': 'XMLHttpRequest'}
      });
      jqXHR.then(function (resp) {
          console.log(resp, 'should hide form');
      });
    }
  };

}());
