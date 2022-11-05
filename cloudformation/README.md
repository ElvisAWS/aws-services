
# Cloud formation plugin
    Indent one space
    VS Code Plugin for CloudFormation
    Create yaml file
    Type the word start to create a template
    Type the name of the resource and you will get a list of templates

# Cloud formation cli
    Available Commands
        activate-type
        batch-describe-type-configurations
        cancel-update-stack
        continue-update-rollback
        create-change-set
        create-stack ===> aws cloudformation create-stack --stack-name myteststack --template-body file://sampletemplate.json --parameters ParameterKey=KeyPairName,ParameterValue=TestKey ParameterKey=SubnetIDs,ParameterValue=SubnetID1\\,SubnetID2
        create-stack-instances
        create-stack-set
        deactivate-type
        delete-change-set
        delete-stack ===> aws cloudformation delete-stack --stack-name my-stack
        delete-stack-instances
        delete-stack-set
        deploy
        deregister-type
        describe-account-limits
        describe-change-set
        describe-change-set-hooks
        describe-publisher
        describe-stack-drift-detection-status
        describe-stack-events ===> aws cloudformation describe-stack-events --stack-name my-stack --max-items 4
        describe-stack-instance
        describe-stack-resource
        describe-stack-resource-drifts
        describe-stack-resources
        describe-stack-set
        describe-stack-set-operation
        describe-stacks ===> aws cloudformation describe-stacks --stack-name my-stack
        describe-type
        describe-type-registration
        detect-stack-drift
        detect-stack-resource-drift
        detect-stack-set-drift
        estimate-template-cost
        execute-change-set
        get-stack-policy
        get-template
        get-template-summary
        import-stacks-to-stack-set
        list-change-sets
        list-exports
        list-imports
        list-stack-instances
        list-stack-resources
        list-stack-set-operation-results
        list-stack-set-operations
        list-stack-sets
        list-stacks
        list-type-registrations
        list-type-versions
        list-types
        package
        publish-type
        record-handler-progress
        register-publisher
        register-type
        rollback-stack
        set-stack-policy
        set-type-configuration
        set-type-default-version
        signal-resource
        stop-stack-set-operation
        test-type
        update-stack
        update-stack-instances
        update-stack-set
        update-termination-protection
        validate-template ===> aws cloudformation validate-template --template-body file://sampletemplate.json
        wait

# CIDR Notation
    172.32.0.0/24
    10.0.0.0/24
    Network Portion - 24
    host Portion - 8  (24 - 32) 
        This is the last octet with zero
        2*8 = 256
    If Network is 25 we get 32 - 25 = 7 
# Subnets
    # https://www.davidc.net/sites/default/subnets/subnets.html
     Subnet 1 (128)
        172.32.0.0/25
        10.0.0.0/24
        Network Portion - 25
        host Portion - 7  (25 - 32) 2*7 = 128 but we shall get 0-127
     Subnet 2 (128)
        172.32.0.128/25
        10.0.0.0/24
        Network Portion - 25
        host Portion - 7  (25 - 32) 2*7 = 128 but we shall get 0-127
        
# https://www.youtube.com/watch?v=M5DOZZN1qmk&list=PLz8JBMMd7yjUukUG1M78ypP9GjWaP8rqf&index=1