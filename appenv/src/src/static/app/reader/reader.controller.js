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
                console.log(response);
                console.log('self.message: ', self.message);
                console.log('self.tagData: ', self.tagData);
                self.$apply(function () {
                    self.message = response.data.message['message'];
                    self.tagData = response.data.message['data'];
                    console.log('self.message: ', self.message);
                    console.log('self.tagData: ', self.tagData);
                });
                console.log('self.message: ', self.message);
                console.log('self.tagData: ', self.tagData);
            });
        }

        /*
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
         });*/
    }
})();