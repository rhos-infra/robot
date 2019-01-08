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
                              --tests /home/opnfv/repos/odl_test/csit/suites/natapp/basic,/home/opnfv/repos/odl_test/csit/suites/openstack/connectivity/l2.robot
                      required: yes

            - title: Robot docker container name
              options:
                  container-image-name:
                      type: Value
                      help: |
                          Name of the container image to use to run Robot in.
                      default: opnfv/cperf:latest

            - title: ODL authentication
              options:
                  opendaylight-username:
                      type: Value
                      help: |
                          Username for ODL REST
                      default: odladmin
                  opendaylight-password:
                      type: Value
                      help: |
                          Password for ODL REST
                      default: redhat
                  karaf-prompt-login:
                      type: Value
                      help: |
                          Username/login that shows up when logged in to karaf
                          console.
                          NOTE: It may need to be overriden with 'karaf'
                          for certain versions, i.e.: OSP13 GA/odlparent 3.1.0.
                      default: 'opendaylight-user'
                  karaf-prompt-line:
                      type: Value
                      help: |
                          Prompt line of the karaf console.
                          NOTE: It may need to be overriden with 'karaf.*root.*'
                          for certain versions, i.e.: OSP13 GA/odlparent 3.1.0.
                      default: 'opendaylight-user.*root.*>'

            - title: ODL release
              options:
                  opendaylight_release:
                      type: Value
                      help: "Name of the OpenDaylight release, i.e.: fluorine."
                      NOTE: if value of this parameters is not specified then it defaults to one from vars.yml

            - title: Deployment environment
              options:
                  deployment-environment:
                      type: Value
                      help: |
                          Type of environment OpenDaylight was deployed in: baremetal, VM
                      default: VM
                      required: yes
                  osp-version:
                      type: Value
                      help: |
                          OSP version. Example: 14
                      required: yes

            - title: Cleanups
              options:
                  cleanup-before:
                      type: Bool
                      help: Whether to clean openstack resources (routers, security groups etc.) before running robot.
                      default: no