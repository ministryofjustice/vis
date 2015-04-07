(function () {
  'use strict';

  vis.Modules.zendesk = {
    selector: '.js-Zendesk',
    successTemplate: vis.templatizer.Zendesk.success,
    failTemplate: vis.templatizer.Zendesk.fail,
    errorsTemplate: vis.templatizer.Zendesk.errors,

    init: function () {
      _.bindAll(this, 'render', 'submit', 'feedbackSuccess', 'feedbackFail');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$form = $(this.selector);
      this.$feedback = this.$form.find('[name="comments"]');
      this.$submitBtn = this.$form.find('button[type="submit"]');
    },

    bindEvents: function () {
      this.$form.on('submit', this.submit);
      vis.Events.on('render', this.render);
    },

    sendFeedback: function (data) {
      $.post(this.$form.attr('action'), data)
        .done(this.feedbackSuccess)
        .error(this.feedbackFail);
    },

    feedbackSuccess: function (resp) {
      if (typeof ga === "function") {
        ga('send', {
          'hitType': 'event',
          'eventCategory': 'feedback',
          'eventAction': 'sent'
        });
      }
      this.$form.replaceWith(this.successTemplate());
    },

    feedbackFail: function (resp) {
      this.setErrors(['There was an error submitting the form, please try again']);
    },

    setErrors: function (errors) {
      this.$form.find('.Error-summary').remove();
      this.$form.prepend(this.errorsTemplate({ errors: errors }));
      this.$submitBtn.prop('disabled', false);
    },

    isValid: function () {
      if (this.$feedback.val() === '') {
        this.setErrors(['Your comment cannot be blank']);
        return false;
      }
      this.$form.find('.Error-summary').remove();
      return true;
    },

    submit: function (evt) {
      evt.preventDefault();
      this.$submitBtn.prop('disabled', true);

      if (this.isValid()) {
        this.sendFeedback(this.$form.serialize());
      } else {
        this.$submitBtn.prop('disabled', false);
      }
    },

    render: function () {
      $('<input/>', {
        name: 'user_agent',
        type: 'hidden',
        value: navigator.userAgent
      }).prependTo(this.$form);

      $('<input/>', {
        name: 'url',
        type: 'hidden',
        value: window.location.href
      }).prependTo(this.$form);
    }
  };

}());
