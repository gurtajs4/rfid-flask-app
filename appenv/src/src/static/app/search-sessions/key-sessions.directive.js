(function () {
    'use strict';

    angular
        .module('appMain')
        .directive('keySessions', keySessions);

    keySessions.$inject = ['templateServiceProvider'];
    function keySessions(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                key: '=keyId'
            },
            templateUrl: appBaseUrl + 'search-sessions/key-sessions.html',
            controller: 'KeySessionsController'
        };
    }
})();