var appMain = angular.module('musicApp');

var baseUrl = angular.element(document.querySelector('base')).attr('href');
var appBaseUrl = baseUrl + "AngularApp/";

function config($routeProvider, $locationProvider) {

    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });

    $routeProvider.
    when('/sessions', {
        templateUrl: appBaseUrl + '/sessions/session-list.html',
        controller: 'SessionsController',
    }).
    when('/sessions/:id', {
        templateUrl: appBaseUrl + '/sessions/session-details.html',
        controller: 'SessionInfoController'
    }).
    when('/users', {
        templateUrl: appBaseUrl + '/users/users-list.html',
        controller: 'UsersListController'
    }).
    when('/users/:id', {
        templateUrl: appBaseUrl + '/users/user-details.html',
        controller: 'UserDetailsController'
    }).
    when('/keys', {
        templateUrl: appBaseUrl + '/keys/keys-list.html',
        controller: 'KeysListController'
    }).
    when('/keys/:id', {
        templateUrl: appBaseUrl + '/keys/key-details.html',
        controller: 'KeyDetailsController'
    }).
    otherwise({ redirectTo: '/sessions' });
}