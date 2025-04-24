| 参数名称 | 参数类型 | 参数说明 | 是否必填 | 参数值约束 |
|---------|---------|---------|---------|------------|
| agentUser | object | 下单代理人信息 | 否 | - |
| └─ name | string | 下单人姓名 | 否 | - |
| └─ userId | string | 下单人ID | 否 | - |
| amount | object | 订单金额信息 | 否 | - |
| └─ baseCurrencyCode | string | 基准币种 | 否 | 例如：CNY |
| └─ currencyCode | string | 下单币种 | 否 | 例如：CNY |
| └─ exchangeRate | string | 支付币种和基础币种的汇率 | 否 | decimal格式 |
| businessStatus | integer | 订单业务状态 | 否 | - |
| businessTripType | string | 出行类型 | 否 | for_business/for_private |
| contactUser | object | 联系人信息 | 否 | - |
| └─ name | string | 联系人姓名 | 否 | - |
| └─ phone | string | 联系人手机号 | 否 | - |
| └─ email | string | 联系人邮箱 | 否 | - |
| └─ phoneAreaCode | string | 联系人手机号区号 | 否 | - |
| createTime | string | 创建时间 | 否 | YYYY-mm-dd HH:ii:ss |
| international | boolean | 是否国际 | 否 | true/false |
| items | array | 订单项信息 机票到票维度 | 否 | - |
| └─ [object] | object | 机票订单项 | 否 | - |
| │  └─ airportFeeOriginPrice | string | 机场建设费原价 | 否 | - |
| │  └─ airportFeePrice | string | 机场建设费 | 否 | - |
| │  └─ fuelFeeOriginPrice | string | 燃油费原价 | 否 | - |
| │  └─ fuelFeePrice | string | 燃油费 | 否 | - |
| │  └─ outFulfillmentOrderSn | string | 资源方履约单号 | 否 | - |
| │  └─ passenger | object | 乘客信息 | 否 | - |
| │     └─ EmployeeId | string | 出行人对应的员工id | 否 | - |
| │     └─ businessTripApplicationForm | object | 出差申请单信息 | 否 | - |
| │        └─ applicationNo | string | 出差申请单号 | 否 | - |
| │        └─ applier | string | 申请人 | 否 | - |
| │        └─ departmentId | string | 部门编号 | 否 | - |
| │        └─ employeeId | string | 员工编号 | 否 | - |
| │        └─ travelArrivalCity | string | 旅行到达城市 | 否 | - |
| │        └─ travelDepartureCity | string | 旅行出发城市 | 否 | - |
| │        └─ travelEndTime | string | 旅行结束时间 | 否 | - |
| │        └─ travelStartTime | string | 旅行开始时间 | 否 | - |
| │     └─ costCenterCode | string | 成本中心code | 否 | - |
| │     └─ costCenterName | string | 成本部门名称 | 否 | - |
| │     └─ departmentId | string | 员工所在部门ID | 否 | - |
| │     └─ departmentName | string | 员工所在部门名称 | 否 | - |
| │     └─ passenger | object | 乘客基本信息 | 否 | - |
| │        └─ birthday | string | 乘客生日 | 否 | YYYY-MM-DD |
| │        └─ cnFirstName | string | 中文名 | 否 | - |
| │        └─ cnLastName | string | 中文姓 | 否 | - |
| │        └─ country | string | 国家 | 否 | - |
| │        └─ countryCode | string | 国家码 | 否 | - |
| │        └─ customerEmployee | object | 客户员工信息 | 否 | - |
| │           └─ companyCode | string | 公司编码 | 否 | - |
| │           └─ companyName | string | 公司名称 | 否 | - |
| │           └─ departmentCode | string | 部门编码 | 否 | - |
| │           └─ departmentName | string | 部门名称 | 否 | - |
| │           └─ email | string | 邮箱 | 否 | - |
| │           └─ employeeId | string | 员工ID | 否 | - |
| │           └─ memberCode | string | 会员编码 | 否 | - |
| │           └─ organizationId | string | 组织ID | 否 | - |
| │           └─ phone | string | 手机号 | 否 | - |
| │           └─ phoneAreaCode | string | 手机区号 | 否 | - |
| │           └─ userId | string | 用户ID | 否 | - |
| │           └─ userLevel | string | 用户等级 | 否 | - |
| │           └─ username | string | 用户名 | 否 | - |
| │        └─ email | string | 乘客邮箱 | 否 | - |
| │        └─ enFirstName | string | 英文名 | 否 | - |
| │        └─ enLastName | string | 英文姓 | 否 | - |
| │        └─ gender | string | 乘客性别 | 否 | male/female |
| │        └─ idExpire | string | 证件有效期 | 否 | - |
| │        └─ idNo | string | 证件号码 | 否 | - |
| │        └─ idType | string | 证件类型 | 否 | idCard/passport |
| │        └─ passengerType | string | 乘客类型 | 否 | adult/child/baby/student/older |
| │        └─ phone | string | 乘客手机号 | 否 | - |
| │        └─ phoneAreaCode | string | 乘客手机区号 | 否 | - |
| │        └─ pyFirstName | string | 拼音名 | 否 | - |
| │        └─ pyLastName | string | 拼音姓 | 否 | - |
| │     └─ reimburseCenterCode | string | 报销部门code | 否 | - |
| │     └─ reimburseCenterName | string | 报销部门名称 | 否 | - |
| │  └─ payAmount | string | 实付金额 | 否 | - |
| │  └─ ticketNo | string | 机票号 | 否 | - |
| │  └─ ticketOriginSalePrice | string | 机票原价 | 否 | - |
| │  └─ ticketSalePrice | string | 机票售价 | 否 | - |
| │  └─ ticketStatus | string | 机票状态 | 否 | - |
| merchantId | string | 商户ID 用于区分不同的商户 店铺ID | 否 | - |
| note | object | 备注信息 | 否 | - |
| └─ customerFiles | array | 客人上传文件 | 否 | - |
| └─ customerNote | string | 客人备注 | 否 | - |
| └─ customerResources | array | 客人上传图片 | 否 | - |
| └─ customerServiceAgentFiles | array | 客服上传文件 | 否 | - |
| └─ customerServiceAgentNote | string | 客服备注 | 否 | - |
| └─ customerServiceAgentResources | array | 客服上传图片 | 否 | - |
| └─ orderReason | object | 下单原因/改签原因 | 否 | - |
| │  └─ desc | string | 原因描述 | 否 | - |
| │  └─ id | string | 原因ID | 否 | - |
| └─ specialService | array | 特殊服务 | 否 | - |
| │  └─ [object] | object | 特殊服务项 | 否 | - |
| │     └─ desc | string | 服务描述 | 否 | - |
| │     └─ id | string | 特殊服务ID | 否 | - |
| outOrderNo | string | 外部订单号 | 否 | - |
| paid | array | 支付信息 | 否 | - |
| └─ [object] | object | 支付项 | 否 | - |
| │  └─ orderSn | string | 订单号 | 否 | - |
| │  └─ payAmount | string | 支付金额 | 否 | decimal |
| │  └─ payCurrency | string | 支付币种 | 否 | 例如：CNY |
| │  └─ payMethodName | string | 支付方式名称 | 否 | - |
| │  └─ payMethodType | string | 支付方式类型 | 否 | credit：授信支付 |

