(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeyRegisterController', KeyRegisterController);

    KeyRegisterController.$inject = ['$scope', '$log', '$location', 'registerService'];
    function KeyRegisterController($scope, $log, $location, registerService) {
        var service = registerService;

        $scope.title = "Key/Room Registration Page";
        $scope.note = "Register room key in the system by associating ID of key tag with some additional information about the room";

        $scope.tagData = "";
        $scope.message = "";

        $scope.register = register;
        $scope.cancel = cancel;

        function register() {
            var key = {
                id: -1,
                tag_id: $scope.tagData,
                room_id: $scope.roomId
            };
            $log.info('Key: ', key);
            service.registerKey(key)
                .then(function (response) {
                    if (response.data.status == 200) {
                        $location.url('/home');
                    }
                    else {
                        $log.debug('Response status is not 200 on registering key: ' + response.data);
                    }
                })
                .catch(function (error) {
                    $log.error('Failed to create key... ' + error.data);
                });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();