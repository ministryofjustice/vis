/* jshint unused: false */
(function(){
  'use strict';

  var gulp = require('gulp'),
      runSequence = require('run-sequence'),
      requireDir = require('require-dir'),
      dir = requireDir('./tasks'); // load tasks from ./tasks/ folder

  // setup default task
  gulp.task('default', ['build:prod']);

  // setup build task
  gulp.task('build:dev', ['clean:pre'], function (cb) {
    runSequence(
      ['copy-fonts', 'images', 'lint', 'sass', 'scripts'],
      'clean:post',
      cb
    );
  });
  gulp.task('build:prod', ['clean:pre'], function (cb) {
    runSequence(
      ['copy-fonts', 'images', 'lint', 'sass', 'scripts', 'minify-styles', 'minify-scripts'],
      'clean:post',
      cb
    );
  });
})();
