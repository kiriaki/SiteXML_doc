.. Put any comments here

  Warning, this file is regenerated from the annotations in the schema file.

  Any changes will be overwritten by convert_xsd_to_rst.py.

.. Auto-generated rst file from scan of fdsn xsd

.. role:: blue
.. role:: red
.. role::  raw-html(raw)
	:format: html
.. role::  raw-latex(raw)
	:format: latex

.. _siteowner:

<siteOwner>     :red:`required`
============================================================
.. container:: hatnote hatnote-gray

   .. container:: description

      siteOwner is not defined in QuakeML 2.0 draft






   **Attributes of <siteOwner>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <siteOwner>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<codeName\><siteOwner-codeName>`, string, ":red:`required`" 
      :ref:`\<fullName\><siteOwner-fullName>`, string, ":red:`required`" 
      :ref:`\<contact\><siteOwner-contact>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-codename:

<codeName>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` codeName

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-fullname:

<fullName>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fullName

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact:

<contact>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact

   .. container:: description

      Contact person for this site.

      Contact information for a person. Includes personal informational and institution affiliation.






   **Sub Elements of <contact>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<person\><siteOwner-contact-person>`, , ":red:`required`" 
      :ref:`\<affiliation\><siteOwner-contact-affiliation>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-person:

<person>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` person

   .. container:: description

      Contact information for a person.






   **Attributes of <person>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <person>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<firstname\><siteOwner-contact-person-firstname>`, string, ":red:`required`" 
      :ref:`\<lastname\><siteOwner-contact-person-lastname>`, string, ":red:`required`" 
      :ref:`\<mbox\><siteOwner-contact-person-mbox>`, string, ":red:`required`" 
      :ref:`\<homepage\><siteOwner-contact-person-homepage>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-person-firstname:

<firstname>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` person :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-person-lastname:

<lastname>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` person :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` lastname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-person-mbox:

<mbox>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` person :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-person-homepage:

<homepage>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` person :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation:

<affiliation>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation




   **Sub Elements of <affiliation>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<institution\><siteOwner-contact-affiliation-institution>`, , ":red:`required`" 
      :ref:`\<department\><siteOwner-contact-affiliation-department>`, string, "optional" 
      :ref:`\<function\><siteOwner-contact-affiliation-function>`, string, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution:

<institution>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution




   **Attributes of <institution>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <institution>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<name\><siteOwner-contact-affiliation-institution-name>`, string, ":red:`required`" 
      :ref:`\<mbox\><siteOwner-contact-affiliation-institution-mbox>`, string, "optional" 
      :ref:`\<phone\><siteOwner-contact-affiliation-institution-phone>`, string, "optional" 
      :ref:`\<homepage\><siteOwner-contact-affiliation-institution-homepage>`, anyURI, "optional" 
      :ref:`\<postalAddress\><siteOwner-contact-affiliation-institution-postalAddress>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-name:

<name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-mbox:

<mbox>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-phone:

<phone>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` phone

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-homepage:

<homepage>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-postaladdress:

<postalAddress>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress




   **Sub Elements of <postalAddress>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<streetAddress\><siteOwner-contact-affiliation-institution-postalAddress-streetAddress>`, string, ":red:`required`" 
      :ref:`\<locality\><siteOwner-contact-affiliation-institution-postalAddress-locality>`, string, ":red:`required`" 
      :ref:`\<postalCode\><siteOwner-contact-affiliation-institution-postalAddress-postalCode>`, string, ":red:`required`" 
      :ref:`\<country\><siteOwner-contact-affiliation-institution-postalAddress-country>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-postaladdress-streetaddress:

<streetAddress>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` streetAddress

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-postaladdress-locality:

<locality>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` locality

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-postaladdress-postalcode:

<postalCode>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalCode

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-postaladdress-country:

<country>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country




   **Sub Elements of <country>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><siteOwner-contact-affiliation-institution-postalAddress-country-code>`, string, ":red:`required`" 
      :ref:`\<country\><siteOwner-contact-affiliation-institution-postalAddress-country-country>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-postaladdress-country-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-institution-postaladdress-country-country:

<country>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` institution :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-department:

<department>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` department

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _siteowner-contact-affiliation-function:

<function>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteOwner :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` contact :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` affiliation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` function

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

