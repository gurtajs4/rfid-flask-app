(function () {
    'use strict';

    angular
        .module('appMain')
        .service('readerService', readerService);

    readerService.$inject = ['$http'];
    function readerService($http) {
        var service = {
            tagRead: tagRead
        };

        return service;

        function tagRead() {
            $http.get('api/reader/');
        }
    }
})();