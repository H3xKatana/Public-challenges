import subprocess

questions_and_answers = [
    
    ("Q1: What is the attacker ip addresse and protocol used nexus{ip_protocol-used} ?", "nexus{192.168.100.13_ssh}"),
    ("Q2: What is coommit id for first commit from the attacker, the attacker email used , the imporsonated github profile  ? nexus{commit-hash_email_githubaccount}", "nexus{a30b48a12aedf79decc3809b3d77dc2e3466816e_kamoudz34@gmail.com_achrafness}"),
    ("Q3: What is the suspicious package/module used , version , domain name of the attacker nexus{package-name_version_attacker-domain}", "nexus{flask_auth_system_0.0.2_kubershell.io}"),
    ("Q4: What is the mitre technique used by attacker for privilege escalation and file path used nexus{mitre-code_file-path} ", "nexus{T1548.003_/usr/bin/python3}"
    "/usr/bin/python3"),
]

def run_netcat_session():
    for question, correct_answer in questions_and_answers:
        user_answer = input(f"{question}\n>> ").strip()
        if user_answer == correct_answer:
            print("Correct! Moving to the next question.\n")
        else:
            print("Incorrect. Exiting ...")
            return
    print("You have succefully answered all the questions. Here is your flag: \n\n")        
    print("nexus{op3r4tion_3nd1aness_initialized_through_5upply_chain!!}")

if __name__ == "__main__":
    print("\n------------------------------------------------Welcome to operation Endianess!-----------------------------------------------------------\n\n ")
    print("NOTE: You have to answer all the questions with the specified format if required to get the flag at the end. ")
    print("all answers must be wrapped with nexus{} ")
    run_netcat_session()




nexus{SvG_Xx3_SqLi_Ch41n_Re@cti0n!}
nexus{SvG_Xx3_SqL1_Ch41n_Re@cti0n!}


nexus{N0T_01D_3N0UGH_4DO5B0X?}