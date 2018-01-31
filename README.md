## Robot

Allows to run robot-based test suites

### How to use this project as an ansible playbook

Create virtual environment:

    virtualenv venv
    source venv/bin/activate
    pip install ansible

Run:
    ansible-playbook -i hosts main.yml --extra-vars @params.yml -vvvv

### How to use this as an InfraRed plugin

    git clone https://github.com/redhat-openstack/infrared.git
    cd infrared
    virtualenv venv
    source venv/bin/activate
    pip install -e .
    
create a 'hosts' file, with content i.e.:

     tester ansible_connection=local ansible_python_interpreter=python

Add this 'robot' plugin to Infrared:

    infrared plugin add https://github.com/rhos-infra/robot.git

Run:
    infrared robot --tests <test_suite>
    
    example:
    
        infrared robot --tests /home/opnfv/repos/odl_test/csit/suites/natapp/basic,
        /home/opnfv/repos/odl_test/csit/suites/openstack/connectivity/l2.robot
