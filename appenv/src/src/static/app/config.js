(function () {
    'use strict';

    angular
        .module('appMain')
        .config(config);

    config.$inject = ['$routeProvider', '$locationProvider', 'templateServiceProvider'];

    function config($routeProvider, $locationProvider, templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();

        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false,
            rewriteLinks: true,
        });

        $routeProvider.when('/home', {
            templateUrl: appBaseUrl + '/home/home.html',
            controller: 'HomeController'
        }).when('/sessions', {
            templateUrl: appBaseUrl + '/sessions/session-list.html',
            controller: 'SessionsController',
        }).when('/sessions/:id', {
            templateUrl: appBaseUrl + '/sessions/session-info.html',
            controller: 'SessionInfoController'
        }).when('/keys/lookup', {
            templateUrl: appBaseUrl + '/keys/keys-lookup.html',
            controller: 'KeysLookupController'
        }).when('/people/lookup', {
            templateUrl: appBaseUrl + '/people/people-lookup.html',
            controller: 'PeopleLookupController'
        }).when('/register/person', {
            templateUrl: appBaseUrl + '/register/register-person.html',
            controller: 'RegisterPersonController'
        }).when('/register/key', {
            templateUrl: appBaseUrl + '/register/register-key.html',
            controller: 'RegisterKeyController'
        }).otherwise({redirectTo: '/home'});
    }
})();
