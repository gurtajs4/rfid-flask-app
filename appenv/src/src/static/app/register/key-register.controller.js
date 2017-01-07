(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeyRegisterController', KeyRegisterController);

    KeyRegisterController.$inject = ['$location', 'registerService'];
    function KeyRegisterController($location, registerService) {
        var self = this;
        var service = registerService;

        self.title = "Key/Room Registration Page";
        self.note = "Register room key in the system by associating ID of key tag with some additional information about the room";

        self.register = register;
        self.cancel = cancel;

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