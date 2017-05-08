(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('MainController', MainController);

    MainController.$inject = ['$scope'];
    function MainController($scope) {
        $scope.isAuthenticated = false;
        $scope.globals = {};

        $scope.setCredentials = setCredentials;
        $scope.clearCredentials = clearCredentials;

        function setCredentials(globals) {
            $scope.globals = globals;
            $scope.isAuthenticated = true;
        }

        function clearCredentials() {
            $scope.globals = {};
            $scope.isAuthenticated = false;
        }
    }
})();