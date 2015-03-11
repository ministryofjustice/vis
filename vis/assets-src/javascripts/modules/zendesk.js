(function () {
  'use strict';

  vis.Modules.zendesk = {
    selector: '.js-Zendesk',
    successTemplate: vis.templatizer.Zendesk.success(),
    errorTemplate: vis.templatizer.Zendesk.error(),

    init: function () {
      _.bindAll(this, 'render', 'submit', 'feedbackSuccess', 'feedbackFail');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$form = $(this.selector);
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
      this.$form.replaceWith(this.successTemplate);
    },

    feedbackFail: function (resp) {
      this.$form.find('.Error').remove();
      this.$form.prepend(this.errorTemplate);
      this.$submitBtn.prop('disabled', false);
    },

    submit: function (evt) {
      evt.preventDefault();
      this.$submitBtn.prop('disabled', true);
      this.sendFeedback(this.$form.serialize());
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
