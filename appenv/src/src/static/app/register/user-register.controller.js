(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    UserRegisterController.$inject = ['$scope', '$log', '$location', '$timeout', 'registerService', 'imagesService'];
    function UserRegisterController($scope, $log, $location, $timeout, registerService, imagesService) {
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
                role_id: $scope.role,
                image: $scope.image
            };
            $log.info('From client - raw user data is: ', user);
            $log.info('From client - user image type - ', user.image.type);
            images.readImageFile(user.image, function (img_uri) {
                if (null !== img_uri) {
                    user.image = img_uri;
                    $log.info('From client - user image uri - ', user.image);
                    var user_json = JSON.parse(user);
                    $log.info('From client - JSON user data is: ', user_json);
                }
                $log.error('Image cannot be parsed...');
            });
            // service.registerUser(user)
            //     .then(function (response) {
            //         if (response.status == 200 || response.data.message['status'] == 200) {
            //             $log.info('Registered user: ', response.data.message);
            //             $location.url('/home');
            //         }
            //         else {
            //             $log.debug('Response status is not 200 on registering user: ' + response.data);
            //         }
            //     })
            //     .catch(function (error) {
            //         $log.error('Failed to create user... From server - ' + error.data);
            //     });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();
/*
 var image = $scope.image;

 $log.info('From client - image url: ', image);
 // store image first & retrieve new url
 images.uploadImageToServer(image)
 .then(function (response) {
 if (response != null) {
 var picUrl = response.data.message['pic_url'];
 var picId = response.data.message['pic_id'];
 $log.info('From client - stored url: ', picUrl);
 // combine new url of image with the rest of user data
 user.pic_url = picUrl;
 $log.info('From client - user to be registered: ', user);

 $log.info('From client - stored pic id: ', picId);
 user.pic_id = picId;
 $log.info('From client - user to be registered: ', user);
 }
 else {
 user.pic_url = '';
 user.pic_id = -1;
 }

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
 $log.error('Failed to create user... From server - ' + error.data);
 });
 });

 */

// **********  Uncomment only in extreme necessity  **********
/*
 $scope.readImageFile = readImageFile;

 function readImageFile(file) {
 if (file) {
 images.readImageFile(file, function (img) {
 $timeout(function () {
 if (img) {
 $scope.apply(function () {
 $scope.image = img;
 $log.info('From client - image src has been updated');
 });
 }
 }, 0);
 });
 }
 }
 */