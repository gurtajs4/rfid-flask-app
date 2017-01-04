(function () {
    'use strict';
    angular
        .module('appMain')
        .directive('usersSearchResults', usersSearchResults);

    usersSearchResults.$inject = ['templateServiceProvider'];
    function usersSearchResults(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                results: '='
            },
            templateUrl: appBaseUrl+ '/users/users-results.html'
        };
    }
})();