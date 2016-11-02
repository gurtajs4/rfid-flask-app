function registerService($http) {
    var service = {
        userId: userId,
        keyId: keyId,
    };

    return service;

    function userId() {
        return $http.get('/api/register/user').then(function (response) {
            return response.data;   // returns user ID
        });
    };

    function keyId() {
        return $http.get('/api/register/key').then(function (response) {
            return response.data;   // returns key ID
        });
    };
}

registerService.$inject = ['$http'];
angular.module('appMain').service('registerService', registerService);