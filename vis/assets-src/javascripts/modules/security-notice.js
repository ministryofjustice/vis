(function () {
  'use strict';

  vis.Modules.securityNotice = {
    selector: '.js-SecurityExit',
    storageKey: 'securityDisabled',

    init: function () {
      _.bindAll(this, 'render', 'closeClick');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$btn = $(this.selector);
      this.$banner = $(this.$btn.data('banner'));
    },

    bindEvents: function () {
      this.$btn.on('click', this.closeClick);
      vis.Events.on('render', this.render);
    },

    closeClick: function (evt) {
      evt.preventDefault();
      localStorage.setItem(this.storageKey, true);
      this.$banner.remove();
    },

    isDisabled: function () {
      return localStorage.getItem(this.storageKey);
    },

    reset: function () {
      localStorage.clear();
    },

    render: function () {
      if (this.isDisabled()) {
        this.$banner.remove();
      }
    }
  };

}());
