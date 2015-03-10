(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var ignore = require('gulp-ignore');
  var minifyCss = require('gulp-minify-css');
  var rename = require('gulp-rename');
  var stylesDir = paths.dest + 'stylesheets/';

  gulp.task('minify:styles', ['sass'], function() {
    gulp.src(stylesDir + '**/*.css')
      .pipe(ignore.exclude('**/*.min.css'))
      .pipe(minifyCss({
        roundingPrecision: 3
      }))
      .pipe(rename({
        suffix: '.min'
      }))
      .pipe(gulp.dest(stylesDir));
  });
})();
