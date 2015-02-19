(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var browserSync = require('browser-sync');
  var argv = require('yargs').argv;

  gulp.task('watch', ['build'], function() {
    var host = argv.host || argv.h || 'localhost';
    var port = argv.port || argv.p || 8000;

    browserSync({
      proxy: host + ':' + port,
      open: false,
      port: 3000
    });

    gulp.watch(paths.styles, ['sass']);
    gulp.watch(paths.scripts, ['scripts', browserSync.reload]);
    gulp.watch(paths.images, ['images', browserSync.reload]);
    gulp.watch(paths.icons, ['sass', browserSync.reload]);
    gulp.watch(paths.src + 'templates/**/*', ['sass', browserSync.reload]);
    gulp.watch('vis/templates/**/*', browserSync.reload); // django templates
  });
})();
