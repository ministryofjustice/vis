(function () {
  'use strict';

  vis.Modules.zendesk = {
    selector: '.js-Zendesk',
    successTemplate: '<div class="Feedback-success"><h2>Thank you for your help.</h2><p>Your feedback has been sent and will be picked up by one of our team.</p></div>',
    errorTemplate: '<p class="Error">There was an error submitting the form, please try again.</p>',

    init: function () {
      _.bindAll(this, 'submit', 'feedbackSuccess', 'feedbackFail');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$form = $(this.selector);
    },

    bindEvents: function () {
      this.$form.on('submit', this.submit);
    },

    sendFeedback: function (formData) {
      var jqXHR = $.ajax({
        method: 'POST',
        url: this.$form.attr('action'),
        data: formData,
        processData: false,
        contentType: false,
        headers: {'X-Requested-With': 'XMLHttpRequest'}
      })
      .done(this.feedbackSuccess)
      .error(this.feedbackFail);
    },

    feedbackSuccess: function (resp) {
      this.$form.replaceWith(this.successTemplate);
    },

    feedbackFail: function (resp) {
      this.$form.find('.Error').remove();
      this.$form.prepend(this.errorTemplate);
    },

    submit: function(evt){
      evt.preventDefault();

      var formData = new FormData(this.$form[0]);
      formData.append('user_agent', window.navigator.userAgent);
      formData.append('url', window.location.href);

      this.sendFeedback(formData);
    }
  };

}());
