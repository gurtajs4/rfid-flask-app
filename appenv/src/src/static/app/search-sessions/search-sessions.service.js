(function () {
    'use strict';

    angular
        .module('appMain')
        .service('searchSessionsService', searchSessionsService);

    searchSessionsService.$inject = ['searchSessionsService'];
    function searchSessionsService($http) {
        var service = {
            getSessionsByKey:getSessionsByKey,
            getSessionsByUser: getSessionsByUser
        };

        return service;

        function getSessionsByKey(keyId) {
            return $http.get('/api/sessions/key/', keyId.toString());
        }

        function getSessionsByUser(userId) {
            return $http.get('/api/sessions/user/' + userId.toString());
        }
    }
})();