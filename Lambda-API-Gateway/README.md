# aws-sam
# Pre-requirements
    # (1) Install AWS CLi
    # (2) Configure AWS CLI
    # (3) Install SAM
    # (4) Install Docker (to run sam locally)
# How to Create a Project
    # sam init
Commands you can use next
    =========================
    [*] Create pipeline: cd sam-app && sam pipeline init --bootstrap
    [*] Validate SAM template: cd sam-app && sam validate
    [*] Test Function in the Cloud: cd sam-app && sam sync --stack-name {stack-name} --watch
# Logs
    # sam logs
# Package
    # sam package
# Build application
    # sam build
Commands you can use next
=========================
    [*] Validate SAM template: sam validate
    [*] Invoke Function: sam local invoke
    [*] Test Function in the Cloud: sam sync --stack-name {stack-name} --watch
    [*] Deploy: sam deploy --guided
# Deploy application
    # sam deploy --guided   # Use the guided flag for the first time you run sam deploy

# Build a docker container
    # sam build
    # sam local start-api




# Sam Commands
sam build
sam delete
sam deploy
sam init
sam local generate-event
sam local invoke
sam local start-api
sam local start-lambda
sam logs
sam package
sam pipeline bootstrap
sam pipeline init
sam publish
sam sync
sam traces
sam validate