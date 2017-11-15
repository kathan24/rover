/**
 * Created by kathan
 */

angular.module('roverApp').factory('dashboardFactory', function ($q, $http) {

    var dashboard_factory = {};
    dashboard_factory.sitters = [];

    dashboard_factory.getSitters = function() {
        var d = $q.defer();

        if(dashboard_factory.sitters.length != 0){
            d.resolve(dashboard_factory.sitters);
            return d.promise;
        }

        $http({
            method: 'GET',
            url: '/data/sitters'
        }).then(function(response) {
            d.resolve(response.data);
        }, function(response) {
            d.reject(response);
        });
        return d.promise;
    };

    return dashboard_factory;
});