(function () {
  'use strict';

  vis.Modules.leaveSite = {
    selector: '.js-LeaveSite',
    weatherURL: 'https://www.bbc.co.uk/weather',

    init: function () {
      this.cacheEls();
      this.bindEvents();
    },
    
    cacheEls: function () {
      this.$body = $('body');
    },

    bindEvents: function () {
      this.$body.on('click.leaveSite', this.selector, this.leaveSite.bind(this));
    },
    
    leaveSite: function (evt) {
      evt.preventDefault();
      window.open(this.weatherURL);
      window.location.replace(evt.currentTarget.href);
    },
  };

}());
