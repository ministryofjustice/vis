(function () {
  'use strict';

  vis.Modules.locateMe = {
    selector: '.locate-me',

    init: function () {
      _.bindAll(this, 'toggleClick');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$toggle = $(this.selector);
    },

    bindEvents: function () {
      this.$toggle.on('click', this.toggleClick);
    },

    toggleClick: function (evt) {
      evt.preventDefault();
      var self = this;
      navigator.geolocation.getCurrentPosition(function(data) {
        var form = self.$toggle.parents('form:first');
        form.find('input[name=q]').val('My location');
        form.find('input[name=lat]').val(data.coords.latitude);
        form.find('input[name=lng]').val(data.coords.longitude);
        form.trigger('submit');
      }, function(error) {
        alert('There was an error with your request, please try again.');
      });
    }
  };

}());
