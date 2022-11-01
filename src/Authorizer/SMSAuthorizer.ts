import Authorizer from "./Authorizer"

export default class SMSAuthorizer implements Authorizer {
    private authorized = false

    public check_authorization(security_code: number): void {
        console.log(`Checking authorization for code ${security_code}`)
        this.authorized = true
    }

    public is_authorized() {
        return this.authorized === true
    }
}
