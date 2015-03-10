/* jshint unused: false */
(function(){
  'use strict';

  var gulp = require('gulp'),
      requireDir = require('require-dir'),
      dir = requireDir('./tasks'); // load tasks from ./tasks/ folder

  // setup default task
  gulp.task('default', ['build:prod']);
})();
