Purchase All Shipments
======================

With the core "purchase" module, in a purchase order a button "In Shipments"
lets the user see the picking that was generated by the order itself.

With this module, that button is replaced by an "All Shipments" button that
shows the original picking, and all others that are grouped with it. This
should include pickings associated to the procurements that generated the
purchase, and also pickings that have been chained with push rules.

This is consistent with the "sale" module, where from the sale order the user
can access the generated delivery and all chained ones.

The implementation uses the procurement group of the moves in the generated
picking. The procurement group is always present in purchases, also when there
is no procurement.

Contributors
------------

* Leonardo Pistone <leonardo.pistone@camptocamp.com>

Maintainer
----------

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
