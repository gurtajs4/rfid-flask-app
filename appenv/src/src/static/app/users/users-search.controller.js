(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UsersSearchController', UsersSearchController);

    UsersSearchController.$inject = ['$location', 'usersService'];
    function UsersSearchController($location, usersService) {
        var self = this;
        var service = usersService;

        self.title = "People Lookup Page";
        self.note = "Check for people by entering Person ID";
        self.submit = submit;
        self.cancel = cancel;

        function submit() {
            return service.search(self.queryset).then(function (response) {
                if (response.status != 404) {
                    $location.url("/sessions/" + response.data.session.id);
                }
                else {
                    console.log('Request didn\'t came through...');
                    $window.alert("User not registered!");
                }
            });
        }

        function cancel() {
            $location.url("/home");
        }
    }
})();