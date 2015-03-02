(function(){
  'use strict';

  var vis = {

    Modules: {},

    Helpers: {},

    Events: $({}),

    init: function () {
      for (var x in vis.Modules) {
        if (typeof vis.Modules[x].init === 'function') {
          vis.Modules[x].init();
        }
      }
      // trigger initial render event
      vis.Events.trigger('render');
    },

    // safe logging
    log: function (msg) {
      if (window && window.console) {
        window.console.log(msg);
      }
    },
    dir: function (obj) {
      if (window && window.console) {
        window.console.dir(obj);
      }
    }

  };

  window.vis = vis;
}());
