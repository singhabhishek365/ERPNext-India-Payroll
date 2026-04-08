
# import frappe
# import json





# def create_lta_component(name, salary_component, abbr, component_type, is_tax_applicable, is_reimbursement, data):
#     component = frappe.new_doc("Salary Component")
#     component.name = name
#     component.salary_component = salary_component
#     component.salary_component_abbr = abbr
#     component.type = component_type

#     component.depends_on_payment_days = data.get("depends_on_payment_days")
#     component.is_tax_applicable = is_tax_applicable
#     component.do_not_include_in_total = data.get("do_not_include_in_total")
#     component.remove_if_zero_valued = data.get("remove_if_zero_valued")
#     component.custom_is_part_of_gross_pay = data.get("is_part_of_gross_pay")
#     component.disabled = data.get("disabled")
#     component.custom_is_part_of_ctc = data.get("is_part_of_ctc")
#     component.custom_perquisite = data.get("perquisite")
#     component.custom_is_accrual = data.get("is_accrual")
#     component.custom_is_reimbursement = is_reimbursement

#     component.custom_is_part_of_appraisal = data.get("is_part_of_appraisal")
#     component.custom_tax_exemption_applicable_based_on_regime = data.get("tax_applicable_based_on_regime")
#     component.custom_regime = data.get("regime")

#     component.formula = data.get("formula")
#     component.condition = data.get("condition")
#     component.custom_sequence = data.get("sequence")
#     component.component_type = name
#     component.insert()

# @frappe.whitelist()
# def get_salary_component(data=None, component=None):
#     try:
#         data = json.loads(data)
#         # custom_field = json.loads(custom_field) if custom_field else []  # Ensure custom_field is parsed as a list



#         salary_component = data.get("salary_component")
#         component_type = data.get("type")

#         if component and salary_component:
#             existing_components = frappe.get_list(
#                 'Salary Component',
#                 filters={
#                     "name": salary_component,
#                     "disabled": 0,
#                     "type": data.get("component_type"),
#                 },
#                 fields=['*']
#             )

#             if len(existing_components) > 0:
#                 get_each_doc = frappe.get_doc("Salary Component", existing_components[0].name)

#                 get_each_doc.depends_on_payment_days = data.get("depends_on_payment_days")
#                 get_each_doc.is_tax_applicable = data.get("is_tax_applicable")
#                 get_each_doc.do_not_include_in_total = data.get("do_not_include_in_total")
#                 get_each_doc.remove_if_zero_valued = data.get("remove_if_zero_valued")
#                 get_each_doc.custom_is_part_of_gross_pay = data.get("is_part_of_gross_pay")
#                 get_each_doc.disabled = data.get("disabled")
#                 get_each_doc.custom_is_part_of_ctc = data.get("is_part_of_ctc")
#                 get_each_doc.custom_perquisite = data.get("perquisite")
#                 get_each_doc.custom_is_accrual = data.get("is_accrual")
#                 get_each_doc.custom_is_reimbursement = data.get("reimbursement")
#                 get_each_doc.custom_is_part_of_appraisal = data.get("is_part_of_appraisal")
#                 get_each_doc.custom_tax_exemption_applicable_based_on_regime = data.get("tax_applicable_based_on_regime")
#                 get_each_doc.custom_regime = data.get("regime")
#                 get_each_doc.condition = data.get("condition")
#                 get_each_doc.formula = data.get("formula")

#                 get_each_doc.save()

#                 if data.get("is_arrear") == 1:

#                     arrear_check = frappe.get_list('Salary Component',
#                     filters={


#                                 "name":data.get("salary_component") + "(Arrear)",

#                             },
#                         fields=['*']
#                         )
#                     insert_doc.accounts = []

#                 if data.get("account"):
#                     insert_doc.append("accounts", {
#                         "company": frappe.defaults.get_user_default("company"),
#                         "account": data.get("account")
#                     })

#                     if len(arrear_check)==0:
#                         insert_doc = frappe.new_doc('Salary Component')
#                         insert_doc.name = data.get("salary_component") + "(Arrear)"
#                         insert_doc.salary_component = data.get("salary_component") + "(Arrear)"
#                         insert_doc.salary_component_abbr = data.get("abbr") + "Arrear"
#                         insert_doc.type = data.get("component_type")
#                         insert_doc.is_tax_applicable = 1
#                         insert_doc.depends_on_payment_days = 0
#                         insert_doc.round_to_the_nearest_integer = 1
#                         insert_doc.do_not_include_in_total = 0
#                         insert_doc.custom_is_part_of_gross_pay = 1
#                         insert_doc.custom_is_part_of_ctc = 0
#                         insert_doc.custom_is_arrear = 1
#                         insert_doc.custom_tax_exemption_applicable_based_on_regime = 1
#                         insert_doc.custom_regime = "All"
#                         insert_doc.custom_component = data.get("salary_component")
                        
