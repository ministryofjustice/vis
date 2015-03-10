(function () {
  'use strict';

  vis.Modules.rowReveal = {
    selector: '.js-RowReveal',
    template: vis.templatizer.RowReveal.expandButton(),

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
      if (this.$rows.length > 1) {
        this.$rows.filter(':gt(0)').hide();
        this.$container.append(this.template);
      }
    }
  };

}());
