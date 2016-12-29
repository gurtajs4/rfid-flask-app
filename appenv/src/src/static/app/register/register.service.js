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
            return $http.post('/api/register/key', JSON.stringify(key));
        }

        function registerUser(user) {
            return $http.post('/api/register/user', JSON.stringify(user));
        }

        function userId(tagData) {
            return $http.get('/api/lookup/user', {
                params: {
                    id: tagData
                }
            });   // returns user ID
        }

        function keyId(tagData) {
            return $http.get('/api/lookup/key', {
                params: {
                    id: tagData
                }
            });   // returns key ID
        }
    }
})();