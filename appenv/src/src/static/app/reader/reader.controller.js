(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['readerService', '$socket'];
    function ReaderController(readerService, $socket) {
        var self = this;
        var service = readerService;

        activate();

        socket.on('reader-done', function (message) {
            console.log('Reader is done - socket-io event from server to client');
            console.log(message);
            self.tagData = message['message']['data'];
        });

        function activate() {
            $socket().then(function (socket) {
                console.log('creating socket instance');
                socket.on('connect', function () {
                    service.initReader().then(function (response) {
                        console.log('Ajax response for activating reader...');
                        console.log(response);
                        self.message = response.data.message;
                    });
                });
            });
            // service.initReader().then(function (response) {
            //     if (response.status == 404) {
            //         self.message = response.data.message;
            //     }
            //     else {
            //         self.tagData = response.data.data;
            //     }
            // });
        }
    }
})();