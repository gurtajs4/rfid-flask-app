(function () {
    'use-strict';

    angular
        .module('appMain')
        .controller('AuthDashboardController', AuthDashboardController);

    AuthDashboardController.$inject = ['$scope', '$location', 'authService', 'usersService'];
    function AuthDashboardController($scope, $location, authService, usersService) {
        $scope.logout = logout;
        $scope.editProfile = editProfile;

        $scope.$on('$routeChangeStart', function (event, newUrl, oldUrl) {
            if (authService.getCredentials != undefined) {
                console.log('From auth dashboard ', event);
                console.log('From auth dashboard ', newUrl);
                console.log('From auth dashboard ', oldUrl);
                var userCredentials = authService.getCredentials();
                console.log('From auth dashboard ', userCredentials);
                if (userCredentials) {
                    if (userCredentials.hasOwnProperty('username')) {
                        var currentServiceUsername = userCredentials.username;
                        console.log('From auth dashboard ', currentServiceUsername);
                        console.log('From auth dashboard ', $scope.username);
                        if ($scope.username != currentServiceUsername) {
                            setUsername(currentServiceUsername);
                        }
                    }
                }
            }
        });

        function setUsername(username) {
            $scope.username = username;
        }

        function editProfile() {
            usersService.search($scope.username)
                .then(function (response) {
                    var userId = null;
                    angular.forEach(response.data, function (value, key) {
                        var user = JSON.parse(value);
                        if (user) {
                            userId = user.id;
                        }
                    });
                    if (userId) {
                        $location.url('/users/edit/' + userId.toString());
                    }
                });
        }

        function logout() {
            authService.clearCredentials();
            $location.url('/home');
        }
    }
})();