#                         insert_doc.accounts = []

#                         account = None
#                         if component and isinstance(component, list):
#                             account = component[0].get("account")

#                         if account:
#                             insert_doc.append("accounts", {
#                                 "company": frappe.defaults.get_user_default("company"),
#                                 "account": account
#                             })
#                         insert_doc.insert()
                       







#                 if data.get("visibility_type")=="Fixed":
#                     get_library_item = frappe.get_doc('Salary Component Library Item',salary_component)
#                     get_library_item.component_added = 1
#                     get_library_item.save()
#                     frappe.msgprint("Salary Component Added")
#                 else:

#                     frappe.msgprint("Salary Component Added")

#             else:
#                 get_abbr_component = frappe.get_list('Salary Component',
#                     filters={

#                         "disabled":0,

#                         "salary_component_abbr":data.get("abbr"),


#                         },
#                         fields=['*']
#                         )

#                 if len(get_abbr_component)>0:
#                     frappe.msgprint("Another component uses same abbr,plz change the abbr")

#                 else:
#                     get_each_doc = frappe.new_doc('Salary Component')
#                     get_each_doc.name=data.get("salary_component")
#                     get_each_doc.salary_component=data.get("salary_component")
#                     get_each_doc.salary_component_abbr=data.get("abbr")
#                     get_each_doc.type=data.get("component_type")

#                     get_each_doc.depends_on_payment_days=data.get("depends_on_payment_days")
#                     get_each_doc.is_tax_applicable=data.get("is_tax_applicable")
#                     get_each_doc.do_not_include_in_total=data.get("do_not_include_in_total")
#                     get_each_doc.remove_if_zero_valued=data.get("remove_if_zero_valued")
#                     get_each_doc.custom_is_part_of_gross_pay=data.get("is_part_of_gross_pay")
#                     get_each_doc.disabled=data.get("disabled")
#                     get_each_doc.custom_is_part_of_ctc=data.get("is_part_of_ctc")
#                     get_each_doc.custom_perquisite=data.get("perquisite")
#                     get_each_doc.custom_is_accrual=data.get("is_accrual")
#                     get_each_doc.custom_is_reimbursement=data.get("reimbursement")

#                     get_each_doc.custom_is_part_of_appraisal=data.get("is_part_of_appraisal")
#                     get_each_doc.custom_tax_exemption_applicable_based_on_regime=data.get("tax_applicable_based_on_regime")
#                     get_each_doc.custom_regime=data.get("regime")

#                     get_each_doc.insert()

                   

#                     if data.get("is_arrear") == 1:
#                         insert_doc = frappe.new_doc('Salary Component')
#                         insert_doc.name = data.get("salary_component") + "(Arrear)"
#                         insert_doc.salary_component = data.get("salary_component") + "(Arrear)"
#                         insert_doc.salary_component_abbr = data.get("abbr") + "(Arrear)"
#                         insert_doc.type = data.get("component_type")
#                         insert_doc.is_tax_applicable = 1
#                         insert_doc.depends_on_payment_days = 0
#                         insert_doc.round_to_the_nearest_integer = 1
#                         insert_doc.do_not_include_in_total = 0
#                         insert_doc.custom_is_part_of_gross_pay = 1
#                         insert_doc.custom_is_part_of_ctc = 0
#                         insert_doc.custom_is_arrear = 1
#                         insert_doc.custom_tax_exemption_applicable_based_on_regime = 1
#                         insert_doc.custom_regime = data.get("regime")
#                         insert_doc.custom_component = data.get("salary_component")
#                         insert_doc.accounts = []

#                         account = None
#                         if component and isinstance(component, list):
#                             account = component[0].get("account")

#                         if account:
#                             insert_doc.append("accounts", {
#                                 "company": frappe.defaults.get_user_default("company"),
#                                 "account": account
#                             })
#                         insert_doc.insert()



#                     if data.get("visibility_type")=="Fixed":
#                         get_library_item = frappe.get_doc('Salary Component Library Item',salary_component)
#                         get_library_item.component_added = 1
#                         get_library_item.save()
#                         frappe.msgprint("Salary Component Added")
#                     else:

#                         frappe.msgprint("Salary Component Added")








