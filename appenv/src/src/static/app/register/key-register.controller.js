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
        self.tagData = "";

        self.register = register;
        self.cancel = cancel;

        function register() {
            //  joins key ID with additional some information and sends it to api/people/add/key/
            var key = {
                id: -1,
                tag_id: self.tagData, // obtain tagData from tag to associate with additional info about that room
                room_id: self.roomId
            };
            console.log('KeyId:' + key.id);
            console.log('TagId:' + key.tag_id);
            console.log('RoomId:' + key.room_id);
            service.registerKey(key).then(function (response) {
                if (response.status == 200) {
                    $location.url('/home');
                }
                else {
                    console.log('Failed to create key...');
                }
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();