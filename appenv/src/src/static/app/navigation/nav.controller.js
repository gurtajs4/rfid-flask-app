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

        $scope.title = 'RFID Sessions Site Dashboard';
        $scope.leftNav = {
            0: '/',
            1: 'sessions',
            2: 'keys/search',
            3: 'users/search'
        };
        $scope.midNav = {
            4: 'keys',
            5: 'users'
        };
        $scope.rightNav = {
            6: 'keys/register',
            7: 'users/register'
        };
        $scope.routeNames = {
            0: 'Home',
            1: 'Sessions',
            2: 'Search Keys',
            3: 'Search Users',
            4: 'Rooms/Keys',
            5: 'Users',
            6: 'Register Room/Key',
            7: 'Register User'
        };

        function setActive(tabId) {
            $scope.tab = tabId;
        }

        function isActive(tabId) {
            return $scope.tab === tabId;
        }
    }
})();