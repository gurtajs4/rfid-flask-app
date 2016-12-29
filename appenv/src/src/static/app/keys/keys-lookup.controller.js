(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeysLookupController', KeysLookupController);

    KeysLookupController.$inject = ['$location', 'keysService'];
    function KeysLookupController($location, keysService) {
        var self = this;
        var service = keysService;

        self.title = "Keys lookup page";
        self.note = "Check for keys by entering Key ID number";
        self.lookup = lookup;
        self.cancel = cancel;

        function lookup() {
            return service.lookup(self.queryset).then(function (response) {
                if (response.status != 404) {
                    $location.url("/sessions/" + response.data.session.id);
                }
                else {
                    console.log('Request didn\'t came through...');
                    $window.alert("Key not registered!");
                }
            });
        }

        function cancel() {

            $location.url("/home");
        }
    }
})();