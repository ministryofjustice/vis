(function () {
  'use strict';

  vis.Modules.mobileMenu = {
    selector: '.js-mobileMenuToggle',

    init: function () {
      _.bindAll(this, 'toggleClick');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$toggle = $(this.selector);
      this.$menu = $(this.$toggle.data('target'));
    },

    bindEvents: function () {
      this.$toggle.on('click', this.toggleClick);
    },

    toggleClick: function (evt) {
      evt.preventDefault();

      this.$toggle.toggleClass('is-open');
      this.$menu.toggleClass('is-open');
    }
  };

}());
