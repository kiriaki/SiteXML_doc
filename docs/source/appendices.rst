.. Put any comments here
   Be sure to indent at this level to keep it in comment.
   :file: StationXMLtoSEEDmapping.html
   .. raw:: html


*******************************************
Appendices
*******************************************

Embedded Schema Keywords
===========================================

.. include:: schema-keywords.rst

Identifiers and codes
===========================================

For information on Network, Station, Location, and Channel codes, in addition to
their combination into Source Identifiers, used in StationXML see:

http://docs.fdsn.org/projects/source-identifiers

Specifying Dates and Times
===========================================
Dates and times should be specified using the ISO 8601 specification, limited
to the following subtypes:

* "YYYY-MM-DDZ" when only a day is needed, for example in Network startDate
* "YYYY-MM-DDThh:mm:ssZ" when second precision is sufficient
* "YYYY-MM-DDThh:mm:ss.SSSZ" when subsecond precision is required, 3, 6 or 9 decimal digits may be used.

The SEED specification limited times to 4 decimal digit precision, tenth of millisecond,
but is recommended that the number of subsecond digits be a multiple of 3, corresponding
to SI unit powers.

Note that in ISO 8601 a time without a "Z" appended is generally assumed
by most string to time conversion routines to be
in local time. Because all times in StationXML should be UTC,
the FDSN strongly recommends that dates and times
have the "Z" timezone specifier appended to avoid this ambiguity.

For further information see the XML Schema recommendation from W3C at
https://www.w3.org/TR/xmlschema-2/#isoformats


.. _type-glossary:

Type Glossary
===========================================

.. include:: type-glossary.rst
