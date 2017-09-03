(function () {
    'use strict';

    angular
        .module('administration')
        .controller('MainController', MainController);

    MainController.$inject = ['$scope', 'authService'];
    function MainController($scope, authService) {

        $scope.isAuthenticated = isUserAuthenticated;

        function isUserAuthenticated() {
            return authService.isAuthenticated();
        }
    }
})();