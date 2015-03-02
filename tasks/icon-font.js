(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var iconfont = require('gulp-iconfont');
  var consolidate = require('gulp-consolidate');
  var rename = require('gulp-rename');

  gulp.task('iconfont', function (cb) {
    var fontName = 'vis-icons';

    return gulp.src(paths.icons)
      .pipe(iconfont({
        fontName: fontName
      }))
      .on('codepoints', function(codepoints) {
        var templateOptions = {
          glyphs: codepoints,
          fontName: fontName,
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
          .pipe(rename({ basename: fontName }))
          .pipe(gulp.dest(paths.dest + 'fonts/'));
      })
      .pipe(gulp.dest(paths.dest + 'fonts/'));
  });
})();
