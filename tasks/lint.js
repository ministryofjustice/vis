'use strict';

var gulp = require('gulp');
var paths = require('./_paths');
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');

function lintScripts () {
  var filesToLint = [
    paths.src + 'javascripts/**/*.js',
    'gulpfile.js',
    'tasks/**/*.js',
  ];

  return gulp.src(filesToLint)
    .pipe(jshint())
    .pipe(jshint.reporter(stylish));
}

// lint js code
gulp.task('lint', lintScripts);
