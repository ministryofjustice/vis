(function(){
  'use strict';

  var gulp = require('gulp');
  var merge = require('merge-stream');
  var concat = require('gulp-concat');
  var paths = require('./_paths');
  var uglify = require('gulp-uglify');
  var rename = require('gulp-rename');

  gulp.task('scripts', function() {
    // main scripts
    var main = gulp.src(paths.scripts.vis)
      .pipe(concat('vis.js'))
      .pipe(gulp.dest(paths.dest + 'javascripts/'));

    // ie only scripts
    var ie = gulp.src(paths.scripts.ie)
      .pipe(concat('ie.js'))
      .pipe(gulp.dest(paths.dest + 'javascripts/'));

    return merge(main, ie);
  });
})();