| 参数名称 | 参数类型 | 参数说明 | 是否必填 | 参数值约束 |
|---------|---------|---------|---------|------------|
| │  └─ payNo | string | 支付号 | 否 | - |
| │  └─ paySerialNumber | string | 支付流水号 | 否 | - |
| │  └─ payTime | string | 支付时间 | 否 | YYYY-mm-dd HH:ii:ss |
| serviceProviderId | string | 服务商ID 经营主体ID | 否 | - |
| tenantId | string | 租户ID | 否 | - |
| terminal | object | 终端信息 | 否 | - |
| └─ orderSource | string | 下单来源 | 否 | platform/tmc |
| └─ terminalId | string | 终端ID | 否 | - |
| └─ terminalIp | string | 终端IP | 否 | - |
| └─ terminalType | string | 终端类型 | 否 | h5/ios/android/pc/wechat/alipay |
| user | object | 用户信息 | 否 | - |
| └─ customerEmployee | object | 客户员工信息 | 否 | - |
| │  └─ companyCode | string | 公司编码 | 否 | - |
| │  └─ companyName | string | 公司名称 | 否 | - |
| │  └─ departmentCode | string | 部门编码 | 否 | - |
| │  └─ departmentName | string | 部门名称 | 否 | - |
| │  └─ email | string | 邮箱 | 否 | - |
| │  └─ employeeId | string | 员工ID | 否 | - |
| │  └─ memberCode | string | 会员编码 | 否 | - |
| │  └─ organizationId | string | 组织ID | 否 | - |
| │  └─ phone | string | 手机号 | 否 | - |
| │  └─ phoneAreaCode | string | 手机区号 | 否 | - |
| │  └─ userId | string | 用户ID | 否 | - |
| │  └─ userLevel | string | 用户等级 | 否 | - |
| │  └─ username | string | 用户名 | 否 | - |
| └─ email | string | 用户邮箱 | 否 | - |
| └─ name | string | 用户姓名 | 否 | - |
| └─ phone | string | 用户手机号 | 否 | - |
| └─ phoneAreaCode | string | 用户手机区号 | 否 | - |
| └─ userId | string | 用户ID | 否 | - |
| voyage | object | 航程信息 | 否 | - |
| └─ ServiceProvideId | string | 经营主体id | 否 | - |
| └─ arriveAddress | object | 到达地 | 否 | - |
| │  └─ city | string | 城市 | 否 | - |
| │  └─ cityCode | string | 城市代码 | 否 | - |
| │  └─ country | string | 国家 | 否 | - |
| │  └─ countryCode | string | 国家代码 | 否 | - |
| │  └─ province | string | 省份 | 否 | - |
| │  └─ provinceCode | string | 省份代码 | 否 | - |
| └─ assetAccountId | string | 账号id | 否 | - |
| └─ departAddress | object | 出发地 | 否 | - |
| │  └─ city | string | 城市 | 否 | - |
| │  └─ cityCode | string | 城市代码 | 否 | - |
| │  └─ country | string | 国家 | 否 | - |
| │  └─ countryCode | string | 国家代码 | 否 | - |
| │  └─ province | string | 省份 | 否 | - |
| │  └─ provinceCode | string | 省份代码 | 否 | - |
| └─ direction | string | 行程方向 | 否 | depart/return |
| └─ externalVoyageId | string | 外部航程ID | 否 | - |
| └─ merchantId | string | 商户ID | 否 | - |
| └─ officeCode | string | 客户对应供应商的office号 | 否 | - |
| └─ officeName | string | office名称 | 否 | - |
| └─ priceInfoId | string | 价格信息ID | 否 | - |
| └─ promotionCode | string | 大客户编码 | 否 | - |
| └─ realRoundTrip | boolean | 是否真实往返 | 否 | true/false |
| └─ segment | array | 航段信息 | 否 | - |
| │  └─ [object] | object | 航段 | 否 | - |
| │     └─ additionalInfo | array | 附加信息 | 否 | - |
| │        └─ [object] | object | 信息项 | 否 | - |
| │           └─ desc | string | 描述 | 否 | - |
| │           └─ key | string | 键 | 否 | - |
| │     └─ airline | object | 航空公司 | 否 | - |
| │        └─ aircraftModel | string | 飞机型号 | 否 | - |
| │        └─ airline | string | 航空公司 | 否 | - |
| │        └─ airlineId | string | 航空公司ID | 否 | - |
| │     └─ airlineCode | string | 航空公司代码 | 否 | - |
| │     └─ arriveTerminal | object | 到达航站楼 | 否 | - |
| │        └─ arrivalDate | string | 到达日期 | 否 | - |
| │        └─ city | string | 城市 | 否 | - |
| │        └─ cityCode | string | 城市代码 | 否 | - |
| │        └─ country | string | 国家 | 否 | - |
| │        └─ countryCode | string | 国家代码 | 否 | - |
| │        └─ departureDate | string | 出发日期 | 否 | - |
| │        └─ province | string | 省份 | 否 | - |
| │        └─ provinceCode | string | 省份代码 | 否 | - |
| │        └─ terminal | string | 航站楼 | 否 | - |
| │        └─ terminalCode | string | 航站楼代码 | 否 | - |
| │        └─ time | string | 时间 | 否 | - |
| │        └─ trafficHub | string | 交通枢纽 | 否 | - |
| │        └─ trafficHubCode | string | 交通枢纽代码 | 否 | - |
| │     └─ cabin | object | 舱位 | 否 | - |
| │        └─ cabin | string | 舱位 | 否 | - |
| │        └─ cabinCode | string | 舱位代码 | 否 | - |
| │        └─ cabinType | string | 舱位类型 | 否 | super_economy/economy/business/first |
| │        └─ price | array | 价格 | 否 | - |
| │           └─ [object] | object | 价格项 | 否 | - |
| │              └─ airportFee | string | 机场费 | 否 | - |
| │              └─ oilFee | string | 燃油费 | 否 | - |
| │              └─ ticketPrice | string | 票价 | 否 | - |
| │              └─ type | string | 类型 | 否 | adult/child |
| │        └─ subCabin | string | 子舱位 | 否 | - |
| │     └─ carbonEmission | string | 碳排放 | 否 | - |
| │     └─ clearingBank | string | 清算银行 | 否 | - |
| │     └─ departTerminal | object | 出发航站楼 | 否 | 同arriveTerminal |
| │     └─ flight | object | 航班 | 否 | - |
| │        └─ flightId | string | 航班ID | 否 | - |
| │        └─ flightNo | string | 航班号 | 否 | - |
| │     └─ hasStopover | boolean | 是否有经停 | 否 | true/false |
| │     └─ sharedAirline | object | 共享航空公司 | 否 | 同airline |
| │     └─ sharedFlight | object | 共享航班 | 否 | 同flight |

| 参数名称 | 参数类型 | 参数说明 | 是否必填 | 参数值约束 |
|---------|---------|---------|---------|------------|
| │     └─ stopover | array | 经停信息 | 否 | - |
| │        └─ [object] | object | 经停点 | 否 | - |
| │           └─ arrivalTime | string | 到达时间 | 否 | - |
| │           └─ city | string | 城市 | 否 | - |
| │           └─ cityCode | string | 城市代码 | 否 | - |
| │           └─ country | string | 国家 | 否 | - |
| │           └─ countryCode | string | 国家代码 | 否 | - |
| │           └─ departureTime | string | 出发时间 | 否 | - |
| │           └─ province | string | 省份 | 否 | - |
| │           └─ provinceCode | string | 省份代码 | 否 | - |
| │           └─ trafficHub | string | 交通枢纽 | 否 | - |
| │           └─ trafficHubCode | string | 交通枢纽代码 | 否 | - |
| └─ supplierCode | string | 供应商代码 | 否 | - |
| └─ supplierName | string | 服务商名称 | 否 | - |
| └─ voyageType | string | 航程类型 | 否 | single/round |
