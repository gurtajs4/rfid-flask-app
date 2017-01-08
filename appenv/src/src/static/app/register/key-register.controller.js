(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeyRegisterController', KeyRegisterController);

    KeyRegisterController.$inject = ['$scope', '$log', '$location', 'registerService'];
    function KeyRegisterController($scope, $log, $location, registerService) {
        // var self = this;
        var service = registerService;

        // self.title = "Key/Room Registration Page";
        $scope.title = "Key/Room Registration Page";
        // self.note = "Register room key in the system by associating ID of key tag with some additional information about the room";
        $scope.note = "Register room key in the system by associating ID of key tag with some additional information about the room";

        // self.tagData = "";
        $scope.tagData = "";
        // self.message = "";
        $scope.message = "";

        $scope.register = register;
        $scope.cancel = cancel;
        // self.register = register;
        // self.cancel = cancel;

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
            var key = {
                id: -1,
                tag_id: $scope.tagData, //self.tagData,
                room_id: $scope.roomId  //self.roomId
            };
            $log.info('Key: ', key);
            service.registerKey(key).then(function (response) {
                if (response.status == 200) {
                    $location.url('/home');
                }
                else {
                    $log.info('Failed to create key...');
                }
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();