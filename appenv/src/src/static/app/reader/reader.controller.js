(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['readerService', '$socket'];
    function ReaderController(readerService, $socket) {
        var self = this;
        var service = readerService;

        // activate();
        self.socketId = '';

        function activate(socket) {
            self.message = 'Reader will be active for the next 20 seconds...';
            // service.initReader().then(function (response) {
            //     console.log('Ajax response for activating reader...');
            //     console.log(response);
            //     // self.message = response.data.message;
            // });

            if (self.socketId === '') {
                socket.emit('sid request');
                socket.on('sid response', function (sid) {
                    self.socketId = sid;
                });
            }

            socket.emit('init reader', {room: self.socketId});
        }

        $socket().then(function (socket) {
            console.log('creating socket instance');

            activate(socket);

            var readerEvent = {
                event: 'reader done',
                room: self.socketId
            };
            socket.on(JSON.stringify(readerEvent), function (message) {
                console.log('Reader is done - socket-io event from server to client');
                console.log(message);
                self.tagData = message['message']['data'];
            });
        });
    }
})();