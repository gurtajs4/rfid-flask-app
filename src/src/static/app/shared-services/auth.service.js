(function () {
    'use-strict';

    angular
        .module('appMain')
        .service('authService', authService);

    authService.$inject = ['$http', '$cookies'];
    function authService($http, $cookies) {
        var service = {
            login: login,
            setCredentials: setCredentials,
            clearCredentials: clearCredentials,
            getCredentials: getCredentials,
            isAuthenticated: isAuthenticated
        };

        return service;

        function login(username, password) {
            var authData = {username: username, password: password};
            return $http.post('/api/login', angular.toJson(authData));
        }

        function setCredentials(username, token, callback) {
            var globals = {
                username: username,
                token: token
            };
            $cookies.putObject('token', globals);

            $http.defaults.headers.common['Authorization'] = 'Token ' + token;
            callback();
        }

        function clearCredentials() {
            $cookies.remove('globals');
            $http.defaults.headers.common['Authorization'] = 'Token ';
        }

        function getCredentials() {
            return $cookies.getObject('globals')
        }

        function isAuthenticated() {
            return !!$cookies.getObject('globals')
        }
    }
})();