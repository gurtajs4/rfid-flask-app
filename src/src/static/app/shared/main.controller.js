(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('MainController', MainController);

    MainController.$inject = ['$scope', '$location'];
    function MainController($scope, $location) {
        $scope.isAuthenticated = false;
        $scope.globals = {};
        $scope.next = '';

        $scope.setCredentials = setCredentials;
        $scope.clearCredentials = clearCredentials;

        function loadNextUrl() {
            if ($scope.next.length != '') {
                var nextUrl = $scope.next;
                $scope.next = '';
                $location.url(nextUrl);
            }
        }

        function setCredentials(globals) {
            $scope.globals = globals;
            $scope.isAuthenticated = true;
            $location.url('/home');
        }

        function clearCredentials() {
            $scope.globals = {};
            $scope.isAuthenticated = false;
            $location.url('/home');
        }

        $scope.$on('$routeChangeStart', function (previous, next) {
            if (next.$$route != undefined) {
                var originalPath = next.$$route.originalPath;
                var _guestRoutes = guestRoutes();

                var locationAllowed = false;
                angular.forEach(_guestRoutes, function (value, key) {
                    if ($location.path.host + value == originalPath) {
                        locationAllowed = true;
                    }
                });

                if (!locationAllowed && !$scope.globals.hasOwnProperty('username') && !$scope.globals.hasOwnProperty('token')) {
                    $location.url('/login');
                }
            }
        });

        $scope.$on('$routeChangeSuccess', function (previous, current) {
            if (current.$$route != undefined) {
                if ($scope.next != '') {
                    loadNextUrl();
                }
            }
        });

        function guestRoutes() {
            return [
                '/',
                '/home',
                '/login',
                '/users/register'
            ]
        }
    }
})();