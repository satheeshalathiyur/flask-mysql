pipeline{
    agent any
    options{
                timestamps()
            }
    stages{
        stage("Build"){
            environment{
              aws_cred = credentials("awscredentials")
              secret = credentials("secret")
            }
            /*
            options{
                skipDefaultCheckout()
            }*/
            steps{
                 echo "hello build aws"
            }
            
        }
        
        
    }
}
