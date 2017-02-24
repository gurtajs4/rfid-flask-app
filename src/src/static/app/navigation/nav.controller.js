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

        $scope.title = 'RFID sustav';
        $scope.leftNav = [
            {id: 0, route: '/', name: 'Naslovnica'},
            {id: 1, route: 'sessions', name: 'Preuzimanja ključeva'},
            {id: 2, route: 'keys/search', name: 'Pretraga ključeva'},
            {id: 3, route: 'users/search', name: 'Pretraga korisnika'}
        ];
        $scope.midNav = [
            {id: 4, route: 'keys', name: 'Prostorije'},
            {id: 5, route: 'users', name: 'Korisnici'}
        ];
        $scope.rightNav = [
            {id: 6, route: '/keys/seed', name: 'Uvoz ključeva'},
            {id: 7, route: 'keys/register', name: 'Registracija ključa'},
            {id: 8, route: 'users/register', name: 'Registracija korisnika'}
        ];

        $scope.$on('$routeChangeSuccess', function (previous, current) {
            if (current.$$route != undefined) {
                var originalPath = current.$$route.originalPath.substring(1);
                checkPath(originalPath);
            }
        });

        function setActive(tabId) {
            $scope.tab = tabId;
        }

        function isActive(tabId) {
            return $scope.tab === tabId;
        }

        function checkPath(originalPath) {
            var availableRoutes = $scope.leftNav.concat($scope.midNav.concat($scope.rightNav));
            if (originalPath == 'home') {
                setActive(0);
                return true;
            }
            for (var i = 0; i < availableRoutes.length; i++) {
                if (availableRoutes[i].route == originalPath) {
                    setActive(availableRoutes[i].id);
                    return true;
                }
            }
            return false;
        }
    }
})();