#         elif component_type != "LTA Reimbursement":
#             get_each_doc = frappe.new_doc('Salary Component')
#             get_each_doc.name=data.get("salary_component")
#             get_each_doc.salary_component=data.get("salary_component")
#             get_each_doc.salary_component_abbr=data.get("abbr")
#             get_each_doc.type=data.get("component_type")

#             get_each_doc.depends_on_payment_days=data.get("depends_on_payment_days")
#             get_each_doc.is_tax_applicable=data.get("is_tax_applicable")
#             get_each_doc.do_not_include_in_total=data.get("do_not_include_in_total")
#             get_each_doc.remove_if_zero_valued=data.get("remove_if_zero_valued")
#             get_each_doc.custom_is_part_of_gross_pay=data.get("is_part_of_gross_pay")
#             get_each_doc.disabled=data.get("disabled")
#             get_each_doc.custom_is_part_of_ctc=data.get("is_part_of_ctc")
#             get_each_doc.custom_perquisite=data.get("perquisite")
#             get_each_doc.custom_is_accrual=data.get("is_accrual")
#             get_each_doc.custom_is_reimbursement=data.get("reimbursement")

#             get_each_doc.custom_is_part_of_appraisal=data.get("is_part_of_appraisal")
#             get_each_doc.custom_tax_exemption_applicable_based_on_regime=data.get("tax_applicable_based_on_regime")
#             get_each_doc.custom_regime=data.get("regime")

#             get_each_doc.formula=data.get("formula")
#             get_each_doc.condition=data.get("condition")
#             get_each_doc.custom_sequence=data.get("sequence")


#             get_each_doc.insert()

#             if data.get("visibility_type")=="Fixed":
#                 get_library_item = frappe.get_doc('Salary Component Library Item',salary_component)
#                 get_library_item.component_added = 1
#                 get_library_item.save()
#                 frappe.msgprint("Salary Component Added")
#             else:

#                 frappe.msgprint("Salary Component Added")



#         elif component_type == "LTA Reimbursement":
#             create_lta_component("LTA Reimbursement", salary_component, data.get("abbr"), data.get("component_type"), data.get("is_tax_applicable"), data.get("reimbursement"), data)
#             create_lta_component("LTA Taxable", "LTA Taxable", "LTA_TAX", data.get("component_type"), 1, 0, data)
#             create_lta_component("LTA Non Taxable", "LTA Non Taxable", "LTA_NON_TAX", data.get("component_type"), 0, 0, data)

#             if data.get("visibility_type")=="Fixed":
#                 get_library_item = frappe.get_doc('Salary Component Library Item',salary_component)
#                 get_library_item.component_added = 1
#                 get_library_item.save()
#                 frappe.msgprint("Salary Component Added")
#             else:

#                 frappe.msgprint("Salary Component Added")








#     except Exception as e:
#         frappe.log_error(f"Error in get_salary_component: {e}")
#         raise




import frappe
import json


# -------------------------------
# COMMON HELPER: ADD ACCOUNTS
# -------------------------------
def add_account_row(doc, account):
    if not account:
        return

    doc.accounts = []
    doc.append("accounts", {
        "company": frappe.defaults.get_user_default("company"),
        "account": account
    })


# -------------------------------
# CREATE GENERIC SALARY COMPONENT
# -------------------------------
def create_salary_component(data, account=None):
    doc = frappe.new_doc("Salary Component")

    doc.name = data.get("salary_component")
    doc.salary_component = data.get("salary_component")
    doc.salary_component_abbr = data.get("abbr")
    doc.type = data.get("component_type")

    doc.depends_on_payment_days = data.get("depends_on_payment_days")
    doc.is_tax_applicable = data.get("is_tax_applicable")
    doc.do_not_include_in_total = data.get("do_not_include_in_total")
    doc.remove_if_zero_valued = data.get("remove_if_zero_valued")

    doc.custom_is_part_of_gross_pay = data.get("is_part_of_gross_pay")
    doc.custom_is_part_of_ctc = data.get("is_part_of_ctc")
    doc.custom_perquisite = data.get("perquisite")
    doc.custom_is_accrual = data.get("is_accrual")
    doc.custom_is_reimbursement = data.get("reimbursement")

    doc.custom_is_part_of_appraisal = data.get("is_part_of_appraisal")
    doc.custom_tax_exemption_applicable_based_on_regime = data.get("tax_applicable_based_on_regime")
    doc.custom_regime = data.get("regime")

    doc.formula = data.get("formula")
    doc.condition = data.get("condition")
    doc.custom_sequence = data.get("sequence")

    doc.disabled = data.get("disabled")

    # ✅ Add account properly
    add_account_row(doc, account)

    doc.insert()
    return doc


