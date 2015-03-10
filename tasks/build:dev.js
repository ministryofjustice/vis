(function(){
  'use strict';

  var gulp = require('gulp');
  var runSequence = require('run-sequence');

  gulp.task('build:dev', ['clean:pre'], function (cb) {
    runSequence(
      ['copyfonts', 'images', 'lint', 'sass', 'scripts'],
      cb
    );
  });
})();
