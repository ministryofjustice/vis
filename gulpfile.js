/* jshint unused: false */
(function(){
  'use strict';

  var gulp = require('gulp'),
      runSequence = require('run-sequence'),
      requireDir = require('require-dir'),
      dir = requireDir('./tasks'); // load tasks from ./tasks/ folder

  // setup default task
  gulp.task('default', ['build']);

  // setup build task
  gulp.task('build', ['clean:pre'], function (cb) {
    runSequence(
      ['copy-fonts', 'images', 'lint', 'sass', 'scripts'],
      'clean:post',
      cb
    );
  });
})();
