| 参数名称 | 参数类型 | 参数说明 | 是否必填 | 参数值约束 |
|---------|---------|---------|---------|------------|
| agentUser | object | - |  | - |
| └─ name | string | - |  | string |
| └─ userId | string | - |  | string |
| amount | object | - |  | - |
| └─ baseCurrencyCode | string | - |  | CNY |
| └─ currencyCode | string | - |  | CNY |
| └─ exchangeRate | string | - |  | string |
| businessStatus | number | - |  | 0 |
| businessTripType | string | - |  | for_private |
| contactUser | object | - |  | - |
| └─ email | string | - |  | string |
| └─ name | string | - |  | string |
| └─ phone | string | - |  | string |
| └─ phoneAreaCode | string | - |  | string |
| createTime | string | - |  | string |
| international | boolean | - |  | true/false |
| items | array | - |  | - |
| └─ airportFeeOriginPrice | string | - |  | string |
| └─ airportFeePrice | string | - |  | string |
| └─ fuelFeeOriginPrice | string | - |  | string |
| └─ fuelFeePrice | string | - |  | string |
| └─ outFulfillmentOrderSn | string | - |  | string |
| └─ passenger | object | - |  | - |
| │  └─ EmployeeId | string | - |  | string |
| │  └─ businessTripApplicationForm | object | - |  | - |
| │  │  └─ applicationNo | string | - |  | string |
| │  │  └─ applier | string | - |  | string |
| │  │  └─ departmentId | string | - |  | string |
| │  │  └─ employeeId | string | - |  | string |
| │  │  └─ travelArrivalCity | string | - |  | string |
| │  │  └─ travelDepartureCity | string | - |  | string |
| │  │  └─ travelEndTime | string | - |  | string |
| │  │  └─ travelStartTime | string | - |  | string |
| │  └─ costCenterCode | string | - |  | string |
| │  └─ costCenterName | string | - |  | string |
| │  └─ departmentId | string | - |  | string |
| │  └─ departmentName | string | - |  | string |
| │  └─ passenger | object | - |  | - |
| │  │  └─ birthday | string | - |  | string |
| │  │  └─ cnFirstName | string | - |  | string |
| │  │  └─ cnLastName | string | - |  | string |
| │  │  └─ country | string | - |  | string |
| │  │  └─ countryCode | string | - |  | string |
| │  │  └─ customerEmployee | object | - |  | - |
| │  │  │  └─ companyCode | string | - |  | string |
| │  │  │  └─ companyName | string | - |  | string |
| │  │  │  └─ departmentCode | string | - |  | string |
| │  │  │  └─ departmentName | string | - |  | string |
| │  │  │  └─ email | string | - |  | string |
| │  │  │  └─ employeeId | string | - |  | string |
| │  │  │  └─ memberCode | string | - |  | string |
| │  │  │  └─ organizationId | string | - |  | string |
| │  │  │  └─ phone | string | - |  | string |
| │  │  │  └─ phoneAreaCode | string | - |  | string |
| │  │  │  └─ userId | string | - |  | string |
| │  │  │  └─ userLevel | string | - |  | string |
| │  │  │  └─ username | string | - |  | string |
| │  │  └─ email | string | - |  | string |
| │  │  └─ enFirstName | string | - |  | string |
| │  │  └─ enLastName | string | - |  | string |
| │  │  └─ gender | string | - |  | male |
| │  │  └─ idExpire | string | - |  | string |
| │  │  └─ idNo | string | - |  | string |
| │  │  └─ idType | string | - |  | idCard |
| │  │  └─ passengerType | string | - |  | adult |
| │  │  └─ phone | string | - |  | string |
| │  │  └─ phoneAreaCode | string | - |  | string |
| │  │  └─ pyFirstName | string | - |  | string |
| │  │  └─ pyLastName | string | - |  | string |
| │  └─ reimburseCenterCode | string | - |  | string |
| │  └─ reimburseCenterName | string | - |  | string |
| └─ payAmount | string | - |  | string |
| └─ ticketNo | string | - |  | string |
| └─ ticketOriginSalePrice | string | - |  | string |
| └─ ticketSalePrice | string | - |  | string |
| └─ ticketStatus | string | - |  | - |
| merchantId | string | - |  | string |
| note | object | - |  | - |
| └─ customerFiles | array | - |  | - |
| └─ └─ [string] | string | - |  | string |
| └─ customerNote | string | - |  | string |
| └─ customerResources | array | - |  | - |
| └─ └─ [string] | string | - |  | string |
| └─ customerServiceAgentFiles | array | - |  | - |
| └─ └─ [string] | string | - |  | string |
| └─ customerServiceAgentNote | string | - |  | string |
| └─ customerServiceAgentResources | array | - |  | - |
| └─ └─ [string] | string | - |  | string |
| └─ orderReason | object | - |  | - |
| │  └─ desc | string | - |  | string |
| │  └─ id | string | - |  | string |
| └─ specialService | array | - |  | - |
| │  └─ desc | string | - |  | string |
| │  └─ id | string | - |  | string |
| outOrderNo | string | - |  | string |
| paid | array | - |  | - |
| └─ orderSn | string | - |  | string |
| └─ payAmount | string | - |  | string |
| └─ payCurrency | string | - |  | CNY |
| └─ payMethodName | string | - |  | string |

