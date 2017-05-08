(function () {
    'use-strict';

    angular
        .module('appMain')
        .directive('authDashboard', authDashboard);

    authDashboard.$inject = ['templateServiceProvider'];
    function authDashboard(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'E',
            scope: false,
            controller: 'AuthDashboardController',
            templateUrl: appBaseUrl + '/auth-dashboard/auth-dashboard.html'
        }
    }
})();