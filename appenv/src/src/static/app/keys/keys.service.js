(function () {
    'use strict';

    angular
        .module('appMain')
        .service('keysService', keysService);

    keysService.$inject = ['$http'];
    function keysService($http) {
        var service = {
            search: search,
            getItems: getItems
        };

        return service;

        function search(roomId) {
            return $http.get('/api/keys/search/' + roomId.toString());
        }

        function getItems() {
            return $http.get('api/keys');
        }
    }
})();