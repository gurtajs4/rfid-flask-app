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
                id: '=',
                tag_id: '=',
                first_name: '=',
                last_name: '=',
                pic_url: '='
            },
            templateUrl: appBaseUrl + '/users/user-info.html'
        };
    }
})();