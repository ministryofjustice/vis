(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var imagemin = require('gulp-imagemin');

  // optimise images
  gulp.task('images', function() {
    return gulp
      .src(paths.images)
      .pipe(imagemin())
      .pipe(gulp.dest(paths.dest + 'images'));
  });
})();
