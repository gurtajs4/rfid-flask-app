(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    UserRegisterController.$inject = ['$scope', '$log', '$location', 'registerService'];
    function UserRegisterController($scope, $log, $location, registerService) {
        // var self = this;
        var service = registerService;

        // self.title = "Person Registration Page";
        // self.note = "Register person in the system by associating ID Card number with some personal information";
        $scope.title = "Person Registration Page";
        $scope.note = "Register person in the system by associating ID Card number with some personal information";

        // self.tagData = "";
        // self.message = "";
        $scope.tagData = "";
        $scope.message = "";

        // self.register = register;
        // self.cancel = cancel;
        $scope.register = register;
        $scope.cancel = cancel;

        $scope.$watch('tagData', function () {
            $log.info('Tag data is: ', $scope.tagData);
        });
        // $scope.$watch(angular.bind(self, function () {
        //     return self.tagData;
        // }), function (current, original) {
        //     $log.info('tagData was %s', original);
        //     $log.info('tagData is now %s', current);
        // });
        //
        // $scope.$watch(angular.bind(self, function () {
        //     return self.message;
        // }), function () {
        //     $log.info('message was %s', original);
        //     $log.info('message is now %s', current);
        // });

        function register() {
            var user = {
                id: -1,
                tag_id: $scope.tagData,         //self.tagData,
                first_name: $scope.firstName,   //self.firstName,
                last_name: $scope.lastName,     //self.lastName,
                pic_url: $scope.picUrl          //self.picUrl
            };
            $log.info('User: ', user);
            service.registerUser(user).then(function (response) {
                if (response.status == 200) {
                    $location.url('/home');
                }
                else {
                    $log.info('Failed to create user...');
                }
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();