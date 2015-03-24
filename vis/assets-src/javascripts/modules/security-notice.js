(function () {
  'use strict';

  vis.Modules.securityNotice = {
    selector: '.js-SecurityExit',
    storageKey: 'securityDisabled',

    init: function () {
      // _.bindAll(this, 'render', 'closeClick');
      // this.cacheEls();
      // this.bindEvents();
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
      $.cookie('vis', true, { path: '/' });
      this.$banner.remove();
    },

    isDisabled: function () {
      if ($.cookie('vis')) {
        return true;
      }
      return false;
    },

    render: function () {
      if (this.isDisabled()) {
        this.$banner.remove();
      }
    }
  };

}());
