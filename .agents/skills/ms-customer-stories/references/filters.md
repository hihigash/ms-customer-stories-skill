# Microsoft Customer Stories - Filter Reference

## API Endpoint

`POST https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch`

## Request Body Parameters

| Parameter | API Key | Filter Tag Format | Example |
|---|---|---|---|
| Products | `products` + `product` | `product:{category}` or `product:{category}/{sub}` | `product:azure/azure-openai` |
| Region | `region` | `region:{continent}/{country}` | `region:asia/japan` |
| Industries | `industries` | `industry:{value}` | `industry:healthcare` |
| Business Need | `businessneed` | `business-need:{value}` | `business-need:artificial-intelligence` |
| Org Size | `organizationSize` | `organization-size:{value}` | `organization-size:50-999-employees` |
| Services | `service` | `service:{value}` | `service:fasttrack` |
| Stories Include | `storiesThatInclude` | `stories-that-include:{value}` | `stories-that-include:videos` |
| Text Search | `query` | free text | `RAG` |
| Results per page | `top` | integer | `12` |
| Offset | `skip` | integer | `0` |
| Locale | `locale` | string | `en-ww` |

**Important:** Use `industries` (not `industry`) as the API key. Using `industry` returns unfiltered results.

**Multiple values:** Comma-separated: `"product:azure/azure-openai,product:azure/azure-ai-search"`

## Industries (16)

| Filter Tag | Label |
|---|---|
| `industry:automotive` | Automotive |
| `industry:defense` | Defense |
| `industry:education` | Education |
| `industry:energy-resources` | Energy & Resources |
| `industry:financial-services` | Financial Services |
| `industry:government` | Government |
| `industry:healthcare` | Healthcare |
| `industry:manufacturing` | Manufacturing |
| `industry:media` | Media |
| `industry:nonprofit` | Nonprofit |
| `industry:professional-services` | Professional Services |
| `industry:retail-consumer-goods` | Retail & Consumer Goods |
| `industry:technology` | Technology |
| `industry:telecommunications` | Telecommunications |
| `industry:travel-transportation` | Travel & Transportation |
| `industry:other` | Other |

## Business Need (18)

| Filter Tag | Label |
|---|---|
| `business-need:accessibility` | Accessibility |
| `business-need:agile-supply-chain` | Agile supply chain |
| `business-need:artificial-intelligence` | Artificial Intelligence |
| `business-need:automation` | Automation |
| `business-need:cloud-scale-analytics` | Cloud-scale analytics |
| `business-need:customer-experience` | Customer experience |
| `business-need:data-driven-decisions` | Data-driven decisions |
| `business-need:digital-service` | Digital service |
| `business-need:employee-experience` | Employee experience |
| `business-need:enterprise-support` | Enterprise support |
| `business-need:high-performance-computing` | High-performance computing |
| `business-need:hybrid-cloud` | Hybrid cloud |
| `business-need:low-code-development` | Low-code development |
| `business-need:modern-infrastructure` | Modern infrastructure |
| `business-need:powerful-business-apps` | Powerful business apps |
| `business-need:scaled-operations` | Scaled operations |
| `business-need:security-compliance` | Security & Compliance |
| `business-need:sustainability` | Sustainability |

## Products (96)

### AI & Microsoft Copilot
| Filter Tag | Label |
|---|---|
| `product:ai-microsoft-copilot` | AI & Microsoft Copilot (all) |
| `product:ai-microsoft-copilot/github-copilot` | GitHub Copilot |
| `product:ai-microsoft-copilot/microsoft-365-copilot` | Microsoft 365 Copilot |
| `product:ai-microsoft-copilot/microsoft-copilot-studio` | Microsoft Copilot Studio |
| `product:ai-microsoft-copilot/microsoft-foundry` | Microsoft Foundry |
| `product:ai-microsoft-copilot/microsoft-security-copilot` | Microsoft Security Copilot |
| `product:ai-microsoft-copilot/other` | Other |

