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
      if (this.hasLocalStorage()) {
        localStorage.setItem(this.storageKey, true);
      }
      this.$banner.remove();
    },

    hasLocalStorage: function () {
      var test = 'test';
      try {
        localStorage.setItem(test, test);
        localStorage.removeItem(test);
        return true;
      } catch (e) {
        return false;
      }
    },

    isDisabled: function () {
      if (this.hasLocalStorage()) {
        return localStorage.getItem(this.storageKey);
      }
      return false;
    },

    reset: function () {
      if (this.hasLocalStorage()) {
        localStorage.clear();
      }
    },

    render: function () {
      if (this.isDisabled()) {
        this.$banner.remove();
      }
    }
  };

}());
