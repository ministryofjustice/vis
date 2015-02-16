(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');

  gulp.task('watch', function() {
    gulp.watch(paths.styles, ['sass']);
    gulp.watch(paths.scripts, ['scripts']);
    gulp.watch(paths.images, ['images']);
  });
})();
