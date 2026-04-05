from unittest import case


def main():    
    # //The risk ratings are
    # //
    # // We are given a list of suspicious e-mails from the Visa VCAS system each day.
    # // Write a function that can parse an internal list of e-mails and determine which ones have a higher risk rating.

    # //0-3 - No Risk
    # //3-5 - Moderate
    # //6-10 - High Risk
    # //Emails are flagged as suspicious if:
    # //1. If the e-mail contains a + sign then we add 3 to the risk rating
    # //2. If the email requires only two or less changes to match the e-mail on the VCAS list, then we add 6 to the risk score. One change must be a swap.
    # //
    # //E.g:
    # //
    # //bob+bubc@gmail.com has a risk rating of 3   => risk score
    # //buc@gmail.com has a risk rating of 6 if cub@gmail.com is on the visa VCAS list
    # // buc -> cub swap b and c score 6

    # //happydays@gmail..com has a risk score of 0 even if dayshappy@gmail.com is on the VCAS list
    # //
    # //Your function could look something like this:
    # //
    # //public int riskRate(String[] VCASList, String email)
    # //{
    # //return -1;
    # //}
    # //
    # //You can test your code with:
    # //
    # //a+bc@gmail.co is on the VCasList what would be the risk score of

    # //
    def risk_rate(vcas_list, email):
        risk_score = 0 
        
        # check for + sign
        
        if '+' in email:
            risk_score+=3;
        
        local_email = email.split('@')[0].replace('+', '')
        for target in vcas_list:
            local_target = target.split('@')[0]
            if (check_similarity(local_email, local_target)):
                risk_score+=6
                break
        
        if risk_score >= 6:
            return "High Risk"
        elif risk_score >= 3:
            return "Moderate"
        else:
            return "No Risk"
        
    
    def check_similarity(suspicious_mail, target):
        n = len(suspicious_mail)
        if n != len(target) or n == 0:
            return False
        s_list = list(suspicious_mail)
        t_list = list(target)
        for i in range(n):
            
            for j in range(i+1, n):
                if s_list[i] == s_list[j]:
                    continue
                s_list[i], s_list[j] = s_list[j], s_list[i]
                diffs=0
                for k in range(n):
                    if s_list[k] != t_list[k]:
                        diffs+=1
                if diffs <= 1:
                    return True
                s_list[i], s_list[j] = s_list[j], s_list[i]
        return False
    
    vcas_list = ["visa@visa.com"]
    
    test_cases = [
        # --- High Risk (Score 6 or 9) ---
        ("vics@visa.com", "High Risk"),      # 0 + 6 = 6
        ("vi+cs@gmail.com", "High Risk"),    # 3 + 6 = 9
        ("aisv@visa.com", "High Risk"),      # 0 + 6 = 6
        
        # --- Moderate Risk (Score 3) ---
        ("vi+sa@visa.com", "Moderate"),     # 3 + 0 = 3
        ("visa+@outlook.com", "Moderate"),   # 3 + 0 = 3
        
        # --- No Risk (Score 0) ---
        ("vias@visa.com", "High Risk"),       # 0 (Only 1 swap, missing sub)
        ("vica@visa.com", "No Risk"),       # 0 (Only 1 sub, missing swap)
        ("viss@visa.com", "No Risk"),       # 0 (2 subs, 0 swaps)
        ("viaso@visa.com", "No Risk"),      # 0 (Length 5 vs 4 - no deletions)
        ("vis@visa.com", "No Risk"),        # 0 (Length 3 vs 4)
        ("visa@visa.com", "No Risk"),       # 0 (Identical)
        ("random@test.com", "No Risk")      # 0 (No relation)
    ]
   
    for email, expected_risk in test_cases:
        actual_risk = risk_rate(vcas_list, email)
        print(f"Email: {email}, Expected: {expected_risk}, Actual: {actual_risk}")

if __name__ == "__main__":    
    main()
    

    