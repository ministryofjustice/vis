(function () {
  'use strict';

  vis.Modules.detailsPolyfill = {
    selector: 'details',

    init: function () {
      _.bindAll(this, 'render');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$details = $(this.selector);
    },

    bindEvents: function () {
      vis.Events.on('render', this.render);
    },

    render: function () {
      this.$details.details();
      if (!$.fn.details.support) {
        this.$details.addClass('is-notnative');
      }
    }
  };

}());
