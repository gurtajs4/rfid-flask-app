function keysService($http) {
    var service = {
        lookup: lookup
    };

    return service;

    function lookup(keyId) {
        return $http.get('/api/lookup/key', keyId).then(function (response) {
            return response
        });
    }
}

keysService.$inject = ['$http'];
angular.module('appMain').service('keysService', keysService);