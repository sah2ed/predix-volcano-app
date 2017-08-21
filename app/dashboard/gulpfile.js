'use strict';
const gulp = require('gulp');
const sass = require('gulp-sass');
const merge = require('merge-stream');

gulp.task('sass', function() {
    // Generate static css file
    return gulp.src('./sass/**/*.scss')
               .pipe(sass({
                    includePaths: './bower_components',
                    }).on('error', sass.logError))
               .pipe(gulp.dest('./dist/css'));
});

gulp.task('dist', function() {
        // bower_components and static files must all be serviceable
        // from static in order to support cross-browser polyfills

        var extraDirectories = [
            'bower_components/',
            'static/',
        ];

        var extraStreams = [];
        extraDirectories.forEach(function(src) {
            extraStreams.push(gulp.src([src + '/**/*.*']).pipe(gulp.dest('dist/' + src.replace(/^[^\/]+\//, ''))));
        });

        return merge(extraStreams);
});

gulp.task('default', ['sass', 'dist']);
