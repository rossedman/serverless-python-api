'use strict';

var AWS = require('aws-sdk');
var dynamodb = new AWS.DynamoDB({apiVersion: '2012-08-10'});

module.exports.handler = function(event, context, cb) {
  dynamodb.scan({
      TableName : "dev-serverless-pets",
      Limit : 10
  }, function(err, data) {
      if (err) {
          context.done('error','reading dynamodb failed: '+err);
      }
      for (var i in data.Items) {
          i = data.Items[i];
          console.log(i);
      }
  });

  return cb(null, {
    message: 'Go Serverless! Your Lambda function executed successfully!'
  });
};
