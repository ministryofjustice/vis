(function(){
  'use strict';

  var gulp = require('gulp');
  var concat = require('gulp-concat');
  var paths = require('./_paths');

  gulp.task('scripts', function() {
    // main scripts
    gulp.src(paths.scripts.vis)
      .pipe(concat('vis.js'))
      .pipe(gulp.dest(paths.dest + 'javascripts/'));
    // ie only scripts
    gulp.src(paths.scripts.ie)
      .pipe(concat('ie.js'))
      .pipe(gulp.dest(paths.dest + 'javascripts/'));
  });
})();