| 参数名称 | 参数类型 | 参数说明 | 是否必填 | 参数值约束 |
|---------|---------|---------|---------|------------|
| └─ payMethodType | string | - |  | credit |
| └─ payNo | string | - |  | string |
| └─ paySerialNumber | string | - |  | string |
| └─ payTime | string | - |  | string |
| serviceProviderId | string | - |  | string |
| tenantId | string | - |  | string |
| terminal | object | - |  | - |
| └─ orderSource | string | - |  | string |
| └─ terminalId | string | - |  | string |
| └─ terminalIp | string | - |  | string |
| └─ terminalType | string | - |  | h5 |
| user | object | - |  | - |
| └─ customerEmployee | object | - |  | - |
| │  └─ companyCode | string | - |  | string |
| │  └─ companyName | string | - |  | string |
| │  └─ departmentCode | string | - |  | string |
| │  └─ departmentName | string | - |  | string |
| │  └─ email | string | - |  | string |
| │  └─ employeeId | string | - |  | string |
| │  └─ memberCode | string | - |  | string |
| │  └─ organizationId | string | - |  | string |
| │  └─ phone | string | - |  | string |
| │  └─ phoneAreaCode | string | - |  | string |
| │  └─ userId | string | - |  | string |
| │  └─ userLevel | string | - |  | string |
| │  └─ username | string | - |  | string |
| └─ email | string | - |  | string |
| └─ name | string | - |  | string |
| └─ phone | string | - |  | string |
| └─ phoneAreaCode | string | - |  | string |
| └─ userId | string | - |  | string |
| voyage | object | - |  | - |
| └─ ServiceProvideId | string | - |  | string |
| └─ arriveAddress | object | - |  | - |
| │  └─ city | string | - |  | string |
| │  └─ cityCode | string | - |  | string |
| │  └─ country | string | - |  | string |
| │  └─ countryCode | string | - |  | string |
| │  └─ province | string | - |  | string |
| │  └─ provinceCode | string | - |  | string |
| └─ assetAccountId | string | - |  | string |
| └─ departAddress | object | - |  | - |
| │  └─ city | string | - |  | string |
| │  └─ cityCode | string | - |  | string |
| │  └─ country | string | - |  | string |
| │  └─ countryCode | string | - |  | string |
| │  └─ province | string | - |  | string |
| │  └─ provinceCode | string | - |  | string |
| └─ direction | string | - |  | depart |
| └─ externalVoyageId | string | - |  | string |
| └─ merchantId | string | - |  | string |
| └─ officeCode | string | - |  | string |
| └─ officeName | string | - |  | string |
| └─ priceInfoId | string | - |  | string |
| └─ promotionCode | string | - |  | string |
| └─ realRoundTrip | boolean | - |  | true/false |
| └─ segment | array | - |  | - |
| │  └─ additionalInfo | array | - |  | - |
| │  │  └─ desc | string | - |  | string |
| │  │  └─ key | string | - |  | string |
| │  └─ airline | object | - |  | - |
| │  │  └─ aircraftModel | string | - |  | string |
| │  │  └─ airline | string | - |  | string |
| │  │  └─ airlineId | string | - |  | string |
| │  └─ airlineCode | string | - |  | string |
| │  └─ arriveTerminal | object | - |  | - |
| │  │  └─ arrivalDate | string | - |  | string |
| │  │  └─ city | string | - |  | string |
| │  │  └─ cityCode | string | - |  | string |
| │  │  └─ country | string | - |  | string |
| │  │  └─ countryCode | string | - |  | string |
| │  │  └─ departureDate | string | - |  | string |
| │  │  └─ province | string | - |  | string |
| │  │  └─ provinceCode | string | - |  | string |
| │  │  └─ terminal | string | - |  | string |
| │  │  └─ terminalCode | string | - |  | string |
| │  │  └─ time | string | - |  | string |
| │  │  └─ trafficHub | string | - |  | string |
| │  │  └─ trafficHubCode | string | - |  | string |
| │  └─ cabin | object | - |  | - |
| │  │  └─ cabin | string | - |  | string |
| │  │  └─ cabinCode | string | - |  | string |
| │  │  └─ cabinType | string | - |  | super_economy |
| │  │  └─ price | array | - |  | - |
| │  │  │  └─ airportFee | string | - |  | string |
| │  │  │  └─ oilFee | string | - |  | string |
| │  │  │  └─ ticketPrice | string | - |  | string |
| │  │  │  └─ type | string | - |  | adult |
| │  │  └─ subCabin | string | - |  | string |
| │  └─ carbonEmission | string | - |  | string |
| │  └─ clearingBank | string | - |  | string |
| │  └─ departTerminal | object | - |  | - |
| │  │  └─ arrivalDate | string | - |  | string |
| │  │  └─ city | string | - |  | string |
| │  │  └─ cityCode | string | - |  | string |
| │  │  └─ country | string | - |  | string |
| │  │  └─ countryCode | string | - |  | string |
| │  │  └─ departureDate | string | - |  | string |
| │  │  └─ province | string | - |  | string |
| │  │  └─ provinceCode | string | - |  | string |

