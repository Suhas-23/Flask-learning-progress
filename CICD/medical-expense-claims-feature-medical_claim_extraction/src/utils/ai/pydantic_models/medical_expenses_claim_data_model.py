from pydantic import BaseModel, Field

class MedicalExpenseClaimDataModel(BaseModel):
    policy_issue_date: str = Field(..., title="Policy Issue Date", description="Date when the policy was issued",
                                   max_length=10, examples=["01/01/2023"])
    year: str = Field(..., title="Year", description="Year of the Policy Issuance",
                      max_length=4, examples=["2023"])
    month: str = Field(..., title="Month", description="Month of the Policy Issuance",
                       max_length=20, examples=["January"])
    policy_number: str = Field(..., title="Policy Number", description="Unique Policy Number",
                               max_length=50, examples=["MED-1234567890"])
    policy_holder: str = Field(..., title="Policy Holder", description="Name of the Policy Holder",
                               max_length=100, examples=["John Doe"])
    premium_type: str = Field(..., title="Premium Type", description="Type of Premium Payment",
                              max_length=50, examples=["Annual"])
    relationship: str = Field(..., title="Relationship", description="Relationship of Policy Holder with Insured",
                              max_length=50, examples=["Self"])
    payment_date: str = Field(..., title="Payment Date", description="Date of the Premium Payment",
                              max_length=10, examples=["01/02/2023"])
    amount: str = Field(..., title="Amount", description="Claimed Medical Expense Amount",
                        max_length=50, examples=["10000 INR"])
