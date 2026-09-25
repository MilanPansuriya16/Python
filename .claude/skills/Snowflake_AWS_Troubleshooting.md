---
name: Snowflake_AWS_Troubleshooting
description: Troubleshooting guide for Snowflake S3 Storage Integration with AWS IAM roles
trigger: Use when troubleshooting Snowflake external stages, S3 integration, or sts:AssumeRole errors
---

# Snowflake AWS S3 Storage Integration Troubleshooting Guide

## Overview
This skill documents comprehensive troubleshooting steps for setting up and debugging Snowflake external stages with AWS S3 using IAM role-based authentication.

## Common Error
```
Error assuming AWS_ROLE: User: arn:aws:iam::<account>:user/<user> is not authorized 
to perform: sts:AssumeRole on resource: arn:aws:iam::<account>:role/<role>
```

---

## Setup Components

### 1. Snowflake Storage Integration
```sql
CREATE OR REPLACE STORAGE INTEGRATION <integration_name>
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = 'S3' 
    ENABLED = TRUE
    STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::<account-id>:role/<role-name>'
    STORAGE_ALLOWED_LOCATIONS = ('s3://<bucket-name>/')
    COMMENT = 'Integration with AWS';

-- Get Snowflake-generated values
DESC INTEGRATION <integration_name>;
```

**Critical values from DESC INTEGRATION:**
- `STORAGE_AWS_IAM_USER_ARN` - Snowflake's IAM user in their AWS account
- `STORAGE_AWS_EXTERNAL_ID` - Unique identifier for security
- `STORAGE_AWS_ROLE_ARN` - Your AWS IAM role

### 2. AWS IAM Role Trust Policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "<STORAGE_AWS_IAM_USER_ARN from Snowflake>"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "<STORAGE_AWS_EXTERNAL_ID from Snowflake>"
                }
            }
        }
    ]
}
```

### 3. AWS IAM Role Permissions Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:ListBucket",
        "s3:GetBucketLocation"
      ],
      "Resource": [
        "arn:aws:s3:::<bucket-name>",
        "arn:aws:s3:::<bucket-name>/*"
      ]
    }
  ]
}
```

### 4. Snowflake External Stage
```sql
CREATE OR REPLACE STAGE <stage_name>
    URL = 's3://<bucket-name>/'
    STORAGE_INTEGRATION = <integration_name>
    FILE_FORMAT = <file_format_name>;

-- Grant permissions
GRANT USAGE ON INTEGRATION <integration_name> TO ROLE ACCOUNTADMIN;
GRANT USAGE ON STAGE <stage_name> TO ROLE ACCOUNTADMIN;

-- Test
LIST @<stage_name>;
```

---

## Systematic Troubleshooting Steps

### Step 1: Verify S3 Bucket Access
Test if the bucket is accessible at all:

**In AWS CloudShell:**
```bash
aws s3 ls s3://<bucket-name>/
```

**In Snowflake (using direct credentials - temporary test):**
```sql
CREATE OR REPLACE STAGE TEST_STAGE_DIRECT
    URL = 's3://<bucket-name>/'
    CREDENTIALS = (
        AWS_KEY_ID = '<access-key>'
        AWS_SECRET_KEY = '<secret-key>'
    )
    FILE_FORMAT = <file_format>;

LIST @TEST_STAGE_DIRECT;
```

✅ **If this works:** S3 bucket, network, and permissions are fine. Issue is with role assumption.  
❌ **If this fails:** S3 bucket access or network issue.

### Step 2: Verify Storage Integration Configuration
```sql
DESC INTEGRATION <integration_name>;
SHOW INTEGRATIONS;
```

Check:
- ✅ `ENABLED` = true
- ✅ `STORAGE_AWS_ROLE_ARN` matches your AWS IAM role exactly
- ✅ `STORAGE_ALLOWED_LOCATIONS` has trailing slash: `s3://bucket/`
- ✅ Note the `STORAGE_AWS_IAM_USER_ARN` and `STORAGE_AWS_EXTERNAL_ID`

