(function () {
  'use strict';

  vis.Modules.outboundLinks = {
    selector: 'a[rel="external"]',

    init: function () {
      _.bindAll(this, 'linkClick');
      this.cacheEls();
      this.bindEvents();
    },

    cacheEls: function () {
      this.$body = $('body');
      // this.$externalLinks = $(this.selector);
    },

    bindEvents: function () {
      this.$body.on('click', 'a[href]', this.linkClick);
    },

    linkClick: function (evt) {
      // abandon if link already aborted or analytics is not available
      if (evt.isDefaultPrevented() || typeof ga !== "function") {
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
        ga('send', {
          'hitType': 'event',
          'eventCategory': 'outbound',
          'eventAction': 'click',
          'eventLabel': link,
          'hitCallback': loadPage
        });

        // redirect after one second if recording takes too long
        setTimeout(loadPage, 1000);

        // redirect to outbound page
        function loadPage() {
          document.location = link;
        }
      }
    }
  };

}());
