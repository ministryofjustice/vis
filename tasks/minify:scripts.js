(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var ignore = require('gulp-ignore');
  var uglify = require('gulp-uglify');
  var rename = require('gulp-rename');
  var jsDir = paths.dest + 'javascripts/';

  gulp.task('minify:scripts', ['scripts'], function() {
    gulp.src(jsDir + '**/*.js')
      .pipe(ignore.exclude('**/*.min.js'))
      .pipe(uglify({
        mangle: false,
        compress: false  // don't compress to prevent reorder
      }))
      .pipe(rename({
        suffix: '.min'
      }))
      .pipe(gulp.dest(jsDir));
  });
})();
