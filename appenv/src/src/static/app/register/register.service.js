(function () {
    'use strict';

    angular
        .module('appMain')
        .service('registerService', registerService);

    registerService.$inject = ['$http'];
    function registerService($http) {
        var service = {
            userId: userId,
            keyId: keyId,
            registerKey: registerKey,
            registerUser: registerUser
        };

        return service;

        function registerKey(key) {
            return $http.post('/api/key/register', JSON.stringify(key));
        }

        function registerUser(user) {
            return $http.post('/api/user/register', JSON.stringify(user));
        }

        function userId(tagData) {
            return $http.get('/api/user/tag/search/' + tagData);   // returns user ID
        }

        function keyId(tagData) {
            return $http.get('/api/key/tag/search/' + tagData);   // returns key ID
        }
    }
})();