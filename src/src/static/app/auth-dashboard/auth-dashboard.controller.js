(function () {
    'use-strict';

    angular
        .module('appMain')
        .controller('AuthDashboardController', AuthDashboardController);

    AuthDashboardController.$inject = ['$scope', '$location', 'authService', 'userService'];
    function AuthDashboardController($scope, $location, authService, userService) {
        $scope.logout = logout;
        $scope.editProfile = editProfile;

        init();

        $scope.$on('$routeChangeStart', function (previous, next) {
            var currentServiceUsername = authService.getCredentials().username;
            if ($scope.username != currentServiceUsername) {
                setUsername(currentServiceUsername);
            }
        });

        function init() {
            setUsername(authService.getCredentials().username);
        }

        function setUsername(username) {
            $scope.username = username;
        }

        function editProfile() {
            userService.search($scope.username)
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