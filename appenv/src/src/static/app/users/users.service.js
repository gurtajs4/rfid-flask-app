(function () {
    'use strict';
    angular.module('appMain').service('usersService', usersService);
    usersService.$inject = ['$http'];
    function usersService($http) {
        var service = {
            search: search,
            getItems: getItems,
            getItem: getItem
        };

        return service;

        function search(queryset) {
            return $http.get('/api/user/search/' + queryset);
        }

        function getItems() {
            return $http.get('/api/users');
        }

        function getItem(userId) {
            return $http.get('/api/user/get/' + userId.toString());
        }
    }
})();