var gulp = require('gulp')
    , uglify = require('gulp-uglify')
    , concat = require('gulp-concat')
    , inject = require('gulp-inject')
    , prefix = require('gulp-prefix')
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
    var prefixUrl = 'static/';
    var target = gulp.src('index.html');
    var sources = gulp.src([
        './vendor/bootstrap-css-only/css/bootstrap.min.css',
        './vendor/angular-bootstrap/ui-bootstrap-csp.css',
        './css/site.css'
    ], {read: false});

    return target.pipe(inject(sources.pipe(prefix(prefixUrl)))).pipe(gulp.dest('./'))
});