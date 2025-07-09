import boto3
import pdfkit

class AWSEvidenceCollector:
    def __init__(self, framework="soc2"):
        self.sts = boto3.client('sts')
        self.account_id = self.sts.get_caller_identity()["Account"]
        self.framework = framework
        
    def generate_s3_evidence(self, bucket_name):
        """Collect SOC 2/HIPAA evidence for S3 buckets"""
        s3 = boto3.client('s3')
        
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket_name)
        except s3.exceptions.ClientError:
            encryption = "No encryption configuration found."

        try:
            policy = s3.get_bucket_policy(Bucket=bucket_name)
        except s3.exceptions.ClientError:
            policy = "No bucket policy attached."

        logging = s3.get_bucket_logging(Bucket=bucket_name)
        
        html_content = f"""
        <h1>AWS S3 Compliance Evidence</h1>
        <h2>Bucket: {bucket_name}</h2>
        <h3>Framework: {self.framework.upper()}</h3>
        
        <h4>Encryption</h4>
        <pre>{encryption}</pre>
        
        <h4>Bucket Policy</h4>
        <pre>{policy}</pre>
        
        <h4>Logging Configuration</h4>
        <pre>{logging}</pre>
        """
        
        output_pdf = f"evidence_packs/{bucket_name}_evidence.pdf"
        pdfkit.from_string(html_content, output_pdf)
        print(f"Generated evidence PDF at: {output_pdf}")
        return output_pdf

if __name__ == "__main__":
    collector = AWSEvidenceCollector()
    collector.generate_s3_evidence('your-bucket-name')
