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
        $scope.leftNav = [
            {id: 0, route: '/', name: 'Home'},
            {id: 1, route: 'sessions', name: 'Sessions'},
            {id: 2, route: 'keys/search', name: 'Search Keys'},
            {id: 3, route: 'users/search', name: 'Search Users'}
        ];
        $scope.midNav = [
            {id: 4, route: 'keys', name: 'Rooms/Keys'},
            {id: 5, route: 'users', name: 'Users'}
        ];
        $scope.rightNav = [
            {id: 6, route: 'keys/register', name: 'Register Room/Key'},
            {id: 7, route: 'users/register', name: 'Register User'}
        ];

        $scope.$on('$routeChangeSuccess', function(previous, current) {
            console.log(previous);
            console.log(current);
            console.log(current.$$route);
            console.log(current.$$route.originalPath);
         });

        function setActive(tabId) {
            $scope.tab = tabId;
        }

        function isActive(tabId) {
            return $scope.tab === tabId;
        }
    }
})();