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

        function setActive(tabId) {
            $scope.tab = tabId;
            $scope.navCollapsed = !$scope.navCollapsed
        }

        function isActive(tabId) {
            return $scope.tab === tabId;
        }
    }
})();