| 参数名称 | 参数类型 | 参数说明 | 是否必填 | 参数值约束 |
|---------|---------|---------|---------|------------|
| │  │  └─ terminal | string | - |  | string |
| │  │  └─ terminalCode | string | - |  | string |
| │  │  └─ time | string | - |  | string |
| │  │  └─ trafficHub | string | - |  | string |
| │  │  └─ trafficHubCode | string | - |  | string |
| │  └─ flight | object | - |  | - |
| │  │  └─ flightId | string | - |  | string |
| │  │  └─ flightNo | string | - |  | string |
| │  └─ hasStopover | boolean | - |  | true/false |
| │  └─ sharedAirline | object | - |  | - |
| │  │  └─ aircraftModel | string | - |  | string |
| │  │  └─ airline | string | - |  | string |
| │  │  └─ airlineId | string | - |  | string |
| │  └─ sharedFlight | object | - |  | - |
| │  │  └─ flightId | string | - |  | string |
| │  │  └─ flightNo | string | - |  | string |
| │  └─ stopover | array | - |  | - |
| │  │  └─ arrivalTime | string | - |  | string |
| │  │  └─ city | string | - |  | string |
| │  │  └─ cityCode | string | - |  | string |
| │  │  └─ country | string | - |  | string |
| │  │  └─ countryCode | string | - |  | string |
| │  │  └─ departureTime | string | - |  | string |
| │  │  └─ province | string | - |  | string |
| │  │  └─ provinceCode | string | - |  | string |
| │  │  └─ trafficHub | string | - |  | string |
| │  │  └─ trafficHubCode | string | - |  | string |
| └─ supplierCode | string | - |  | string |
| └─ supplierName | string | - |  | string |
| └─ voyageType | string | - |  | single |