'use strict';

var gulp = require('gulp');
var paths = require('./_paths');
var del = require('del');

function postClean (cb) {
  del([
    paths.tmp,
    paths.src + 'stylesheets/_icons.scss' // generated icon font
  ], cb);
}

gulp.task('clean:post', postClean);
