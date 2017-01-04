(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UsersSearchController', UsersSearchController);

    UsersSearchController.$inject = ['$location', 'usersService'];
    function UsersSearchController($location, usersService) {
        var self = this;
        var service = usersService;

        self.title = "User Lookup Page";
        self.note = "Check for users by entering their name";
        self.submit = submit;
        self.cancel = cancel;
        self.results = {};

        function submit() {
            return service.search(self.queryset).then(function (response) {
                if (response.status != 404) {
                    self.results = response.data;
                }
                else {
                    console.log(response.data.message['message']);
                    $window.alert("User not registered!");
                }
            });
        }

        function cancel() {
            $location.url("/home");
        }
    }
})();