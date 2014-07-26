var gulp = require('gulp');

var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var compass = require('gulp-compass');
var changed = require('gulp-changed');
// var imagemin = require('gulp-imagemin');
var minifyCSS = require('gulp-minify-css');
// var optipng = require('imagemin-optipng');
var livereload = require('gulp-livereload');
var lr = require('tiny-lr');
var server = lr();
var notify = require('gulp-notify');

var paths = {
  scripts: 'bgradar/assets/js/**/*',
  styles: 'bgradar/assets/styles/*.scss',
  images: 'bgradar/assets/images/**/*.{jpg,jpeg,png,gif}',
  partials: 'bgradar/assets/partials/**/*'
};

gulp.task('styles', function () {
  return gulp.src(paths.styles)
    // .pipe(gulp.dest('bgradar/static/assets/styles'))
    .pipe(compass({
        style: 'compressed',
        comments: false,
        css: 'bgradar/static/assets/styles',
        sass: 'bgradar/assets/styles',
        // image: 'bgradar/static/assets/images',
        // font: 'bgradar/static/assets/fonts',
        import_path: [
            // 'bower_components/bootstrap-sass-official/vendor/assets/stylesheets',
            // 'bower_components/components-font-awesome/scss'
        ]
    }))
    .pipe(livereload(server))
});


gulp.task('vendor-js', function() {
  return gulp.src([
                    'bower_components/jquery/dist/jquery.js',
                    'bower_components/bootstrap/dist/js/bootstrap.min.js',
                    // 'bower_components/blockui/jquery.blockUI.js',
                    'bower_components/angular/angular.js',
                    'bower_components/angular-resource/angular-resource.js',
                    'bower_components/angular-route/angular-route.js',
                    'bower_components/angular-strap/dist/angular-strap.js',
                    'bower_components/angular-strap/dist/modules/datepicker.tpl.js',
                    'bower_components/angular-translate/angular-translate.js',
                    'bower_components/angular-ui/angular-ui.js',
                    'bower_components/ngDialog/js/ngDialog.js',
                    'bower_components/mousetrap/mousetrap.js',
                    // 'bgradar/assets/js/utils/utils-module.js',
                    // 'bgradar/assets/js/utils/ui-bootstrap-tpls-0.11.0.min.js'
                  ])
    .pipe(uglify({mangle: false}))
    .pipe(concat('vendor.min.js'))
    .pipe(gulp.dest('bgradar/static/assets/js'))
    .pipe(livereload(server))
});

gulp.task('vendor-css', function () {
  return gulp.src([
      'bower_components/bootstrap/dist/css/bootstrap.css',
      'bgradar/assets/libstyle/**/*'
    ])
    .pipe(concat('vendor-css.min.css'))
    .pipe(gulp.dest('bgradar/static/assets/styles'))
    .pipe(livereload(server))
});



gulp.task('scripts', function() {
  return gulp.src(paths.scripts)
    .pipe(uglify({mangle: false}))
    .pipe(gulp.dest('bgradar/static/assets/js'))
    .pipe(livereload(server))
});


// gulp.task('images', function() {

//   var imgDst = './static/assets/images';

//   return gulp.src(paths.images)
//     .pipe(changed(imgDst))
//     .pipe(gulp.dest(imgDst))
//     .pipe(livereload(server))
//     .pipe(notify({ message: 'Images task completed.' }));

// });


gulp.task('partials', function() {

  var paritalsDst = 'bgradar/static/partials';

  return gulp.src(paths.partials)
    .pipe(gulp.dest(paritalsDst))
    .pipe(livereload(server))
});

gulp.task('fonts', function () {
  return gulp.src([
      'bower_components/fontawesome/fonts/*',
      'bower_components/bootstrap/fonts/*'
    ])
    .pipe(gulp.dest('bgradar/static/assets/fonts'))
});



// Rerun the task when a file changes
gulp.task('watch', function() {
  server.listen(35709, function (e) {
    if (e) {
      return console.log(e);
    };

    var watcher = gulp.watch([
                               paths.scripts,
                               paths.styles,
                               paths.partials,
                               'bower_components/bootstrap/dist/css/bootstrap.css',
                               'bgradar/assets/styles/libs/**/*',
                               'bower_components/**/*.js',
                               'templates/**/*.html'
                               // paths.images
                             ],
                             [
                               'scripts',
                               'styles',
                               'partials',
                               'vendor-css',
                               'vendor-css',
                               'vendor-js'
                               // 'images'
                             ]);

    watcher.on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
  });
});


gulp.task('debug-watch', function() {
  server.listen(35709, function (e) {
    if (e) {
      return console.log(e);
    };

    var watcher = gulp.watch([
                               paths.scripts,
                               paths.styles,
                               paths.partials
                             ],
                             [
                               'scripts',
                               'styles',
                               'partials'
                             ]);

    watcher.on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
  });
});

gulp.task('default', ['vendor-js', 'scripts', 'partials', 'vendor-css', 'styles', 'fonts','watch']);
gulp.task('debug', ['scripts', 'styles', 'debug-watch']);
