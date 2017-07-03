(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('NavController', NavController);

    NavController.$inject = ['$scope', '$location', 'authService'];
    function NavController($scope, $location, authService) {
        $scope.isAuthenticated = false;
        $scope.tab = 0;
        $scope.setActive = setActive;
        $scope.isActive = isActive;

        $scope.title = 'RFID sustav';
        $scope.leftNav = [
            {id: 0, route: '/', name: 'Naslovnica'},
            {id: 1, route: '/sessions', name: 'Preuzimanja ključeva'},
            {id: 2, route: '/keys/search', name: 'Pretraga ključeva'},
            {id: 3, route: '/keys/seed', name: 'Uvoz ključeva'},
            {id: 4, route: '/keys/register', name: 'Registracija ključa'},
            {id: 5, route: '/keys', name: 'Prostorije'}
        ];
        $scope.midNav = [
            {id: 6, route: '/users', name: 'Korisnici'},
            {id: 7, route: '/users/search', name: 'Pretraga korisnika'}
        ];
        $scope.rightNav = [
            {id: 8, route: '/login', name: 'Prijava korisnika'},
            {id: 9, route: '/users/register', name: 'Registracija korisnika'}
        ];

        $scope.$on('$routeChangeStart', function (event, newUrl, oldUrl) {
            if (newUrl.$$route != undefined) {
                console.log('From naviagation ', event);
                console.log('From naviagation ', newUrl);
                console.log('From naviagation ', oldUrl);
                var originalPath = newUrl.$$route.originalPath;
                var _guestRoutes = guestRoutes();
                console.log('From naviagation ', originalPath);
                console.log('From naviagation ', _guestRoutes);
                var doReturn = false;
                angular.forEach(_guestRoutes, function (value, key) {
                    if (value == originalPath) {
                        doReturn = true;
                    }
                });

                console.log('From naviagation ', doReturn);
                if (doReturn) {
                    return;
                }

                console.log('From naviagation ', $scope.isAuthenticated);
                if (authService.getCredentials != undefined) {
                    $scope.isAuthenticated = !!authService.getCredentials();
                }
                else {
                    $scope.isAuthenticated = false;
                }

                console.log('From naviagation ', $scope.isAuthenticated);
                if (!$scope.isAuthenticated) {
                    event.preventDefault();
                    $location.url('/login');
                }
            }
        });

        $scope.$on('$routeChangeSuccess', function (event, newUrl, oldUrl) {
            if (newUrl.$$route != undefined) {
                var originalPath = newUrl.$$route.originalPath.substring(1);
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

        function guestRoutes() {
            return [
                '/home',
                '/login',
                '/users/register'
            ]
        }
    }
})();