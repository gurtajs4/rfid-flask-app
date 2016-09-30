var appMain = angular.module('appMain');

var appBaseUrl = angular.element(document.querySelector('base')).attr('href');

function config($routeProvider, $locationProvider) {

    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false,
        rewriteLinks: true,
    });

    $routeProvider.
    when('/', {
        templateUrl: appBaseUrl + '/sessions/session-list.html',
        controller: 'SessionsController',
    }).
    when('/sessions', {
        templateUrl: appBaseUrl + '/sessions/session-list.html',
        controller: 'SessionsController',
    }).
    when('/sessions/:id', {
        templateUrl: appBaseUrl + '/sessions/session-info.html',
        controller: 'SessionInfoController'
    }).
    otherwise({ redirectTo: '/' });
}

config.$inject = ['$routeProvider', '$locationProvider'];
appMain.config(config);