(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');

  // copy fonts
  gulp.task('copy-fonts', function() {
    gulp.src(paths.fonts)
      .pipe(gulp.dest(paths.dest + 'fonts/'));
    // specific paths for Fira font
    gulp.src(paths.src + 'vendor/fira/**/*.{eot,svg,ttf,woff}')
      .pipe(gulp.dest(paths.dest + 'stylesheets/'));
  });
})();
