(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    UserRegisterController.$inject = ['$scope', '$log', '$location', 'registerService'];
    function UserRegisterController($scope, $log, $location, registerService) {
        var service = registerService;

        $scope.title = "Person Registration Page";
        $scope.note = "Register person in the system by associating ID Card number with some personal information";

        $scope.tagData = "";
        $scope.message = "";

        $scope.register = register;
        $scope.cancel = cancel;

        function register() {
            var user = {
                id: -1,
                tag_id: $scope.tagData,
                first_name: $scope.firstName,
                last_name: $scope.lastName,
                pic_url: $scope.picUrl
            };
            $log.info('User: ', user);
            service.registerUser(user)
                .then(function (response) {
                    if (response.status == 200) {
                        $location.url('/home');
                    }
                    else {
                        $log.debug('Response status is not 200 on registering user: ' + response.data);
                    }
                })
                .catch(function (error) {
                    $log.error('Failed to create user... ' + error.data);
                });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();