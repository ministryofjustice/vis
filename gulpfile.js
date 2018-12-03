/*jslint node: true */
'use strict';

var gulp = require('gulp');
var HubRegistry = require('gulp-hub');
var browsersync = require('browser-sync');
var argv = require('yargs').argv;
var paths = require('./tasks/_paths');

var hub = new HubRegistry(['tasks/*.js']);

gulp.registry(hub);

// Build tasks
gulp.task(
  'build:dev',
  gulp.series(
    'clean:pre',
    gulp.parallel('fonts', 'images', 'lint', 'styles', 'scripts')
  )
);

gulp.task(
  'build:prod',
  gulp.series(
    'clean:pre',
    gulp.parallel(
      'fonts',
      'images',
      'lint',
      'scripts:minify',
      'styles:minify'
    ),
    'revision',
    'clean:post'
  )
);

// BrowserSync
function browserSync (done) {
  var host = argv.host || argv.h || 'localhost';
  var port = argv.port || argv.p || 8000;

  browsersync({
    proxy: host + ':' + port,
    open: false,
    port: 3000,
  });
  done();
}

// BrowserSync Reload
function browserSyncReload (done) {
  browsersync.reload();
  done();
}

// Watch files
function watchFiles () {
  gulp.watch(paths.styles, gulp.series('sass'));
  gulp.watch(paths.src + 'javascripts/**/*', gulp.series('scripts', browserSyncReload));
  gulp.watch(paths.images, gulp.series('images', browserSyncReload));
  gulp.watch('vis/templates/**/*', browserSyncReload); // django templates
}

gulp.task('watch', gulp.series('build:dev', browserSync, watchFiles));
