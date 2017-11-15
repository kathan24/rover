/**
 * Created by kathan
 */
var roverApp = angular.module('roverApp', ['ngMaterial']);

roverApp.controller('dashboardController', function dashboardController($scope, dashboardFactory) {

    $scope.sitters = [];
    $scope.searchText = '';
    $scope.rating = 0;


    $scope.init = function(){
        dashboardFactory.getSitters().then(function(data){
            $scope.sitters = data;
        })

    };

    $scope.init();
});

roverApp.filter('ratingFilter', function() {
    return function(sitter_list, invert_rating) {
        var filtered_list = [];
        for(var i = 0; i < sitter_list.length; i++){
            if(sitter_list[i].rating_score >= invert_rating){
                filtered_list.push(sitter_list[i]);
            }
        }
        return filtered_list
    };
});