### Azure
| Filter Tag | Label |
|---|---|
| `product:azure` | Azure (all) |
| `product:azure/analytics` | Analytics |
| `product:azure/azure-ai-search` | Azure AI Search |
| `product:azure/azure-machine-learning` | Azure Machine Learning |
| `product:azure/azure-openai` | Azure OpenAI |
| `product:azure/compute` | Compute |
| `product:azure/containers` | Containers |
| `product:azure/databases` | Databases |
| `product:azure/developer-tools` | Developer Tools |
| `product:azure/devops` | DevOps |
| `product:azure/hybrid-multicloud` | Hybrid & Multicloud |
| `product:azure/iaas` | IaaS |
| `product:azure/integration` | Integration |
| `product:azure/iot` | IoT |
| `product:azure/management-governance` | Management & Governance |
| `product:azure/microsoft-fabric` | Microsoft Fabric |
| `product:azure/microsoft-foundry` | Microsoft Foundry |
| `product:azure/migration` | Migration |
| `product:azure/modern-applications` | Modern Applications |
| `product:azure/networking` | Networking |
| `product:azure/optimization` | Optimization |
| `product:azure/security` | Security |
| `product:azure/storage` | Storage |
| `product:azure/vdi` | VDI |
| `product:azure/other` | Other |

### Dynamics 365
| Filter Tag | Label |
|---|---|
| `product:dynamics-365` | Dynamics 365 (all) |
| `product:dynamics-365/dynamics-365-business-central` | Dynamics 365 Business Central |
| `product:dynamics-365/dynamics-365-commerce` | Dynamics 365 Commerce |
| `product:dynamics-365/dynamics-365-customer-insights` | Dynamics 365 Customer Insights |
| `product:dynamics-365/dynamics-365-customer-service` | Dynamics 365 Customer Service |
| `product:dynamics-365/dynamics-365-field-service` | Dynamics 365 Field Service |
| `product:dynamics-365/dynamics-365-finance` | Dynamics 365 Finance |
| `product:dynamics-365/dynamics-365-human-resources` | Dynamics 365 Human Resources |
| `product:dynamics-365/dynamics-365-project-operations` | Dynamics 365 Project Operations |
| `product:dynamics-365/dynamics-365-remote-assist` | Dynamics 365 Remote Assist |
| `product:dynamics-365/dynamics-365-sales` | Dynamics 365 Sales |
| `product:dynamics-365/dynamics-365-supply-chain-management` | Dynamics 365 Supply Chain Management |
| `product:dynamics-365/other` | Other |

### Exchange
| Filter Tag | Label |
|---|---|
| `product:exchange` | Exchange |

### Microsoft 365
| Filter Tag | Label |
|---|---|
| `product:microsoft-365` | Microsoft 365 (all) |
| `product:microsoft-365/education` | Education |
| `product:microsoft-365/microsoft-365-for-business` | Microsoft 365 for Business |
| `product:microsoft-365/microsoft-365-for-education` | Microsoft 365 for Education |
| `product:microsoft-365/microsoft-365-for-enterprise` | Microsoft 365 for Enterprise |
| `product:microsoft-365/other` | Other |

### Microsoft Power Platform
| Filter Tag | Label |
|---|---|
| `product:microsoft-power-platform` | Microsoft Power Platform (all) |
| `product:microsoft-power-platform/dataverse` | Dataverse |
| `product:microsoft-power-platform/managed-environments` | Managed Environments |
| `product:microsoft-power-platform/power-apps` | Power Apps |
| `product:microsoft-power-platform/power-automate` | Power Automate |
| `product:microsoft-power-platform/power-bi` | Power BI |
| `product:microsoft-power-platform/power-pages` | Power Pages |
| `product:microsoft-power-platform/other` | Other |

