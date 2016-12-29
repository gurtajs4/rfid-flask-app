(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('PeopleLookupController', PeopleLookupController);

    PeopleLookupController.$inject = ['$location', 'peopleService'];
    function PeopleLookupController($location, peopleService) {
        var self = this;
        var service = peopleService;

        self.title = "People Lookup Page";
        self.note = "Check for people by entering Person ID";
        self.lookup = lookup;
        self.cancel = cancel;

        function lookup() {
            return service.lookup(self.queryset).then(function (response) {
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