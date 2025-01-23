Feature: Loading Data in Amazon RDS

  Scenario: The client call the route /jobs with a jobs id and a url
    Given A job_id "123"
    And A dataSource "http://fake.url/data.json"
    When The client call the route with the job_id and the dataSource
    Then The service return a HTTP code 200 and a success message
