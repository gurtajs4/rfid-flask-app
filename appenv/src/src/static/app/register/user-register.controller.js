(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    UserRegisterController.$inject = ['$scope', '$log', '$location', 'registerService'];
    function UserRegisterController($scope, $log, $location, registerService) {
        var self = this;
        var service = registerService;

        self.title = "Person Registration Page";
        self.note = "Register person in the system by associating ID Card number with some personal information";

        self.register = register;
        self.cancel = cancel;

        $scope.$watch(angular.bind(self, function () {
            return self.tagData;
        }), function (current, original) {
            $log.info('tagData was %s', original);
            $log.info('tagData is now %s', current);
        });

        $scope.$watch(angular.bind(self, function () {
            return self.message;
        }), function () {
            $log.info('tagData was %s', original);
            $log.info('tagData is now %s', current);
        });

        function register() {
            var user = {
                id: -1,
                tag_id: self.tagData,
                first_name: self.firstName,
                last_name: self.lastName,
                pic_url: self.picUrl
            };
            console.log('User: ', user);
            service.registerUser(user).then(function (response) {
                if (response.status == 200) {
                    $location.url('/home');
                }
                else {
                    window.alert('Failed to create user...');
                    console.log('Failed to create user...');
                }
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();