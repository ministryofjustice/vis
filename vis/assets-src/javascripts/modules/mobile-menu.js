(function () {
  'use strict';

  vis.Modules.mobileMenu = {
    selector: '.js-mobileMenuToggle',

    init: function () {
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$toggle = $(this.selector);
      this.$menu = $(this.$toggle.data('target'));
    },

    bindEvents: function () {
      this.$toggle.on('click', this.toggleClick.bind(this));
    },

    toggleClick: function (evt) {
      evt.preventDefault();

      this.$toggle.toggleClass('is-open');
      this.$menu.toggleClass('is-open');
    }
  };

}());
