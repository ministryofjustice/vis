(function () {
  'use strict';

  vis.Modules.mobileMenu = {
    selector: '.js-mobileMenuToggle',
    textSelector: '.js-mobileMenuToggleText',

    init: function () {
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$toggle = $(this.selector);
      this.$menuText = $(this.textSelector);
      this.$menu = $(this.$toggle.data('target'));
      this.$closedText = this.$menuText.text();
      this.$openText = this.$toggle.data('open-text');
    },

    bindEvents: function () {
      this.$toggle.on('click', this.toggleClick.bind(this));
    },

    toggleClick: function (evt) {
      evt.preventDefault();

      if (this.$toggle.hasClass('is-open')) {
        this.$menuText.text(this.$closedText);
      } else {
        this.$menuText.text(this.$openText);
      }

      this.$toggle.toggleClass('is-open');
      this.$menu.toggleClass('is-open');
    }
  };

}());
