(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('NavController', NavController);

    NavController.$inject = ['$scope'];
    function NavController($scope) {

        $scope.tab = 0;
        $scope.setActive = setActive;
        $scope.isActive = isActive;
        $scope.collapseNavbar = collapseNavbar;

        function setActive(tabId) {
            $scope.tab = tabId;
            collapseNavbar();
        }

        function isActive(tabId) {
            return $scope.tab === tabId;
        }

        function collapseNavbar() {
            $scope.navCollapsed = !$scope.navCollapsed;
        }
    }
})();