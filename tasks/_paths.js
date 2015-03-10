(function(){
  'use strict';

  var paths = {
    tmp: '.gulptmp/',
    dest: 'vis/assets/',
    src: 'vis/assets-src/',
    vendor: 'vis/assets-src/vendor/',
    icons: [],
    images: [],
    fonts: [],
    styles: [],
    scripts: {
      ie: [],
      vis: []
    }
  };

  // styles
  paths.styles.push(paths.src + 'stylesheets/**/*.scss');
  // icons
  paths.icons.push(paths.src + 'fonts/svg-src/*.svg');
  // fonts
  paths.fonts.push(paths.src + 'fonts/*.{eot,svg,ttf,woff}');
  // images
  paths.images.push(paths.src + 'images/**/*');
  // scripts
  paths.scripts.ie.push(paths.vendor + 'html5shiv/dist/html5shiv.js');
  paths.scripts.ie.push(paths.vendor + 'html5shiv/dist/html5shiv-printshiv.js');
  paths.scripts.vis.push(paths.vendor + 'lodash/lodash.js');
  paths.scripts.vis.push(paths.vendor + 'jquery/dist/jquery.js');
  paths.scripts.vis.push(paths.vendor + 'jquery-details/jquery.details.js');
  paths.scripts.vis.push(paths.src + 'javascripts/vis.js');
  paths.scripts.vis.push(paths.src + 'javascripts/modules/**.*js');
  paths.scripts.vis.push(paths.src + 'javascripts/app.js');

  module.exports = paths;
})();
