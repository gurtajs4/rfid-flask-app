(function () {
    'use strict';

    angular
        .module('appMain')
        .service('keysService', keysService);

    keysService.$inject = ['$http'];
    function keysService($http) {
        var service = {
            search: search,
            activeSession: activeSession,
            getItems: getItems
        };

        return service;

        function search(roomId) {
            return $http.get('/api/key/search/' + roomId.toString());
        }

        function activeSession(keyId) {
            return $http.get('/api/session/key/', keyId.toString());
        }

        function getItems() {
            return $http.get('api/keys');
        }
    }
})();