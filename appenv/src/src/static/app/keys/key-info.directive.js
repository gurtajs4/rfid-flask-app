(function () {
    'use strict';

    angular
        .module('appMain')
        .directive('infoKey', infoKey);

    infoKey.$inject = ['templateServiceProvider'];
    function infoKey(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'E',
            scope: '=',
            templateUrl: appBaseUrl + '/keys/key-info.html'
        };
    }
})();
