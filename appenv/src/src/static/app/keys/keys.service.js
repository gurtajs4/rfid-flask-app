(function () {
    'use strict';

    angular
        .module('appMain')
        .service('keysService', keysService);

    keysService.$inject = ['$http'];
    function keysService($http) {
        var service = {
            search: search,
            getItems: getItems,
            getItem: getItem
        };

        return service;

        function search(roomId) {
            return $http.get('/api/keys/search/' + roomId.toString());
        }

        function getItems() {
            return $http.get('api/keys');
        }

        function getItem(keyId) {
            return $http.get('/api/key/get/' + keyId.toString());
        }
    }
})();