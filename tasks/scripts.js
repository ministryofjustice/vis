'use strict';

var gulp = require('gulp');
var concat = require('gulp-concat');
var paths = require('./_paths');
var mkdirp = require('mkdirp');
var templatizer = require('templatizer');
var ignore = require('gulp-ignore');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');

var jsDir = paths.dest + 'javascripts/';

// compile js templates
function templates (cb) {
  var dir = paths.tmp + 'javascripts/';

  mkdirp(dir, function (err) {
    if (err) {
      console.error(err);
    } else {
      templatizer(paths.templates, dir + 'templates.js', {
        namespace: 'vis'
      });
    }
    cb();
  });
}

function buildMainScripts () {
  return gulp.src(paths.scripts.vis)
    .pipe(concat('vis.js'))
    .pipe(gulp.dest(paths.dest + 'javascripts/'));
}

function buildIeScripts () {
  return gulp.src(paths.scripts.ie)
    .pipe(concat('ie.js'))
    .pipe(gulp.dest(paths.dest + 'javascripts/'));
}

function minifyScripts () {
  return gulp.src(jsDir + '**/*.js')
    .pipe(ignore.exclude('**/*.min.js'))
    .pipe(uglify({
      mangle: false,
      compress: false  // don't compress to prevent reorder
    }))
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(jsDir));
}

gulp.task('templates', templates);
gulp.task('scripts', gulp.series('templates', gulp.parallel(buildMainScripts, buildIeScripts)));
gulp.task('scripts:minify', gulp.series('scripts', minifyScripts));
