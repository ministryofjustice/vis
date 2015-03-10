/* jshint unused: false */
(function(){
  'use strict';

  var gulp = require('gulp');
  var requireDir = require('require-dir');
  var dir = requireDir('./tasks'); // load tasks from ./tasks/ folder

  // setup default task
  gulp.task('default', ['build:prod']);
})();
