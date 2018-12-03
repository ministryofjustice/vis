'use strict';

var gulp = require('gulp');
var paths = require('./_paths');
var sass = require('gulp-sass');
var browsersync = require('browser-sync');
var iconfont = require('gulp-iconfont');
var consolidate = require('gulp-consolidate');
var rename = require('gulp-rename');
var ignore = require('gulp-ignore');
var minifyCss = require('gulp-minify-css');
var rename = require('gulp-rename');

function buildIcons (cb) {
  var runTimestamp = Math.round(Date.now() / 1000);

  return gulp.src(paths.icons)
    .pipe(iconfont({
      fontName: 'vis-icons',
      formats: ['ttf', 'eot', 'woff', 'svg'],
      timestamp: runTimestamp
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
}

function compileSass () {
  return gulp.src(paths.src + 'stylesheets/**/*.scss')
    .pipe(sass({
      outputStyle: 'compact',
      includePaths: ['vis/assets-src/vendor/', 'node_modules/']
    }).on('error', sass.logError))
    .pipe(gulp.dest(paths.dest + 'stylesheets/'))
    .pipe(browsersync.reload({stream:true}));
}

function minifyStyles () {
  var stylesDir = paths.dest + 'stylesheets/';

  return gulp.src(stylesDir + '**/*.css')
    .pipe(ignore.exclude('**/*.min.css'))
    .pipe(minifyCss({
      roundingPrecision: 3
    }))
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(stylesDir));
}

gulp.task('iconfont', buildIcons);
gulp.task('sass', compileSass);
gulp.task('styles', gulp.series('iconfont', 'sass'));
gulp.task('styles:minify', gulp.series('styles', minifyStyles));

