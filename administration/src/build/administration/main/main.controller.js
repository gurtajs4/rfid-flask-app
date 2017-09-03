(function () {
    'use strict';

    angular
        .module('administration')
        .controller('MainController', MainController);

    MainController.$inject = ['$scope', 'authService'];
    function MainController($scope, authService) {

        $scope.isUserAuthenticated = false;

        init();

        function init() {
            $scope.isUserAuthenticated = authService.isAuthenticated();
            console.log($scope.isUserAuthenticated);
        }
    }
})();