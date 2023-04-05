#!/usr/bin/ruby

require 'rbygem'
require 'mongo'
	
$client = Mongo::Client.new(['0.0.0.0:27017'], :database => 'ruby')
Mongo::Logger.logger.level = ::Logger::ERROR
$emp = $client[:emp]
puts 'connected!'
	
$emp.find({"deptno"=>30}).update_many({"$set" => {
	 "deptno" => 40

}})


cursor = $emp.find ()
cursor = cursor.each do | doc |
		puts doc
	
end


