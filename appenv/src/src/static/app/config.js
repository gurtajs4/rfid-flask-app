(function () {
    'use strict';

    angular
        .module('appMain')
        .config(config);

    config.$inject = ['$routeProvider', '$locationProvider'];

    function config($routeProvider, $locationProvider) {
        var appBaseUrl = angular.element(document.querySelector('base')).attr('href') + 'static/app';

        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false,
            rewriteLinks: true
        });

        $routeProvider.when('/home', {
            templateUrl: appBaseUrl + '/home/home.html',
            controller: 'HomeController',
            controllerAs: 'home'
        }).when('/sessions', {
            templateUrl: appBaseUrl + '/sessions/sessions.html',
            controller: 'SessionsController',
            controllerAs: 'sessions'
        }).when('/sessions/:id', {
            templateUrl: appBaseUrl + '/sessions/session-info.html',
            controller: 'SessionInfoController',
            controllerAs: 'sessionInfo'
        }).when('/keys/search', {
            templateUrl: appBaseUrl + '/keys/keys-search.html',
            controller: 'KeysSearchController',
            controllerAs: 'keysSearch'
        }).when('/users/search', {
            templateUrl: appBaseUrl + '/users/users-search.html',
            controller: 'UsersSearchController',
            controllerAs: 'usersSearch'
        }).when('/users/register', {
            templateUrl: appBaseUrl + '/register/user-register.html',
            controller: 'UserRegisterController',
            controllerAs: 'userRegister'
        }).when('/keys/register', {
            templateUrl: appBaseUrl + '/register/key-register.html',
            controller: 'KeyRegisterController',
            controllerAs: 'keyRegister'
        }).otherwise({redirectTo: '/home'});
    }
})();
