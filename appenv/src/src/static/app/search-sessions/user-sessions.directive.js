(function () {
    'use strict';

    angular
        .module('appMain')
        .directive('userSessions', userSessions);

    userSessions.$inject = ['templateServiceProvider'];
    function userSessions(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                userId: '=user'
            },
            templateUrl: appBaseUrl + '/search-sessions/user-sessions.html',
            controller: 'UserSessionsController'
        };
    }
})();