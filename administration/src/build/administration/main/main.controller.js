(function () {
    'use strict';

    angular
        .module('administration')
        .controller('MainController', MainController);

    MainController.$inject = ['$scope'];
    function MainController($scope) {

        init();

        function init() {
            console.log(document.cookie);
            if (!$scope.isUserAuthenticated) {
                $scope.isUserAuthenticated = (document.cookie.indexOf('token') > -1);
            }
        }
    }
})();