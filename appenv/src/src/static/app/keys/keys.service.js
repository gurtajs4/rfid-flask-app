(function () {
    'use strict';

    angular
        .module('appMain')
        .service('keysService', keysService);

    keysService.$inject = ['$http'];
    function keysService($http) {
        var service = {
            search: search,
            activeSession: activeSession
        };

        return service;

        function search(keyId) {
            return $http.get('/api/key/search/' + keyId.toString());
        }

        function activeSession(keyId) {
            return $http.get('/api/session/key/', keyId.toString());
        }
    }
})();