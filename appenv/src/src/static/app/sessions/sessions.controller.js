function SessionsController(sessionService) {
    var self = this;
    var service = sessionService;

    self.list = [];

    load();

    function load() {
        service.sessions().then(function (response) {
            var data = response.data;
            var viewModel = new Array();
            for (i = 0; i < data.length; i++) {
                viewModel.push(JSON.parse(data[i]));
            }
            self.list = viewModel;
        });
    }
}

SessionsController.$inject = ['sessionService'];
angular.module('appMain').controller('SessionsController', SessionsController);