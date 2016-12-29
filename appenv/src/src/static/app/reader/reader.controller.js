(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['readerService'];
    function ReaderController(readerService) {
        var self = this;
        var service = readerService;

        activate();

        function activate() {
            service.tagRead().then(function (response) {
                if (response.status == 404) {
                    self.message = response.data.message;
                }
                else {
                    self.tagData = response.data.data;
                }
            });
        }
    }
})();