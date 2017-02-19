(function () {
    'use strict';

    angular
        .module('appMain')
        .directive('keyInfo', keyInfo);

    keyInfo.$inject = ['templateServiceProvider'];
    function keyInfo(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                key: '=keyInfo'
            },
            templateUrl: appBaseUrl + '/keys/key-info.html'
        };
    }
})();
