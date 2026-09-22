SELECT c.login, COUNT(o."inDelivery")
FROM "Couriers" AS c
LEFT OUTER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;
