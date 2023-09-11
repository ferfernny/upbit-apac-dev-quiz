SELECT
    MIP.member_uuid,
    D.currency,
    D.amount,
    MIP.first_name,
    MIP.last_name,
    MIP.birthday,
    MIP.gender,
    MIP.nationality,
    MIP.country_of_birth,
    MIP.country_location
FROM
    deposits D
JOIN
    memberinfopersonal MIP ON D.account_id = MIP.personal_info_id
WHERE
    D.currency = 'THB'
    AND D.amount >= 5000000
ORDER BY
    D.amount DESC;
