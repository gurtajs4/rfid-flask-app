(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    UserRegisterController.$inject = ['$location', 'registerService'];
    function UserRegisterController($location, registerService) {
        var self = this;
        var service = registerService;

        self.title = "Person Registration Page";
        self.note = "Register person in the system by associating ID Card number with some personal information";
        self.tagData = "";
        self.message = "";

        self.register = register;
        self.cancel = cancel;

        function register() {
            //  creates person object and sends it to api/people/add/person/
            var user = {
                id: -1,
                tag_id: self.tagData,
                first_name: self.firstName,
                last_name: self.lastName,
                pic_url: self.picUrl
            };
            console.log('UserId:' + user.id);
            console.log('TagId:' + user.tag_id);
            console.log('FirstName:' + user.first_name);
            console.log('LastName:' + user.last_name);
            service.registerUser(user).then(function (response) {
                if (response.status == 200) {
                    $location.url('/home');
                }
                else {
                    console.log('Failed to create user...');
                }
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();