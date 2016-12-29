(function () {
    'use strict';

    angular
        .module('appMain')
        .service('sessionService', SessionService);

    SessionService.$inject = ['$http'];
    function SessionService($http) {

        var service = {
            sessions: sessions,
            session: session
        };

        return service;

        function sessions() {
            return $http.get('/api/sessions');
        }

        function session(id) {
            return $http.get('/api/sessions/' + id.toString());
        }
    }
})();