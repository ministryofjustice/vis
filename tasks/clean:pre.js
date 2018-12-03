'use strict';

var gulp = require('gulp');
var paths = require('./_paths');
var del = require('del');

function preClean (cb) {
  del([
    paths.dest,
    paths.tmp,
    paths.src + 'stylesheets/_icons.scss' // generated icon font
  ], cb);
}

gulp.task('clean:pre', preClean);
