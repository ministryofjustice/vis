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
      this.$subject = this.$form.find('[name="subject"]');
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
      if (typeof ga === 'function') {
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
      var errors = [];

      if (this.$feedback.val() === '') {
        errors.push('Your comment cannot be blank');
      }

      if (this.$subject.val() !== '') {
        errors.push('Subject must be blank. We use this to prevent spam.');
      }

      if (errors.length === 0) {
        this.$form.find('.Error-summary').remove();
        return true;
      } else {
        this.setErrors(errors);
        return false;
      }
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
