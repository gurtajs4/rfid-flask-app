(function () {
    'use-strict';

    angular
        .module('appMain')
        .controller('AuthDashboardController', AuthDashboardController);

    AuthDashboardController.$inject = ['$scope', '$location', 'authService'];
    function AuthDashboardController($scope, $location, authService) {
        var service = authService;

        $scope.logout = logout;

        function logout(callback) {
            service.clearCredentials(callback);
            $location.url('/home');
        }
    }
})();