function RegisterKeyController($location, registerService) {
    var self = this;
    var service = registerService;

    self.title = "Key/Room Registration Page";
    self.note = "Register room key in the system by associating ID of key tag with some additional information about the room";
    self.extendedNote = "Please move the key tag (keychain) to the reader and the system will detect its unique number. The number will be displayed shortly after, and you can enter the rest of information then.";
    self.keyInfo = {};

    load();

    function load() {
        service.keyId().then(function (keyId) {
            self.keyInfo.keyId = keyId;    // obtain keyId from tag to associate with additional info about that room
        });
    }

    function register() {
        //  joins key ID with additional some information and sends it to api/people/add/key/
    }

    function cancel() {
        $location.url('/home');
    }
}

RegisterKeyController.$inject = ['$location', 'registerService'];
angular.module('appMain').controller('RegisterKeyController', RegisterKeyController);