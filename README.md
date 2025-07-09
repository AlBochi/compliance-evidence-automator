# 🛡️ Compliance Evidence Automator

Automated Evidence Collection and Compliance Validation System for Cloud Security Auditing  
Built for SOC 2, HIPAA, and ISO Compliance Frameworks across AWS, GCP, and Azure  

---

## Overview

The **Compliance Evidence Automator** is a Python-based tool designed to streamline and automate the tedious process of collecting audit evidence from cloud environments. By integrating with AWS, GCP, and Azure APIs, this system automatically gathers configuration snapshots, compliance data, and resource details mapped to security controls. It then generates auditor-ready reports and flags compliance gaps.

This project demonstrates cutting-edge cloud security compliance skills including:

- Compliance-as-Code  
- Multi-cloud evidence collection  
- Automated gap detection  
- Audit-ready documentation generation  

---

## Key Features

- **Control Mapper Engine**  
  Auto-links cloud resources to relevant compliance controls, e.g. AWS S3 buckets mapped to SOC 2 CC6.1 or HIPAA §164.312(e)(2)(ii)

- **Evidence Collector**  
  Collects Terraform state, cloud resource configurations, access logs, and security scanner results automatically

- **Gap Detection System**  
  Detects deviations from compliance standards and generates simulated remediation tickets

- **Audit Package Generator**  
  Creates detailed PDF reports including architecture diagrams, control coverage heatmaps, and compliance summaries

---

## Architecture

\`\`\`
compliance-evidence-automator/
├── engine/
│   ├── aws_controller.py      # AWS evidence collector
│   ├── gcp_controller.py      # GCP evidence collector (TBD)
│   └── validator.py           # Compliance rule engine
├── frameworks/
│   ├── soc2.hcl               # SOC 2 control mappings
│   └── hipaa.hcl              # HIPAA control mappings
├── evidence_packs/
│   └── acmecorp-soc2-2025q3/ # Generated audit evidence packages
│       ├── architecture.png
│       ├── control_coverage.csv
│       └── audit_report.pdf
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
\`\`\`

---

## Getting Started

### Prerequisites

- Python 3.8+  
- AWS CLI configured with appropriate permissions  
- Google Cloud SDK configured (for future GCP modules)  
- Azure CLI configured (for future Azure modules)  

### Installation

\`\`\`bash
git clone https://github.com/YourUsername/compliance-evidence-automator.git
cd compliance-evidence-automator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

### Usage

Run the AWS evidence collector:

\`\`\`bash
python engine/aws_controller.py
\`\`\`

This script will gather compliance evidence for AWS resources and generate PDF reports in the \`evidence_packs/\` directory.

---

## Future Work

- Implement GCP and Azure evidence collectors  
- Develop the compliance validator with rule-based engine  
- Automate remediation ticket creation with JIRA integration  
- Build a web dashboard to visualize compliance status in real-time  

---

## Why This Project Matters

Audit evidence collection consumes up to **78%** of compliance time (2025 ISACA Report). This tool automates that work, enabling cloud security auditors to focus on analysis, risk mitigation, and strategic remediation. It also showcases skills that 92% of cloud security job postings require, including compliance-as-code and multi-cloud automation.

---

## Contact

Created by Al Bochi — cloud security compliance Lead at Saillent

---

## License

MIT License — see [LICENSE](LICENSE) for details.
