(function(){
  'use strict';

  var paths = {
    root: './',
    tmp: './.gulptmp/',
    dest: './vis/assets/',
    src: './vis/assets-src/',
    vendor: './vis/assets-src/vendor/',
    node_modules: './node_modules/',
    icons: [],
    images: [],
    fonts: [],
    styles: [],
    templates: [],
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
  // templates
  paths.templates.push(paths.src + 'javascripts/templates/');
  // scripts
  paths.scripts.ie.push(paths.vendor + 'html5shiv/dist/html5shiv.js');
  paths.scripts.ie.push(paths.vendor + 'html5shiv/dist/html5shiv-printshiv.js');
  paths.scripts.vis.push(paths.node_modules + 'lodash/index.js');
  paths.scripts.vis.push(paths.vendor + 'jquery/dist/jquery.js');
  paths.scripts.vis.push(paths.vendor + 'jquery-details/jquery.details.js');
  paths.scripts.vis.push(paths.vendor + 'jquery-cookie/jquery.cookie.js');
  paths.scripts.vis.push(paths.src + 'javascripts/vis.js');
  paths.scripts.vis.push(paths.tmp + 'javascripts/templates.js'); // auto generated in templates task
  paths.scripts.vis.push(paths.src + 'javascripts/modules/**.*js');
  paths.scripts.vis.push(paths.src + 'javascripts/app.js');

  module.exports = paths;
})();
