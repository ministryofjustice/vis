'use strict';

var gulp = require('gulp');
var paths = require('./_paths');
var imagemin = require('gulp-imagemin');

function optimiseImages () {
  return gulp
    .src(paths.images)
    .pipe(imagemin())
    .pipe(gulp.dest(paths.dest + 'images'));
}

gulp.task('images', optimiseImages);
