---
plugin_type: test
subparsers:
    robot:
        description: Run Robot based tests
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: Robot tests
              options:
                  tests:
                      type: Value
                      help: |
                        Comma,delimited list of robot files to execute.
                        Example:
                            /home/opnfv/repos/odl_test/csit/suites/natapp/basic,/home/opnfv/repos/odl_test/csit/suites/openstack/connectivity/l2.robot
                      required: yes
            - title: Robot docker containers
              options:
                  container-image-name:
                      type: Value
                      help: |
                          Name of the container image to use to run Robot in.
                      default: opnfv/cperf:latest
            - title: ODL authentication
              options:
                  odl-username:
                      type: Value
                      help: |
                          Username for ODL REST
                      default: odladmin
                   odl-password:
                      type: Value
                      help: |
                          Password for ODL REST
                      default: redhat
