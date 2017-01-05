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
            scope: 'keyId',
            templateUrl: appBaseUrl + '/keys/key-info.html'
        };
    }
})();
