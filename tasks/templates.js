(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var templatizer = require('templatizer');

  // optimise images
  gulp.task('templates', function() {
    templatizer(paths.templates, paths.templates + 'compiled.js', {
      namespace: 'vis'
    });
  });
})();
