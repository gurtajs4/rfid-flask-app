(function () {
    'use strict';

    angular
        .module('appMain')
        .service('keysService', keysService);

    keysService.$inject = ['$http'];
    function keysService($http) {
        var service = {
            search: search
        };

        return service;

        function search(keyId) {
            return $http.get('/api/key/search/', {
                params: {
                    key_id: keyId
                }
            }).then(function (response) {
                var key = {
                    id: parseInt(response.data.key)
                };
                return key;
            });
        }
    }
})();