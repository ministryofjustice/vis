(function(){
  'use strict';

  var gulp = require('gulp');
  var concat = require('gulp-concat');
  var paths = require('./_paths');

  gulp.task('scripts', function() {
    gulp.src(paths.scripts)
      .pipe(concat('script.js'))
      .pipe(gulp.dest(paths.dest + 'javascripts/'));
  });
})();
