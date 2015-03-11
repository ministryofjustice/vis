var gulp = require('gulp');
var revall = require('gulp-rev-all');
var paths = require('./_paths');

gulp.task('revall', function () {
  // by default, gulp would pick `assets/css` as the base,
  // so we need to set it explicitly:
  return gulp.src(paths.dest+'**')
    .pipe(revall())
    .pipe(gulp.dest(paths.dest))  // write rev'd assets to build dir
    .pipe(revall.manifest({ fileName: 'manifest.json' })) // create manifest (`fileName` is optional)
    .pipe(gulp.dest(paths.dest)); // write manifest to build dir
});
