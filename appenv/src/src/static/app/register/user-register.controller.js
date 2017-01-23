(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    UserRegisterController.$inject = ['$scope', '$log', '$location', 'Upload', 'registerService', 'imagesService'];
    function UserRegisterController($scope, $log, $location, Upload, registerService, imagesService) {
        var service = registerService;
        var images = imagesService;

        $scope.title = "Person Registration Page";
        $scope.note = "Register person in the system by associating ID Card number with some personal information";

        $scope.tagData = "";
        $scope.message = "";

        $scope.register = register;
        $scope.cancel = cancel;
        $scope.isNotValid = isNotValid;


        function isNotValid() {
            return ($scope.tagData == '' || $scope.firstName == '' || $scope.lastName == '' || $scope.email == '' || $scope.role == '');
        }

        function register() {
            var user = {
                tag_id: $scope.tagData,
                first_name: $scope.firstName,
                last_name: $scope.lastName,
                email: $scope.email,
                role_id: $scope.role
            };
            $log.info('From client - raw user data is: ', user);
            var imgName = user.image.name;
            var imgType = user.image.type;
            $log.info('Image type is ', imgType);
            $log.info('Image name is ', imgName);
            Upload.upload({
                url: '/api/user/register',
                data: {file: $scope.image, 'user_json': JSON.parse(user), 'user': user}
            }).then(function (response) {
                $log.info('Success ' + response.config.data.file.name + 'uploaded. Response: ' + response.data);
            }, function (error) {
                $log.error('Error status: ' + error.status);
            }, function (evt) {
                var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                $log.info('progress: ' + progressPercentage + '% ' + evt.config.data.file.name);
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();