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
            service.initReader().then(function (response) {
                console.log('Ajax response for activating reader...');
                console.log(response);
                self.message = response.data.message;
            });
        }

        $socket().then(function (socket) {
            console.log('creating socket instance');
            // socket.on('connect', function () {
            // });
            socket.emit('request-sid');

            socket.on('response-sid', function (sid) {
                self.socket_id = sid;
            });

            socket.on('reader-done-' + self.socket_id, function (message) {
                console.log('Reader is done - socket-io event from server to client');
                console.log(message);
                self.tagData = message['message']['data'];
            });
        });
    }
})();