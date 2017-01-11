(function () {
    'use strict';
    angular.module('appMain').service('usersService', usersService);
    usersService.$inject = ['$http'];
    function usersService($http) {
        var service = {
            search: search,
            getItems:getItems
        };

        return service;

        function search(username) {
            return $http.get('/api/user/search/' + username);
        }

        function getItems() {
            return $http.get('/api/users');
        }
    }
})();