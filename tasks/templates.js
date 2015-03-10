(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var mkdirp = require('mkdirp');
  var templatizer = require('templatizer');

  // compile js templates
  gulp.task('templates', function (cb) {
    var dir = paths.tmp + 'javascripts/';

    mkdirp(dir, function (err) {
      if (err) {
        console.error(err);
      } else {
        templatizer(paths.templates, dir + 'templates.js', {
          namespace: 'vis'
        });
      }
      cb();
    });
  });
})();
