(function () {
    'use strict';

    angular
        .module('appMain')
        .directive('navBar', navBar);

    navBar.$inject = ['templateServiceProvider'];
    function navBar(templateServiceProvider) {
        var sharedBaseUrl = templateServiceProvider.sharedBaseUrl();
        return {
            restrict: 'E',
            scope: false,
            templateUrl: sharedBaseUrl + '/navigation/navigation.html',
            controller: 'NavController'
        };
    }
})();