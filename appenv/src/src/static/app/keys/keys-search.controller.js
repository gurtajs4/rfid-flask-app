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
        self.keyId = {};
        self.result = {};

        function submit() {
            service.search(self.queryset).then(function (response) {
                if (response.status != 404) {
                    self.keyId = response.data;
                }
                else {
                    console.log(response.data['message']);
                    $window.alert("Key not registered!");
                }
            });
        }

        function cancel() {

            $location.url("/home");
        }
    }
})();