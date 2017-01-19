(function () {
    'use strict';

    angular
        .module('appMain')
        .directive('keySession', keySession);

    keySession.$inject = ['templateServiceProvider'];
    function keySession(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                result: '='
            },
            templateUrl: appBaseUrl + 'sessions/session-info.html',
            controller: 'KeySessionController',
            controllerAs: 'sessionInfo'
        };
    }
})();