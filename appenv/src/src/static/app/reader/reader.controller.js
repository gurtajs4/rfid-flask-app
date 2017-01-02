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

        function activate() {
            $socket().then(function (socket) {
                console.log('creating socket instance');
                socket.on('connect', function (message) {
                    socket.emit('message', {
                        message: 'hello-from-client'
                    });
                });
                socket.on('reader-done', function (message) {
                    console.log(message);
                    self.tagData = message['message']['data'];
                });
            });
            service.initReader().then(function (response) {
                self.message = response.data.message;
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