function peopleService($http) {
    var service = {
        //
    };

    return service;

    function lookup(userId) {
        return $http.get('/api/lookup/user', userId).then(function (response) {
            return response
        });
    }
}

peopleService.$inject = ['$http'];
angular.module('appMain').service('peopleService', peopleService);