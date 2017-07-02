(function () {
    'use-strict';

    angular
        .module('appMain')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$scope', '$log', '$location', 'authService'];
    function LoginController($scope, $log, $location, authService) {
        var service = authService;

        $scope.loginErrror = {};

        $scope.doLogin = doLogin;
        $scope.isValid = isValid;

        function isValid() {
            var _isValid = true;
            if (!$scope.email) {
                $scope.loginError.email = 'Ovo polje je obavezno!';
                _isValid = false;

            }
            if (!$scope.password) {
                $scope.loginError.password = 'Ovo polje je obavezno!';
                _isValid = false;

            }
            if ($scope.password.length < 9) {
                $scope.loginError.password = 'Lozinka je sigurna kao ima više od 8 znakova!';
                _isValid = false;

            }
            return _isValid;
        }

        function doLogin(callback) {
            if (isValid()) {
                $log.info('Entered the login controller...');
                service.login($scope.email, $scope.password)
                    .then(function (response) {
                        var token = response.data['token'];
                        service.setCredentials($scope.email, token, function () {
                            callback(response.data);
                            $location.url('/home');
                        });
                    })
                    .catch(function (error) {
                        $log.error(error);
                    });
            }
        }
    }
})();