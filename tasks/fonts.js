'use strict';

var gulp = require('gulp');
var paths = require('./_paths');

function copyStatic () {
  return gulp.src(paths.fonts)
    .pipe(gulp.dest(paths.dest + 'fonts/'));
}

function copyFira () {
  return gulp.src(paths.node_modules + 'mozilla-fira-pack/**/*.{eot,svg,ttf,woff,woff2}')
    .pipe(gulp.dest(paths.dest + 'fonts/'));
}

gulp.task('fonts', gulp.parallel(copyStatic, copyFira));
