var gulp = require('gulp')
    , uglify = require('gulp-uglify')
    , concat = require('gulp-concat')
    , inject = require('gulp-inject')
    , angularFilesort = require('gulp-angular-filesort');


gulp.task('scripts', function () {
    gulp.src('index.html')
        .pipe(inject(
            gulp.src(['./app/*.js', './app/*/*.js'])
                .pipe(angularFilesort())
                .pipe(concat('angular.app.min.js'))
                .pipe(uglify())
                .pipe(gulp.dest('./'))
        ))
        .pipe(gulp.dest('./'));
});


gulp.task('styles', function () {
    var target = gulp.src('index.html');
    var sources = gulp.src([
        './vendor/bootstrap/dist/css/bootstrap.min.css'
    ], {read: false});

    return target.pipe(inject(sources)).pipe(gulp.dest('./'))
});