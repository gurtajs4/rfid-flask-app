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
            service.initReader().then(function (response) {
                console.log('Ajax response for activating reader...');
                self.message = response.data['message'];
                self.tagData = response.data['data'];
            });
        }
    }
})();