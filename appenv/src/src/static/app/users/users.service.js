(function () {
    'use strict';
    angular.module('appMain').service('usersService', usersService);
    usersService.$inject = ['$http'];
    function usersService($http) {
        var service = {
            search: search
        };

        return service;

        function search(username) {
            return $http.get('/api/user/search/', {
                params: {
                    user_name: username
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