function RegisterPersonController($location, registerService) {
    var self = this;
    var service = registerService;

    self.title = "Person Registration Page";
    self.note = "Register person in the system by associating ID Card number with some personal information";
    self.extendedNote = "Please move your ID card to the reader and the system will detect its unique number. The number will be displayed shortly after, and you can enter the rest of information then.";
    self.person = {};

    load();

    function load() {
        service.userId().then(function (userId) {
            self.person.userId = userId;    // obtain userId from tag to associate with person info
        });
    }

    function register() {
        //  creates person object and sends it to api/people/add/person/
    }

    function cancel() {
        $location.url('/home');
    }
}

RegisterPersonController.$inject = ['$location', 'registerService'];
angular.module('appMain').controller('RegisterPersonController', RegisterPersonController);