function keysService($http) {
    var service = {
        lookup: lookup
    };

    return service;

    function lookup(keyId) {
        return $http.get('/api/lookup/key/' + keyId.toString()).then(function (response) {
            var key = {
                id: parseInt(response.data.key)
            };
            return key;
        });
    }
}

keysService.$inject = ['$http'];
angular.module('appMain').service('keysService', keysService);