### Step 3: Verify AWS IAM Role Trust Policy
In **AWS Console → IAM → Roles → [role-name] → Trust relationships**

Verify:
- ✅ `Principal.AWS` matches `STORAGE_AWS_IAM_USER_ARN` from Snowflake exactly
- ✅ `sts:ExternalId` matches `STORAGE_AWS_EXTERNAL_ID` from Snowflake exactly
- ✅ No typos or hidden characters
- ✅ Version is `2012-10-17`

**Test without Condition (temporary):**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<snowflake-account>:user/<user>"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

If this works, the External ID has a typo or hidden character.

### Step 4: Verify AWS IAM Role Permissions
In **AWS Console → IAM → Roles → [role-name] → Permissions**

Check:
- ✅ S3 permissions policy is attached
- ✅ Policy includes both bucket and bucket/* resources
- ✅ Actions include: `s3:GetObject`, `s3:ListBucket`, `s3:GetBucketLocation`
- ✅ No permission boundaries restricting access

### Step 5: Check for AWS Organization SCPs
If your AWS account is part of an AWS Organization:
- **AWS Console → AWS Organizations → Policies**
- Check for Service Control Policies (SCPs) that might block `sts:AssumeRole`

### Step 6: Wait for IAM Propagation
IAM changes can take 1-2 minutes to propagate. After making changes:
1. Wait 2 full minutes
2. Try listing again: `LIST @<stage_name>;`

### Step 7: Refresh Storage Integration
```sql
-- Toggle integration to force refresh
ALTER STORAGE INTEGRATION <integration_name> SET ENABLED = FALSE;
ALTER STORAGE INTEGRATION <integration_name> SET ENABLED = TRUE;

-- Wait 10 seconds
LIST @<stage_name>;
```

### Step 8: Recreate with Fresh Values
Sometimes cached configurations cause issues:

```sql
-- Drop and recreate
DROP STAGE IF EXISTS <stage_name>;
DROP STORAGE INTEGRATION IF EXISTS <integration_name>;

-- Recreate with NEW name
CREATE STORAGE INTEGRATION <integration_name>_v2
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = 'S3' 
    ENABLED = TRUE
    STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::<account>:role/<new-role-name>'
    STORAGE_ALLOWED_LOCATIONS = ('s3://<bucket>/')
    COMMENT = 'Fresh integration';

DESC INTEGRATION <integration_name>_v2;
```

Update AWS trust policy with the NEW `STORAGE_AWS_IAM_USER_ARN` and `STORAGE_AWS_EXTERNAL_ID`.

---

## ⚠️ CRITICAL: Opt-In AWS Regions Issue

### The Problem
**If your Snowflake account is in a newer AWS opt-in region** (e.g., ap-southeast-7 Thailand, ap-south-2 Hyderabad, etc.), the AWS STS endpoint for that region may be **inactive by default**.

**Symptoms:**
- ✅ Trust policy is correct
- ✅ Permissions are correct
- ✅ Direct credentials work
- ❌ Role assumption fails with sts:AssumeRole error
- ❌ Recreating integration doesn't help
- ❌ Removing External ID condition doesn't help

### The Root Cause
Newer AWS regions are **opt-in** and disabled by default in AWS accounts. When disabled:
- The regional STS endpoint is inactive
- Snowflake routes AssumeRole through the regional STS endpoint
- Inactive endpoint = failed role assumption

### The Solution

#### Step 1: Enable the AWS Region
**Option A: AWS Console**
1. AWS Console → Top-right account menu → **Account**
2. Left sidebar → **AWS Regions**
3. Find your Snowflake's region (e.g., "Asia Pacific (Thailand) ap-southeast-7")
4. Click **Enable**
5. Confirm

**Option B: AWS CLI**
```bash
aws account enable-region --region-name ap-southeast-7
```

#### Step 2: Activate STS Endpoint
1. AWS Console → **IAM** → **Account settings**
2. Scroll to **Security Token Service (STS)** section
3. Under **Endpoints**, find your region
4. Change from **Inactive** to **Active**
5. Click **Save changes**

#### Step 3: Wait and Test
1. Wait 5-15 minutes for activation
2. Test in Snowflake:
```sql
LIST @<stage_name>;
```

### Affected AWS Regions (Opt-In)
- ap-southeast-7 (Thailand - Bangkok)
- ap-south-2 (India - Hyderabad)
- ap-southeast-4 (Australia - Melbourne)
- ca-west-1 (Canada - Calgary)
- eu-south-2 (Spain - Madrid)
- eu-central-2 (Switzerland - Zurich)
- il-central-1 (Israel - Tel Aviv)
- me-central-1 (UAE - Abu Dhabi)

**Check your Snowflake region:**
```sql
SELECT CURRENT_REGION();
```

---

## Common Syntax Errors

### ❌ Wrong: Missing SET keyword
```sql
ALTER STORAGE INTEGRATION AWS_S3_INTEGRATION
    STORAGE_AWS_ROLE_ARN = '...'
```

### ✅ Correct: Include SET
```sql
ALTER STORAGE INTEGRATION AWS_S3_INTEGRATION SET
    STORAGE_AWS_ROLE_ARN = '...'
```

### ❌ Wrong: Invalid Version
```json
{
  "Version": "2025-10-10",
  ...
}
```

### ✅ Correct: Use 2012-10-17
```json
{
  "Version": "2012-10-17",
  ...
}
```

### ❌ Wrong: Missing trailing slash
```sql
STORAGE_ALLOWED_LOCATIONS = ('s3://bucket')
```

### ✅ Correct: Include trailing slash
```sql
STORAGE_ALLOWED_LOCATIONS = ('s3://bucket/')
```

---

## Alternative: Direct IAM User Credentials

If role-based access is not working and you need to proceed:

### Setup
1. Create dedicated IAM user: `snowflake-production-user`
2. Attach S3 access policy (read-only or specific bucket)
3. Generate access keys
4. Create stage with credentials

### Implementation
```sql
CREATE OR REPLACE STAGE PROD_S3_STAGE
    URL = 's3://<bucket-name>/'
    CREDENTIALS = (
        AWS_KEY_ID = '<access-key-id>'
        AWS_SECRET_KEY = '<secret-access-key>'
    )
    FILE_FORMAT = <file_format_name>;
```

### Security Best Practices
- ✅ Use dedicated IAM user (not personal account)
- ✅ Restrict permissions to specific bucket only
- ✅ Rotate credentials every 90 days
- ✅ Enable CloudTrail for audit logging
- ✅ Use least-privilege permissions

### When to Use
- Role assumption persistently fails after all troubleshooting
- Need immediate access while resolving role issues
- Legacy systems or compatibility requirements
- Testing/development environments

---

## Quick Reference Commands

### Snowflake
```sql
-- Create file format
CREATE OR REPLACE FILE FORMAT CSV_FORMAT
    TYPE = CSV
    SKIP_HEADER = 1
    FIELD_DELIMITER = ','
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    NULL_IF = ('NULL', 'null', '');

-- List files in stage
LIST @<stage_name>;

-- Query files directly
SELECT $1, $2, $3 
FROM @<stage_name>
(FILE_FORMAT => 'CSV_FORMAT') 
LIMIT 10;

-- Load data into table
COPY INTO <table_name>
FROM @<stage_name>
FILE_FORMAT = CSV_FORMAT
ON_ERROR = 'CONTINUE';

-- Check integration details
DESC INTEGRATION <integration_name>;
SHOW INTEGRATIONS;

-- Check stage details
DESC STAGE <stage_name>;
SHOW STAGES;
```

### AWS CLI
```bash
# List S3 bucket
aws s3 ls s3://<bucket>/

# Check caller identity
aws sts get-caller-identity

# Enable region
aws account enable-region --region-name <region>

# Test role assumption (will fail but shows detailed error)
aws sts assume-role \
  --role-arn arn:aws:iam::<account>:role/<role> \
  --role-session-name test \
  --external-id "<external-id>"
```

---

## Diagnostic Checklist

Use this checklist to systematically troubleshoot:

- [ ] S3 bucket exists and is accessible (test with AWS CLI)
- [ ] Direct credentials stage works (proves S3/network OK)
- [ ] Storage integration ENABLED = true
- [ ] STORAGE_AWS_ROLE_ARN matches AWS role exactly
- [ ] STORAGE_ALLOWED_LOCATIONS has trailing slash
- [ ] Trust policy Principal matches STORAGE_AWS_IAM_USER_ARN exactly
- [ ] Trust policy ExternalId matches STORAGE_AWS_EXTERNAL_ID exactly
- [ ] Trust policy Version is "2012-10-17"
- [ ] S3 permissions policy attached to role
- [ ] S3 policy includes both bucket and bucket/* resources
- [ ] No permission boundaries on role
- [ ] No AWS Organization SCPs blocking sts:AssumeRole
- [ ] Waited 2+ minutes after IAM changes
- [ ] Tested without External ID condition (temporary)
- [ ] Checked if Snowflake region is opt-in region
- [ ] If opt-in region: AWS region enabled in account
- [ ] If opt-in region: STS endpoint activated for region
- [ ] Tried recreating integration with fresh values
- [ ] Contacted Snowflake support if all else fails

---

## When to Contact Snowflake Support

Contact support if:
1. ✅ All troubleshooting steps completed
2. ✅ Direct credentials work
3. ✅ Trust policy and permissions verified multiple times
4. ✅ Region is enabled (if opt-in region)
5. ❌ Role assumption still fails

Provide:
- Snowflake account ID (`SELECT CURRENT_ACCOUNT()`)
- AWS account ID
- S3 bucket name
- IAM role ARN
- Output of `DESC INTEGRATION`
- Trust policy JSON
- Permissions policy JSON
- Complete error message
- All troubleshooting steps attempted

---

## Key Learnings

### What We Learned
1. **Direct credentials working ≠ role assumption working** - They use different AWS services (IAM vs STS)
2. **Opt-in regions are disabled by default** - Must enable region AND activate STS endpoint
3. **External ID must match exactly** - Even one character difference causes failure
4. **IAM changes take time** - Wait 1-2 minutes for propagation
5. **Trust policy alone isn't enough** - Role also needs S3 permissions policy
6. **Trailing slashes matter** - `s3://bucket` vs `s3://bucket/` are different

### Common Misconceptions
- ❌ "If trust policy is correct, it should work" - Region/STS issues can still cause failures
- ❌ "Direct credentials are always less secure" - With proper IAM user setup, both are secure
- ❌ "Recreating fixes everything" - Doesn't help if underlying issue is regional
- ❌ "Error is always in AWS configuration" - Sometimes it's Snowflake-side (like region)

### Best Practices
- ✅ Always test direct credentials first to isolate the problem
- ✅ Check Snowflake region before troubleshooting role issues
- ✅ Copy External ID directly from Snowflake (avoid manual typing)
- ✅ Document your configuration for future reference
- ✅ Use meaningful names for integrations and roles
- ✅ Keep AWS policies minimal (least privilege)

---

## Related Resources

### Snowflake Documentation
- [Storage Integration Reference](https://docs.snowflake.com/en/sql-reference/sql/create-storage-integration)
- [External Stages](https://docs.snowflake.com/en/user-guide/data-load-s3)
- [COPY INTO Command](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table)

### AWS Documentation
- [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [STS AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
- [Opt-In Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html)
- [STS Regional Endpoints](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html)

---

## Version History

- **v1.0** (2026-09-25): Initial documentation based on comprehensive troubleshooting session
  - Documented opt-in region STS endpoint issue
  - Added systematic troubleshooting steps
  - Included alternative direct credentials approach
  - Created diagnostic checklist

---

*This skill was created from real-world troubleshooting experience and should be referenced when debugging Snowflake S3 storage integration issues.*
