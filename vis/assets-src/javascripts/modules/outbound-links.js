(function () {
  'use strict';

  vis.Modules.outboundLinks = {
    selector: 'a[href]',

    init: function () {
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$body = $('body');
    },

    bindEvents: function () {
      this.$body.on('click.outboundLinks', this.selector, this.linkClick);
    },

    linkClick: function (evt) {
      // abandon if link already aborted or analytics is not available
      if (evt.isDefaultPrevented() || typeof ga !== 'function') {
        return;
      }

      // abandon if no active link or link within domain
      var link = $(evt.currentTarget).attr('href');

      // abandon if local absolute link
      if (link.indexOf(window.location.host) !== -1) {
        return;
      }

      // proceed if still contains external protocol
      if (link.match(/^http/)) {
        // cancel event and record outbound link
        evt.preventDefault();

        var loadPage = function () {
          document.location = link;
        };

        ga('send', {
          'hitType': 'event',
          'eventCategory': 'outbound',
          'eventAction': 'click',
          'eventLabel': link,
          'hitCallback': loadPage
        });

        // redirect after one second if recording takes too long
        setTimeout(loadPage, 1000);
      }
    }
  };

}());
