(function () {
    'use strict';
    angular.module('appMain').service('peopleService', peopleService);
    peopleService.$inject = ['$http'];
    function peopleService($http) {
        var service = {
            lookup: lookup
        };

        return service;

        function lookup(userId) {
            return $http.get('/api/lookup/user/', {
                params: {
                    user_id: userId
                }
            }).then(function (response) {
                var person = {
                    id: parseInt(response.data.user)
                };
                return person;
            });
        }
    }
})();