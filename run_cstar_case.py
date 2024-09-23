import cstar
cstar_test_case = cstar.Case.from_blueprint(
    blueprint="cstar_blueprint_test_case",
    caseroot="cstar_test_case/",
    start_date="20120101 12:00:00",
    end_date="20120101 12:10:00",
)

## Set up and run C-Star case locally:
cstar_test_case.setup()
cstar_test_case.build()
cstar_test_case.pre_run()
cstar_test_case.run(account_key=None) #substituting your account key on any HPC system
cstar_test_case.post_run()
