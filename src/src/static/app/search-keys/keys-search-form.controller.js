(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeysSearchController', KeysSearchController);

    KeysSearchController.$inject = ['$location', '$log', 'keysService'];
    function KeysSearchController($location, $log, keysService) {
        var self = this;
        var service = keysService;

        self.submit = submit;
        self.cancel = cancel;
        self.results = [];

        function submit() {
            service.search(self.queryset).then(function (response) {
                var data = response.data;
                $log.info(data);
                var viewModel = [];
                angular.forEach(data, function (value, key) {
                    var singleViewModel = JSON.parse(value);
                    this.push(singleViewModel);
                }, viewModel);
                self.results = viewModel;
            }).catch(function (error) {
                $log.error(error.data);
            });
        }

        function cancel() {

            $location.url("/home");
        }
    }
})();