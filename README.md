#Auto-tests web UI in stack Behave + Cucumber + Allure + Python 3

##To start tests:
`$ cd proj root
`$ behave -f allure_behave.formatter:AllureFormatter -o my_report
`$ allure serve my_report
`$ behave --tags="@search_em" -f allure_behave.formatter:AllureFormatter -c -o my_report