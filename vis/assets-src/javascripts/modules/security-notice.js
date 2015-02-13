(function () {
  'use strict';

  vis.Modules.securityNotice = {
    selector: '.security-banner',
    closeSelector: '.close-link',
    storageKey: 'securityDisabled',

    init: function () {
      _.bindAll(this, 'render', 'closeClick');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$el = $(this.selector);
      this.$body = $('body');
      this.$close = this.$el.find(this.closeSelector);
    },

    bindEvents: function () {
      this.$close.on('click', this.closeClick);
      vis.Events.on('render', this.render);
    },

    closeClick: function (evt) {
      evt.preventDefault();
      localStorage.setItem(this.storageKey, true);
      this.$el.remove();
    },

    isDisabled: function () {
      return localStorage.getItem(this.storageKey);
    },

    reset: function () {
      localStorage.clear();
    },

    render: function () {
      if (this.isDisabled()) {
        this.$el.remove();
      }
    }
  };

}());
