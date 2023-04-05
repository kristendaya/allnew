#!/usr/bin/ruby

require 'rbygem'
require 'mongo'
	
$client = Mongo::Client.new(['127.0.0.1:27017'], :database => 'ruby')
Mongo::Logger.logger.level = ::Logger::ERROR
$emp = $client[:emp]
puts 'connected!'
	
$emp.drop()
	
$emp.insert_one({"eno"=>7499, "ename"=>"ALLEN", "job"=> "SALESMAN", "sal"=>1250, "deptno" => 30})
$emp.insert_one({"eno"=>7698, "ename"=>"BLAKE", "job"=> "SALESMAN", "sal"=>2250, "deptno" => 30})
$emp.insert_one({"eno"=>7782, "ename"=>"CLARK", "job"=> "SALESMAN", "sal"=>2350, "deptno" => 30})
$emp.insert_one({"eno"=>7934, "ename"=>"DAVID", "job"=> "SALESMAN", "sal"=>2200, "deptno" => 30})
$emp.insert_one({"eno"=>7902, "ename"=>"FORD", "job"=> "MANAGER", "sal"=>3500,"comm"=>2000, "deptno" => 20})
$emp.insert_one({"eno"=>7900, "ename"=>"JAMES", "job"=> "ANALYST", "sal"=>3800,"comm"=>2400, "deptno" => 20})
$emp.insert_one({"eno"=>7566, "ename"=>"JONES", "job"=> "SALESMAN", "sal"=>1250, "deptno" => 30})
$emp.insert_one({"eno"=>7654, "ename"=>"MARTIN", "job"=> "MANAGER", "sal"=>2280,"comm"=>2400, "deptno" => 30})
$emp.insert_one({"eno"=>7839, "ename"=>"PRESIDENT", "job"=> "CEO", "sal"=>5000,"comm"=>4400, "deptno" => 10})
cursor = $emp.find()
cursor.each do |doc|
	puts doc
end

