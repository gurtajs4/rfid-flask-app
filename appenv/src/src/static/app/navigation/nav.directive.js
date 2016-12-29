(function () {
    'use strict';
    angular.module('appMain').directive('navBar', navBar);
    function navBar() {
        return {
            restrict: 'E',
            scope: true,
            templateUrl: '/navigation/navigation.html',
            controller: 'NavController'
        };
    }
})();