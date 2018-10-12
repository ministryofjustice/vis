(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var sass = require('gulp-sass');
  var browserSync = require('browser-sync');

  gulp.task('sass', ['iconfont'], function() {
    return gulp.src(paths.src + 'stylesheets/**/*.scss')
      .pipe(sass({
        outputStyle: 'compact',
        includePaths: ['vis/assets-src/vendor/', 'node_modules/']
      }).on('error', sass.logError))
      .pipe(gulp.dest(paths.dest + 'stylesheets/'))
      .pipe(browserSync.reload({stream:true}));
  });
})();
