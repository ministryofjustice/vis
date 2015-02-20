(function () {
  'use strict';

  vis.Modules.rowReveal = {
    selector: '.js-RowReveal',
    template: '<p class="u-center"><a class="Button u-center js-RowReveal-expand">See all cases</a></p>',

    init: function () {
      _.bindAll(this, 'render', 'expandClick');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$container = $(this.selector);
      this.$rows = this.$container.find(this.$container.data('rowSelector'));
    },

    bindEvents: function () {
      this.$container.on('click', '.js-RowReveal-expand', this.expandClick);
      vis.Events.on('render', this.render);
    },

    expandClick: function (evt) {
      evt.preventDefault();
      this.$rows.show();
      $(evt.target).remove();
    },

    render: function () {
      this.$rows.filter(':gt(0)').hide();
      this.$container.append(this.template);
    }
  };

}());
