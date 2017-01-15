(function () {
    'use strict';

    angular
        .module('appMain')
        .service('userSessionsService', userSessionsService);

    userSessionsService.$inject = ['userSessionsService'];
    function userSessionsService($http) {
        var service = {
            getUserSessions: getUserSessions
        };

        return service;

        function getUserSessions(userId) {
            $http.get('/api/user/sessions/' + userId.toString());
        }
    }
})();