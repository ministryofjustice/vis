(function(){
  'use strict';

  var gulp = require('gulp');
  var merge = require('merge-stream');
  var paths = require('./_paths');

  // copy fonts
  gulp.task('copyfonts', function() {
    // all static fonts
    var staticFonts = gulp.src(paths.fonts)
      .pipe(gulp.dest(paths.dest + 'fonts/'));

    // specific paths for Fira font
    var fira = gulp.src(paths.src + 'vendor/fira/**/*.{eot,svg,ttf,woff}')
      .pipe(gulp.dest(paths.dest + 'stylesheets/'));

    return merge(staticFonts, fira);
  });
})();
