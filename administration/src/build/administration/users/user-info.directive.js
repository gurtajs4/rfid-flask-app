(function () {
    'use strict';
    angular
        .module('appMain')
        .directive('userInfo', userInfo);

    userInfo.$inject = ['templateServiceProvider'];
    function userInfo(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                user: '=userInfo'
            },
            templateUrl: appBaseUrl + '/users/user-info.html'
        };
    }
})();