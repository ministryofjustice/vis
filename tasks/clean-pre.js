(function(){
  'use strict';

  var gulp = require('gulp');
  var paths = require('./_paths');
  var del = require('del');

  // clean out assets folder
  gulp.task('clean:pre', function (cb) {
    del([
      paths.dest,
      paths.tmp,
      paths.src + 'stylesheets/_icons.scss', // generated icon font
      paths.templates + 'compiled.js' // generated js templates
    ], cb);
  });
})();