### Microsoft Security
| Filter Tag | Label |
|---|---|
| `product:microsoft-security` | Microsoft Security (all) |
| `product:microsoft-security/azure-security` | Azure Security |
| `product:microsoft-security/microsoft-defender` | Microsoft Defender |
| `product:microsoft-security/microsoft-entra` | Microsoft Entra |
| `product:microsoft-security/microsoft-intune` | Microsoft Intune |
| `product:microsoft-security/microsoft-priva` | Microsoft Priva |
| `product:microsoft-security/microsoft-purview` | Microsoft Purview |
| `product:microsoft-security/microsoft-security-copilot` | Microsoft Security Copilot |
| `product:microsoft-security/microsoft-sentinel` | Microsoft Sentinel |
| `product:microsoft-security/other` | Other |

### Microsoft Teams
| Filter Tag | Label |
|---|---|
| `product:microsoft-teams` | Microsoft Teams (all) |
| `product:microsoft-teams/learning-accelerators` | Learning Accelerators |
| `product:microsoft-teams/teams-phone` | Teams Phone |
| `product:microsoft-teams/teams-rooms` | Teams Rooms |
| `product:microsoft-teams/other` | Other |

### Microsoft Viva
| Filter Tag | Label |
|---|---|
| `product:microsoft-viva` | Microsoft Viva (all) |
| `product:microsoft-viva/viva-engage` | Viva Engage |
| `product:microsoft-viva/viva-goals` | Viva Goals |
| `product:microsoft-viva/viva-insights` | Viva Insights |
| `product:microsoft-viva/viva-learning` | Viva Learning |
| `product:microsoft-viva/other` | Other |

### Surface
| Filter Tag | Label |
|---|---|
| `product:surface` | Surface |

### Windows
| Filter Tag | Label |
|---|---|
| `product:windows` | Windows (all) |
| `product:windows/windows-10` | Windows 10 |
| `product:windows/windows-11` | Windows 11 |
| `product:windows/windows-365` | Windows 365 |
| `product:windows/windows-autopilot` | Windows Autopilot |
| `product:windows/windows-server` | Windows Server |
| `product:windows/other` | Other |

### Other Products
| Filter Tag | Label |
|---|---|
| `product:other` | Other (all) |
| `product:other/hololens` | HoloLens |
| `product:other/marketplace` | Marketplace |
| `product:other/sharepoint` | SharePoint |
| `product:other/sql-server` | SQL Server |
| `product:other/visual-studio` | Visual Studio |
| `product:other/xbox` | Xbox |

## Services & Support (7)

| Filter Tag | Label |
|---|---|
| `service:fasttrack` | FastTrack |
| `service:industry-clouds` | Industry Clouds |
| `service:industry-solutions-delivery` | Industry Solutions Delivery |
| `service:microsoft-security-experts` | Microsoft Security Experts |
| `service:microsoft-unified` | Microsoft Unified |
| `service:other-services` | Other services |
| `service:other-support` | Other support |

## Organization Size (4)

| Filter Tag | Label |
|---|---|
| `organization-size:10000-employees` | 10,000+ employees |
| `organization-size:1000-9999-employees` | 1,000-9,999 employees |
| `organization-size:50-999-employees` | 50-999 employees |
| `organization-size:1-49-employees` | 1-49 employees |

## Region (245)

### Africa
`region:africa` (all Africa)

Countries: `region:africa/angola`, `region:africa/benin`, `region:africa/botswana`, `region:africa/burkina-faso`, `region:africa/burundi`, `region:africa/cabo-verde`, `region:africa/cameroon`, `region:africa/central-african-republic`, `region:africa/chad`, `region:africa/comoros`, `region:africa/congo`, `region:africa/congo-drc`, `region:africa/cote-d-ivoire`, `region:africa/djibouti`, `region:africa/equatorial-guinea`, `region:africa/eritrea`, `region:africa/eswatini`, `region:africa/ethiopia`, `region:africa/french-polynesia`, `region:africa/gabon`, `region:africa/gambia`, `region:africa/ghana`, `region:africa/guinea`, `region:africa/guinea-bissau`, `region:africa/kenya`, `region:africa/liberia`, `region:africa/libya`, `region:africa/madagascar`, `region:africa/malawi`, `region:africa/mali`, `region:africa/mauritania`, `region:africa/mauritius`, `region:africa/mayotte`, `region:africa/mozambique`, `region:africa/namibia`, `region:africa/new-caledonia`, `region:africa/niger`, `region:africa/nigeria`, `region:africa/runion`, `region:africa/rwanda`, `region:africa/sao-tome-prncipe`, `region:africa/senegal`, `region:africa/seychelles`, `region:africa/sierra-leone`, `region:africa/somalia`, `region:africa/south-africa`, `region:africa/south-sudan`, `region:africa/sudan`, `region:africa/tanzania`, `region:africa/togo`, `region:africa/tunisia`, `region:africa/uganda`, `region:africa/zambia`, `region:africa/zimbabwe`

