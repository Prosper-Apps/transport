# Copyright (c) 2021, Aakvatech Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def set_dimension(src_doc, tr_doc, src_child=None, tr_child=None):
    set = frappe.get_doc("Transport Settings", "Transport Settings")
    if len(set.accounting_dimension) == 0:
        return
    for dim in set.accounting_dimension:
        if (
            dim.source_doctype == src_doc.doctype
            and dim.target_doctype == tr_doc.doctype
        ):
            value = None

            if dim.source_type == "Field" and not src_child:
                value = src_doc.get(dim.source_field_name)
            elif dim.source_type == "Value" and not src_child:
                value = dim.value
            elif dim.source_type == "Child" and src_child:
                value = src_child.get(dim.child_field_name)

            if dim.target_type == "Main" and not tr_child:
                tr_doc[dim.target_field_name] = value
            elif dim.target_type == "Child" and tr_child:
                tr_child[dim.target_child_field_name] = value
