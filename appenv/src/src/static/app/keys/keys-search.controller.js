(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeysSearchController', KeysSearchController);

    KeysSearchController.$inject = ['$location', 'keysService'];
    function KeysSearchController($location, keysService) {
        var self = this;
        var service = keysService;

        self.title = "Keys lookup page";
        self.note = "Check for keys by entering Key ID number";
        self.submit = submit;
        self.cancel = cancel;

        function submit() {
            return service.search(self.queryset).then(function (response) {
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