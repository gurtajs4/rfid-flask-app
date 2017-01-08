(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeyRegisterController', KeyRegisterController);

    KeyRegisterController.$inject = ['$scope', '$log', '$location', 'registerService'];
    function KeyRegisterController($scope, $log, $location, registerService) {
        var self = this;
        var service = registerService;

        self.title = "Key/Room Registration Page";
        self.note = "Register room key in the system by associating ID of key tag with some additional information about the room";

        self.tagData = "";
        self.message = "";

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
            $log.info('message was %s', original);
            $log.info('message is now %s', current);
        });

        function register() {
            var key = {
                id: -1,
                tag_id: self.tagData,
                room_id: self.roomId
            };
            console.log('Key:', key);
            service.registerKey(key).then(function (response) {
                if (response.status == 200) {
                    $location.url('/home');
                }
                else {
                    window.alert('Failed to create key...');
                    console.log('Failed to create key...');
                }
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();