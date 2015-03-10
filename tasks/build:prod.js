(function(){
  'use strict';

  var gulp = require('gulp');
  var runSequence = require('run-sequence');

  gulp.task('build:prod', ['clean:pre'], function (cb) {
    runSequence(
      ['copyfonts', 'images', 'lint', 'sass', 'scripts', 'minify:styles', 'minify:scripts'],
      'clean:post',
      cb
    );
  });
})();
