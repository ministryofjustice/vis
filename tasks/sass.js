(function(){
  'use strict';

  var gulp = require('gulp');
  var sass = require('gulp-ruby-sass');
  var paths = require('./_paths');

  gulp.task('sass', function() {
    return sass(paths.src + 'stylesheets/', {
        lineNumbers: true,
        compass: true,
        style: 'compact',
        loadPath: 'vis/assets-src/vendor/'
      })
      .on('error', function (err) { console.log(err.message); })
      .pipe(gulp.dest(paths.dest + 'stylesheets/'));
  });
})();
