(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var sass = require('gulp-ruby-sass');
  var browserSync = require('browser-sync');

  gulp.task('sass', ['iconfont'], function() {
    return sass(paths.src + 'stylesheets/', {
        lineNumbers: true,
        compass: false,
        bundleExec: true,
        style: 'compact',
        loadPath: ['vis/assets-src/vendor/', 'node_modules/']
      })
      .on('error', function (err) { console.log(err.message); })
      .pipe(gulp.dest(paths.dest + 'stylesheets/'))
      .pipe(browserSync.reload({stream:true}));
  });
})();
