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
            0: {route: '/', name: 'Home'},
            1: {route: 'sessions', name: 'Sessions'},
            2: {route: 'keys/search', name: 'Search Keys'},
            3: {route: 'users/search', name: 'Search Users'}
        };
        $scope.midNav = {
            4: {route: 'keys', name: 'Rooms/Keys'},
            5: {route: 'users', name: 'Users'}
        };
        $scope.rightNav = {
            6: {route: 'keys/register', name: 'Register Room/Key'},
            7: {route: 'users/register', name: 'Register User'}
        };

        function setActive(tabId) {
            $scope.tab = tabId;
        }

        function isActive(tabId) {
            return $scope.tab === tabId;
        }
    }
})();