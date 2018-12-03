'use strict';

var gulp = require('gulp');
var RevAll = require('gulp-rev-all');
var paths = require('./_paths');

function revisionAssets() {
  var revOptions = {
    fileNameManifest: 'manifest.json',
      includeFilesInManifest: [
        '.eot',
        '.ttf',
        '.woff',
        '.woff2',
        '.svg',
        '.png',
        '.gif',
        '.jpg',
        '.jpeg',
        '.ico',
        '.js',
        '.css',
      ],
  };

  return gulp.src(paths.dest + '**')
    .pipe(RevAll.revision(revOptions))
    .pipe(gulp.dest(paths.dest))
    .pipe(RevAll.manifestFile())
    .pipe(gulp.dest(paths.dest));
}

gulp.task('revision', revisionAssets);
