(function () {
  'use strict';

  vis.Modules.pccSearch = {
    selector: '.js-PCCSearch',

    init: function () {
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$formSubmits = $('[type="submit"]', this.selector);
    },

    bindEvents: function () {
      this.$formSubmits.on('click', this.formSubmit);
    },

    formSubmit: function (evt) {
      // abandon if link already aborted or analytics is not available
      if (evt.isDefaultPrevented() || typeof ga !== 'function') {
        return;
      }

      evt.preventDefault();
      var $form = $(evt.currentTarget).parents('form');
      var location = $form.attr('name');
      var submitForm = function () {
        $form.submit();
      };

      ga('send', {
        'hitType': 'event',
        'eventCategory': 'search',
        'eventAction': 'submitted',
        'eventLabel': location,
        'hitCallback': submitForm
      });

      // submit after one second if recording takes too long
      setTimeout(submitForm, 1000);
    }
  };

}());
