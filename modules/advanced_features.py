# Member 1 - Anjali - AI Threat Detection Engine
import re

def extract_features(email_text):
    email_text = str(email_text).lower()
    features = {}

    # 1. Spoofed Sender Check
    features['spoofed_sender'] = 1 if 'via' in email_text or 'on behalf of' in email_text else 0

    # 2. Deceptive Domain - like paypaI, sb1, amaz0n
    features['deceptive_domain'] = 1 if re.search(r'paypa[lI]|sb[i1]|amaz[o0]n|g00gle', email_text) else 0

    # 3. Suspicious Attachment
    features['suspicious_attachment'] = 1 if re.search(r'\.exe|\.scr|\.js|\.bat|\.vbs', email_text) else 0

    # 4. Malicious Link - bit.ly, tinyurl, @ symbol
    features['malicious_link'] = 1 if re.search(r'bit\.ly|tinyurl|@.*\.com|shorturl', email_text) else 0

    # 5. Obfuscated URL - punycode xn--, hex
    features['obfuscated_url'] = 1 if 'xn--' in email_text or '%2e' in email_text or 'hex' in email_text else 0

    # 6. Payment Diversion - BEC Pattern 1
    features['payment_diversion'] = 1 if re.search(r'wire transfer|bank.*changed|new.*account|urgent.*payment', email_text) else 0

    # 7. Fake Invoice - BEC Pattern 2
    features['fake_invoice'] = 1 if re.search(r'invoice|past due|remit|overdue|payment receipt', email_text) else 0

    # 8. Credential Harvest - BEC Pattern 3
    features['credential_harvest'] = 1 if re.search(r'verify.*password|login.*continue|mailbox.*full|account.*locked', email_text) else 0

    # 9. Executive Impersonation - BEC Pattern 4
    features['executive_impersonation'] = 1 if re.search(r'ceo|boss|managing director|urgent.*request.*from', email_text) else 0

    # 10. Urgency Score
    urgent_words = ['urgent', 'immediate', 'asap', 'emergency', 'action required', 'within 24 hours']
    features['urgency_score'] = sum(1 for w in urgent_words if w in email_text)

    return features

# Test function
if __name__ == "__main__":
    test_mail = "Urgent! CEO asking for wire transfer to new account http://bit.ly/paypaI"
    print(extract_features(test_mail))
