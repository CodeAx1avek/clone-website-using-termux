import subprocess
def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass
# print(B+"http or https : ")
# htt = int(input(B+"Enter :"))
# print('Website Example: codeax1.herokuapp.com')
# inp = input("Enter Website name without http or https: ")
# runcmd("wget --random-wait -r -p robots=off -U mozilla http://codeax1.herokuapp.com", verbose = True)