### Asia
`region:asia` (all Asia)

Countries: `region:asia/bangladesh`, `region:asia/bhutan`, `region:asia/brunei`, `region:asia/china`, `region:asia/hong-kong-sar`, `region:asia/india`, `region:asia/indonesia`, `region:asia/japan`, `region:asia/korea`, `region:asia/laos`, `region:asia/macao-sar`, `region:asia/malaysia`, `region:asia/maldives`, `region:asia/myanmar`, `region:asia/nepal`, `region:asia/philippines`, `region:asia/singapore`, `region:asia/sri-lanka`, `region:asia/taiwan`, `region:asia/thailand`, `region:asia/vietnam`

### Australia and Pacific
`region:australia-and-pacific` (all)

Countries: `region:australia-and-pacific/australia`, `region:australia-and-pacific/new-zealand`, `region:australia-and-pacific/fiji`, `region:australia-and-pacific/papua-new-guinea`, and others

### Central America
`region:central-america` (all)

Countries: `region:central-america/puerto-rico`, `region:central-america/dominican-republic`, `region:central-america/jamaica`, `region:central-america/trinidad-tobago`, and others

### Europe
`region:europe` (all Europe)

Countries: `region:europe/united-kingdom`, `region:europe/france`, `region:europe/germany`, `region:europe/italy`, `region:europe/spain`, `region:europe/netherlands`, `region:europe/sweden`, `region:europe/switzerland`, `region:europe/norway`, `region:europe/denmark`, `region:europe/finland`, `region:europe/poland`, `region:europe/austria`, `region:europe/belgium`, `region:europe/czechia`, `region:europe/ireland`, `region:europe/portugal`, `region:europe/romania`, `region:europe/greece`, `region:europe/hungary`, and others

### Middle East
`region:middle-east` (all)

Countries: `region:middle-east/united-arab-emirates`, `region:middle-east/saudi-arabia`, `region:middle-east/israel`, `region:middle-east/turkiye`, `region:middle-east/qatar`, `region:middle-east/egypt`, `region:middle-east/kuwait`, `region:middle-east/bahrain`, `region:middle-east/jordan`, `region:middle-east/oman`, `region:middle-east/pakistan`, `region:middle-east/iraq`, `region:middle-east/morocco`, `region:middle-east/algeria`, `region:middle-east/lebanon`, and others

### North America
`region:north-america` (all)

Countries: `region:north-america/united-states`, `region:north-america/canada`, `region:north-america/mexico`, `region:north-america/guam`, `region:north-america/american-samoa`

### South America
`region:south-america` (all)

Countries: `region:south-america/brazil`, `region:south-america/argentina`, `region:south-america/colombia`, `region:south-america/chile`, `region:south-america/peru`, `region:south-america/venezuela`, `region:south-america/ecuador`, `region:south-america/bolivia`, `region:south-america/paraguay`, `region:south-america/uruguay`, `region:south-america/costa-rica`, `region:south-america/panama`, `region:south-america/guatemala`, `region:south-america/honduras`, `region:south-america/el-salvador`, `region:south-america/nicaragua`, and others

## Stories that Include (2)

| Filter Tag | Label |
|---|---|
| `stories-that-include:partners` | Partners |
| `stories-that-include:videos` | Videos |
