function keysService($http) {
    var service = {
        lookup: lookup
    };

    return service;

    function lookup(keyId) {
        return $http.get('/api/lookup/key/', {params: {
            key_id: keyId
        }}).then(function (response) {
            var key = {
                id: parseInt(response.data.key)
            };
            return key;
        });
    }
}

keysService.$inject = ['$http'];
angular.module('appMain').service('keysService', keysService);