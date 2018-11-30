(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var iconfont = require('gulp-iconfont');
  var consolidate = require('gulp-consolidate');
  var rename = require('gulp-rename');

  gulp.task('iconfont', function (cb) {
    var runTimestamp = Math.round(Date.now() / 1000);

    return gulp.src(paths.icons)
      .pipe(iconfont({
        fontName: 'vis-icons',
        formats: ['ttf', 'eot', 'woff', 'svg'],
        timestamp: runTimestamp,
      }))
      .on('glyphs', function(glyphs, options) {
        var templateOptions = {
          glyphs: glyphs,
          fontName: options.fontName,
          fontPath: '../fonts/',
          className: 'Icon'
        };

        // export sass template
        gulp.src(paths.src + 'templates/_icons.scss')
          .pipe(consolidate('lodash', templateOptions))
          .pipe(gulp.dest(paths.src + 'stylesheets/'));

        // create template containing all fonts
        gulp.src(paths.src + 'templates/icon-template.html')
          .pipe(consolidate('lodash', templateOptions))
          .pipe(rename({ basename: options.fontName }))
          .pipe(gulp.dest(paths.dest + 'fonts/'));
      })
      .pipe(gulp.dest(paths.dest + 'fonts/'));
  });
})();
