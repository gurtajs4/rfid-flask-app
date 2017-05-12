(function () {
    'use-strict';

    angular
        .module('appMain')
        .service('authService', authService);

    authService.$inject = ['$http', '$cookies'];
    function authService($http, $cookies) {
        var service = {
            login: login,
            logout: logout,
            setCredentials: setCredentials,
            clearCredentials: clearCredentials
        };

        return service;

        function login(username, password) {
            var authData = {username: username, password: password};
            return $http.post('/api/login', angular.toJson(authData));
        }

        function logout() {
            return $http.get('/api/logout');
        }

        function setCredentials(username, token, callback) {
            var globals = {
                username: username,
                token: token
            };
            $cookies.putObject('token', globals);

            $http.defaults.headers.common['Authorization'] = 'Token ' + token;
            callback(username);
        }

        function clearCredentials(callback) {
            callback();     // clear credentials in main ctrl
            $cookies.remove('globals');
            $http.defaults.headers.common['Authorization'] = 'Token ';
        }
    }
})();