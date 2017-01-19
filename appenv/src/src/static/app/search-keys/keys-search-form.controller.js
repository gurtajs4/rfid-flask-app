(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeysSearchController', KeysSearchController);

    KeysSearchController.$inject = ['$location', '$log', 'keysService'];
    function KeysSearchController($location, $log, keysService) {
        var self = this;
        var service = keysService;

        self.title = "Keys lookup page";
        self.note = "Check for keys by entering Key ID number";
        self.submit = submit;
        self.cancel = cancel;
        self.result = {};

        function submit() {
            service.search(self.queryset).then(function (response) {
                $log.info(response.data);
                if (response.status == 200) {
                    self.result = JSON.parse(response.data);
                }
                else {
                    $log.debug('Response status is not 200 for key search: ' + response.data['message']);
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