function peopleService($http) {
    var service = {
        lookup: lookup
    };

    return service;

    function lookup(userId) {
        return $http.get('/api/lookup/user/', {params:{
            user_id: userId
        }}).then(function (response) {
            var person = {
                id: parseInt(response.data.user)
            };
            return person;
        });
    }
}

peopleService.$inject = ['$http'];
angular.module('appMain').service('peopleService', peopleService);