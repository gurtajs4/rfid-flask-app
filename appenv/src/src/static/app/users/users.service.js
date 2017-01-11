(function () {
    'use strict';
    angular.module('appMain').service('usersService', usersService);
    usersService.$inject = ['$http'];
    function usersService($http) {
        var service = {
            search: search,
            getAllItems:getAllItems
        };

        return service;

        function search(username) {
            return $http.get('/api/user/search/' + username);
        }

        function getAllItems() {
            return $http.get('/api/users');
        }
    }
})();