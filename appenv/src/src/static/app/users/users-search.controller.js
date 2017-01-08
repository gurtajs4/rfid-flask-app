(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UsersSearchController', UsersSearchController);

    UsersSearchController.$inject = ['$location', '$log', 'usersService'];
    function UsersSearchController($location, $log, usersService) {
        var self = this;
        var service = usersService;

        self.title = "User Lookup Page";
        self.note = "Check for users by entering their name";
        self.submit = submit;
        self.cancel = cancel;
        self.results = [];

        function submit() {
            service.search(self.queryset).then(function (response) {
                $log.info(response.data);
                if (response.status == 200) {
                    self.results = response.data;
                }
                else {
                    $log.debug('Response status for users search is not 200: ' + response.data.message['message']);
                }
            }).catch(function (error) {
                $log.error(error.data);
            });
        }

        function cancel() {
            $location.url("/home");
        }
    }
})();