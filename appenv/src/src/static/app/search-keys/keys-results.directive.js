(function () {
    'use strict';
    angular
        .module('appMain')
        .directive('keysSearchResults', keysSearchResults);

    keysSearchResults.$inject = ['templateServiceProvider'];
    function keysSearchResults(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                results: '='
            },
            templateUrl: appBaseUrl+ '/search-keys/keys-results.html'
        };
    }
})();