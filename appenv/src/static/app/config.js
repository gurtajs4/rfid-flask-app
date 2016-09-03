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
        controllerAs: 'sessions'
    }).
    when('/sessions/:id', {
        templateUrl: appBaseUrl + '/sessions/session-details.html',
        controller: 'SessionInfoController',
        controllerAs: 'sessionInfo'
    }).
    when('/users', {
        templateUrl: appBaseUrl + '/users/users-list.html',
        controller: 'UsersListController',
        controllerAs: 'users'
    }).
    when('/users/:id', {
        templateUrl: appBaseUrl + '/users/user-details.html',
        controller: 'UserDetailsController',
        controllerAs: 'userInfo'
    }).
    when('/keys', {
        templateUrl: appBaseUrl + '/keys/keys-list.html',
        controller: 'KeysListController',
        controllerAs: 'keys'
    }).
    when('/keys/:id', {
        templateUrl: appBaseUrl + '/keys/key-details.html',
        controller: 'KeyDetailsController',
        controllerAs: 'keyInfo'
    }).
    otherwise({ redirectTo: '/sessions' });
}