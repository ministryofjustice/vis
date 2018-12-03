'use strict';

var gulp = require('gulp');
var concat = require('gulp-concat');
var paths = require('./_paths');
var mkdirp = require('mkdirp');
var template = require('gulp-template-compile');
var ignore = require('gulp-ignore');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');


var jsDir = paths.dest + 'javascripts/';
var tempJsDir = paths.tmp + 'javascripts/';

function createTempDir (cb) {
  mkdirp(tempJsDir, function (err) {
    if (err) {
      cb(err);
    } else {
      cb();
    }
  });
}

// compile js templates
function templates () {
  return gulp.src(paths.templates + '**/*.html')
    .pipe(template({
      namespace: 'vis.templates',
      name: function (file) {
        var paths = file.relative.replace('.html', '');
        var parts = paths.split('/');

        return parts.join('.');
      },
    }))
    .pipe(concat('templates.js'))
    .pipe(gulp.dest(tempJsDir));
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

gulp.task('templates', gulp.series(createTempDir, templates));
gulp.task('scripts', gulp.series('templates', gulp.parallel(buildMainScripts, buildIeScripts)));
gulp.task('scripts:minify', gulp.series('scripts', minifyScripts));
