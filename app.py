#!/usr/bin/env python3

from aws_cdk import core


#from new.new_stack import NewStack

from resource_stack.customvpc_stack import Customvpc

from resource_stack.MyEc2Stack import MyEc2Stack

from  resource_stack.MyEc2AsgStack import MyEc2AsgStack

from   resource_stack.SecretStack import  MySecretStack





app = core.App()

print(app.node.try_get_context('envs')['prod']['ohio'])

core.Tag.add(app,key="OwnerMail",value=app.node.try_get_context('envs')['prod']['mail'])

env_US=core.Environment(account=app.node.try_get_context('envs')['prod']['account'],
                        region=app.node.try_get_context('envs')['prod']['region'])

env_oh=core.Environment(account=app.node.try_get_context('envs')['prod']['account'],
                        region=app.node.try_get_context('envs')['prod']['ohio'])
#env_Europe=core.Environment(account=app.node.try_get_context('dev')['account'],region=app.node.try_get_context('dev')['region'])

#print(app.node.try_get_context('dev')['region'])

#print(app.node.try_get_context('@aws-cdk/core:enableStackNameDuplicates'))

#VPC Stack
 
#Customvpc(app,"myvpcstack",env=env_US)  

 


#EC2 Stack 1
#MyEc2Stack(app,"MyEc2Stack",env=env_US) 

#EC2 Stack2
#MyEc2Stack(app,"MyOhioStack",env=env_oh)

#autoscalling stacks
#MyEc2AsgStack(app,"MyASGStack",env=env_US)


#secrets and ssm
MySecretStack(app,"SecreteStack")
#NewStack(app, "mydevstack1",env=env_US)

#NewStack(app,"myprodstack1",is_prod=True,env=env_US)

app.synth()
