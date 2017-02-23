(function () {
    'use strict';

    angular.module('appMain').directive('templateDownload', templateDownload);

    templateDownload.$inject = ['templateServiceProvider'];
    function templateDownload(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: false,
            templateUrl: appBaseUrl + '/template-download/template-download.html'
        };
    }
})();