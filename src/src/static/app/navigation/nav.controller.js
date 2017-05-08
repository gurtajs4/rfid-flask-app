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
            {id: 3, route: '/keys/seed', name: 'Uvoz ključeva'},
            {id: 4, route: 'keys/register', name: 'Registracija ključa'},
            {id: 5, route: 'keys', name: 'Prostorije'}
        ];
        $scope.midNav = [
            {id: 6, route: 'users', name: 'Korisnici'},
            {id: 7, route: 'users/search', name: 'Pretraga korisnika'}
        ];
        $scope.rightNav = [
            {id: 8, route: '/login', name: 'Prijava korisnika'},
            {id: 9, route: 'users/register', name: 'Registracija korisnika'}
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