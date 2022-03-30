#include <etc/security/pam_appl.h>
#include <etc/security/pam_misc.h>
#include <stdio.h>

static struct pam_conv conv = {
	misc_conv,
	NULL
};

int main(int argc, char* argv[]){
	const char* pam_strerror(pamh, errnum);
	pam_handle_t* pamh;
	int errnum;

	int rvalue;
	const char* user = "";
	if(argc == 2){
	user = argv[1];
	}
	if(argc != 2){
	fprintf(stderr, "Check input!\n");
	return 2;
	}

	rvalue = pam_start("check", user, &conv,&pamh);

	if(rvalue == PAM_SUCCESS){
        rvalue = pam_authentificate(pamh, 0);
        }
        if(rvalue == PAM_SUCCESS){
       	rvalue = pam_acct_mgmt(pamh, 0);
        }

        if(rvalue == PAM_SUCCESS){
       	fprintf("AUTH SUCCESSFUL\n");
        }
        if(rvalue != PAM_SUCCESS){
       	fprintf("AUTH FAILURE\n");
        }

	if(pam_end(pamh,rvalue) != PAM_SUCCESS){
	pamh = NULL;
	fprintf(strerr, "Check user: failed to release authenticator ");
	return 3;
	}
	return (rvalue == PAM_SUCCESS ? 0 : 1);
}