# -------------------------------
# CREATE ARREAR COMPONENT
# -------------------------------
def create_arrear_component(data, account=None):
    arrear_name = data.get("salary_component") + "_ARR"

    # Check if already exists
    if frappe.db.exists("Salary Component", arrear_name):
        return

    doc = frappe.new_doc("Salary Component")

    doc.name = arrear_name
    doc.salary_component = arrear_name
    doc.salary_component_abbr = data.get("abbr") + "_ARR"
    doc.type = data.get("component_type")

    doc.is_tax_applicable = 1
    doc.depends_on_payment_days = 0
    doc.round_to_the_nearest_integer = 1
    doc.do_not_include_in_total = 0

    doc.custom_is_part_of_gross_pay = 1
    doc.custom_is_part_of_ctc = 0
    doc.custom_is_arrear = 1

    doc.custom_tax_exemption_applicable_based_on_regime = 1
    doc.custom_regime = "All"

    doc.custom_component = data.get("salary_component")

    # ✅ Add account
    add_account_row(doc, account)

    doc.insert()


# -------------------------------
# LTA COMPONENT CREATION
# -------------------------------
def create_lta_component(name, abbr, component_type, is_tax, is_reimbursement, data):
    doc = frappe.new_doc("Salary Component")

    doc.name = name
    doc.salary_component = name
    doc.salary_component_abbr = abbr
    doc.type = component_type

    doc.is_tax_applicable = is_tax
    doc.custom_is_reimbursement = is_reimbursement

    doc.depends_on_payment_days = data.get("depends_on_payment_days")
    doc.custom_is_part_of_gross_pay = data.get("is_part_of_gross_pay")

    doc.insert()


# -------------------------------
# MAIN API
# -------------------------------
@frappe.whitelist()
def get_salary_component(data=None, component=None):
    try:
        data = json.loads(data)
        component_type = data.get("component_type")
        salary_component = data.get("salary_component")

        account = data.get("account")

        # -------------------------------
        # UPDATE EXISTING
        # -------------------------------
        if frappe.db.exists("Salary Component", salary_component):

            doc = frappe.get_doc("Salary Component", salary_component)

            doc.depends_on_payment_days = data.get("depends_on_payment_days")
            doc.is_tax_applicable = data.get("is_tax_applicable")
            doc.do_not_include_in_total = data.get("do_not_include_in_total")
            doc.remove_if_zero_valued = data.get("remove_if_zero_valued")

            doc.custom_is_part_of_gross_pay = data.get("is_part_of_gross_pay")
            doc.custom_is_part_of_ctc = data.get("is_part_of_ctc")
            doc.custom_perquisite = data.get("perquisite")
            doc.custom_is_accrual = data.get("is_accrual")
            doc.custom_is_reimbursement = data.get("reimbursement")

            doc.custom_is_part_of_appraisal = data.get("is_part_of_appraisal")
            doc.custom_tax_exemption_applicable_based_on_regime = data.get("tax_applicable_based_on_regime")
            doc.custom_regime = data.get("regime")

            doc.formula = data.get("formula")
            doc.condition = data.get("condition")

            # ✅ Reset and re-add accounts
            doc.accounts = []
            add_account_row(doc, account)

            doc.save()

            # Create arrear if needed
            if data.get("is_arrear") == 1:
                create_arrear_component(data, account)

        # -------------------------------
        # CREATE NEW
        # -------------------------------
        else:

            # Check duplicate abbr
            if frappe.db.exists("Salary Component", {"salary_component_abbr": data.get("abbr")}):
                frappe.throw("Abbreviation already exists")

            create_salary_component(data, account)

            if data.get("is_arrear") == 1:
                create_arrear_component(data, account)

        # -------------------------------
        # LTA SPECIAL CASE
        # -------------------------------
        if component_type == "LTA Reimbursement":
            create_lta_component("LTA Reimbursement", data.get("abbr"), component_type, 1, 1, data)
            create_lta_component("LTA Taxable", "LTA_TAX", component_type, 1, 0, data)
            create_lta_component("LTA Non Taxable", "LTA_NON_TAX", component_type, 0, 0, data)

        # -------------------------------
        # LIBRARY UPDATE
        # -------------------------------
        if data.get("visibility_type") == "Fixed":
            lib = frappe.get_doc("Salary Component Library Item", salary_component)
            lib.component_added = 1
            lib.save()

        frappe.msgprint("Salary Component Processed Successfully")

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Salary Component Error")
        raise