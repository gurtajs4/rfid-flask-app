var appMain = angular.module('appMain');

//var appBaseUrl = angular.element(document.querySelector('base')).attr('href');
var appBaseUrl = angular.element(document.querySelector('base')).attr('href') + 'static/app'

//, $interpolateProvider
function config($routeProvider, $locationProvider) {

//    $interpolateProvider.startSymbol('<<').endSymbol('>>');

//    $locationProvider.html5Mode(true);
    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false,
        rewriteLinks: true,
    });

    $routeProvider.
    when('/home', {
        templateUrl: appBaseUrl + '/home/home.html',
        controller: 'HomeController'
    }).
//    when('/', {
//        templateUrl: appBaseUrl + '/sessions/session-list.html',
//        controller: 'SessionsController',
//    }).
    when('/sessions', {
        templateUrl: appBaseUrl + '/sessions/session-list.html',
        controller: 'SessionsController',
    }).
    when('/sessions/:id', {
        templateUrl: appBaseUrl + '/sessions/session-info.html',
        controller: 'SessionInfoController'
    }).
//    when('/users', {
//        templateUrl: appBaseUrl + '/users/users-list.html',
//        controller: 'UsersListController'
//    }).
//    when('/users/:id', {
//        templateUrl: appBaseUrl + '/users/user-details.html',
//        controller: 'UserDetailsController'
//    }).
//    when('/keys', {
//        templateUrl: appBaseUrl + '/keys/keys-list.html',
//        controller: 'KeysListController'
//    }).
//    when('/keys/:id', {
//        templateUrl: appBaseUrl + '/keys/key-details.html',
//        controller: 'KeyDetailsController'
//    }).
    otherwise({ redirectTo: '/home' });
}

//config.$inject = ['$routeProvider', '$locationProvider', '$interpolateProvider'];
config.$inject = ['$routeProvider', '$locationProvider'];
appMain.config(config);