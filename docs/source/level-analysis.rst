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

.. _analysis:

<analysis>
============================================================
.. container:: hatnote hatnote-gray

   .. container:: description

      Each SiteXML document may include more than one Analysis objects






   **Attributes of <analysis>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <analysis>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<siteDescriptionID\><analysis-siteDescriptionID>`, anyURI, ":red:`required`" 
      :ref:`\<creationInfo\><analysis-creationInfo>`, , "optional" 
      :ref:`\<comment\><analysis-comment>`, , "optional, many" 
      :ref:`\<resonanceFrequency\><analysis-resonanceFrequency>`, , "optional" 
      :ref:`\<resonanceFrequencyQindex1\><analysis-resonanceFrequencyQindex1>`, , "optional" 
      :ref:`\<resonanceFrequencyMethod\><analysis-resonanceFrequencyMethod>`, string, "optional, many" 
      :ref:`\<resonanceFrequencyReference\><analysis-resonanceFrequencyReference>`, , "optional" 
      :ref:`\<velocityS30\><analysis-velocityS30>`, , "optional" 
      :ref:`\<velocityS30Qindex1\><analysis-velocityS30Qindex1>`, , "optional" 
      :ref:`\<velocityS30Method\><analysis-velocityS30Method>`, string, "optional, many" 
      :ref:`\<velocityS30MethodCombIndex\><analysis-velocityS30MethodCombIndex>`, double, "optional" 
      :ref:`\<velocityS30ManualIndex\><analysis-velocityS30ManualIndex>`, double, "optional" 
      :ref:`\<velocityS30Reference\><analysis-velocityS30Reference>`, , "optional" 
      :ref:`\<velocityProfileCount\><analysis-velocityProfileCount>`, decimal, "optional" 
      :ref:`\<sptLogsCount\><analysis-sptLogsCount>`, decimal, "optional" 
      :ref:`\<cptLogsCount\><analysis-cptLogsCount>`, decimal, "optional" 
      :ref:`\<boreholeLogsCount\><analysis-boreholeLogsCount>`, decimal, "optional" 
      :ref:`\<velocityProfile\><analysis-velocityProfile>`, , "optional, many" 
      :ref:`\<velocityProfileQindex1\><analysis-velocityProfileQindex1>`, , "optional" 
      :ref:`\<velocityProfileReference\><analysis-velocityProfileReference>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-sitedescriptionid:

<siteDescriptionID>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescriptionID

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_

   .. container:: description

      The Site Description this Analysis object refers to.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo:

<creationInfo>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo

   .. container:: description

      Date that this analysis was generated.
      You may not include this information if you provide referencies for the individual site indicators.






   **Sub Elements of <creationInfo>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<author\><analysis-creationInfo-author>`, , "optional" 
      :ref:`\<agency\><analysis-creationInfo-agency>`, , "optional" 
      :ref:`\<creationTime\><analysis-creationInfo-creationTime>`, dateTime, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-author:

<author>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author




   **Attributes of <author>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <author>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<firstname\><analysis-creationInfo-author-firstname>`, string, ":red:`required`" 
      :ref:`\<lastname\><analysis-creationInfo-author-lastname>`, string, ":red:`required`" 
      :ref:`\<mbox\><analysis-creationInfo-author-mbox>`, string, ":red:`required`" 
      :ref:`\<homepage\><analysis-creationInfo-author-homepage>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-author-firstname:

<firstname>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-author-lastname:

<lastname>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` lastname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-author-mbox:

<mbox>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-author-homepage:

<homepage>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency:

<agency>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency




   **Attributes of <agency>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <agency>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<name\><analysis-creationInfo-agency-name>`, string, ":red:`required`" 
      :ref:`\<mbox\><analysis-creationInfo-agency-mbox>`, string, "optional" 
      :ref:`\<phone\><analysis-creationInfo-agency-phone>`, string, "optional" 
      :ref:`\<homepage\><analysis-creationInfo-agency-homepage>`, anyURI, "optional" 
      :ref:`\<postalAddress\><analysis-creationInfo-agency-postalAddress>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-name:

<name>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-mbox:

<mbox>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-phone:

<phone>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` phone

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-homepage:

<homepage>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-postaladdress:

<postalAddress>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress




   **Sub Elements of <postalAddress>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<streetAddress\><analysis-creationInfo-agency-postalAddress-streetAddress>`, string, ":red:`required`" 
      :ref:`\<locality\><analysis-creationInfo-agency-postalAddress-locality>`, string, ":red:`required`" 
      :ref:`\<postalCode\><analysis-creationInfo-agency-postalAddress-postalCode>`, string, ":red:`required`" 
      :ref:`\<country\><analysis-creationInfo-agency-postalAddress-country>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-postaladdress-streetaddress:

<streetAddress>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` streetAddress

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-postaladdress-locality:

<locality>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` locality

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-postaladdress-postalcode:

<postalCode>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalCode

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-postaladdress-country:

<country>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country




   **Sub Elements of <country>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><analysis-creationInfo-agency-postalAddress-country-code>`, string, ":red:`required`" 
      :ref:`\<country\><analysis-creationInfo-agency-postalAddress-country-country>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-postaladdress-country-code:

<code>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-agency-postaladdress-country-country:

<country>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-creationinfo-creationtime:

<creationTime>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment:

<comment>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment




   **Sub Elements of <comment>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<text\><analysis-comment-text>`, string, ":red:`required`" 
      :ref:`\<creationInfo\><analysis-comment-creationInfo>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-text:

<text>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` text

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo:

<creationInfo>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo




   **Sub Elements of <creationInfo>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<author\><analysis-comment-creationInfo-author>`, , "optional" 
      :ref:`\<agency\><analysis-comment-creationInfo-agency>`, , "optional" 
      :ref:`\<creationTime\><analysis-comment-creationInfo-creationTime>`, dateTime, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-author:

<author>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author




   **Attributes of <author>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <author>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<firstname\><analysis-comment-creationInfo-author-firstname>`, string, ":red:`required`" 
      :ref:`\<lastname\><analysis-comment-creationInfo-author-lastname>`, string, ":red:`required`" 
      :ref:`\<mbox\><analysis-comment-creationInfo-author-mbox>`, string, ":red:`required`" 
      :ref:`\<homepage\><analysis-comment-creationInfo-author-homepage>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-author-firstname:

<firstname>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-author-lastname:

<lastname>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` lastname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-author-mbox:

<mbox>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-author-homepage:

<homepage>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency:

<agency>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency




   **Attributes of <agency>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <agency>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<name\><analysis-comment-creationInfo-agency-name>`, string, ":red:`required`" 
      :ref:`\<mbox\><analysis-comment-creationInfo-agency-mbox>`, string, "optional" 
      :ref:`\<phone\><analysis-comment-creationInfo-agency-phone>`, string, "optional" 
      :ref:`\<homepage\><analysis-comment-creationInfo-agency-homepage>`, anyURI, "optional" 
      :ref:`\<postalAddress\><analysis-comment-creationInfo-agency-postalAddress>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-name:

<name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-mbox:

<mbox>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-phone:

<phone>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` phone

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-homepage:

<homepage>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-postaladdress:

<postalAddress>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress




   **Sub Elements of <postalAddress>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<streetAddress\><analysis-comment-creationInfo-agency-postalAddress-streetAddress>`, string, ":red:`required`" 
      :ref:`\<locality\><analysis-comment-creationInfo-agency-postalAddress-locality>`, string, ":red:`required`" 
      :ref:`\<postalCode\><analysis-comment-creationInfo-agency-postalAddress-postalCode>`, string, ":red:`required`" 
      :ref:`\<country\><analysis-comment-creationInfo-agency-postalAddress-country>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-postaladdress-streetaddress:

<streetAddress>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` streetAddress

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-postaladdress-locality:

<locality>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` locality

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-postaladdress-postalcode:

<postalCode>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalCode

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-postaladdress-country:

<country>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country




   **Sub Elements of <country>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><analysis-comment-creationInfo-agency-postalAddress-country-code>`, string, ":red:`required`" 
      :ref:`\<country\><analysis-comment-creationInfo-agency-postalAddress-country-country>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-postaladdress-country-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-agency-postaladdress-country-country:

<country>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-comment-creationinfo-creationtime:

<creationTime>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequency:

<resonanceFrequency>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequency




   **Sub Elements of <resonanceFrequency>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-resonanceFrequency-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-resonanceFrequency-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequency-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequency-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyqindex1:

<resonanceFrequencyQindex1>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyQindex1




   **Sub Elements of <resonanceFrequencyQindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-resonanceFrequencyQindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-resonanceFrequencyQindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyqindex1-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyqindex1-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencymethod:

<resonanceFrequencyMethod>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyMethod

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference:

<resonanceFrequencyReference>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference




   **Sub Elements of <resonanceFrequencyReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><analysis-resonanceFrequencyReference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><analysis-resonanceFrequencyReference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource:

<literatureSource>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><analysis-resonanceFrequencyReference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><analysis-resonanceFrequencyReference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><analysis-resonanceFrequencyReference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><analysis-resonanceFrequencyReference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><analysis-resonanceFrequencyReference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><analysis-resonanceFrequencyReference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><analysis-resonanceFrequencyReference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource-title:

<title>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource-secondaryauthors:

<secondaryAuthors>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource-year:

<year>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource-booktitle:

<booktitle>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource-doi:

<doi>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource-language:

<language>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><analysis-resonanceFrequencyReference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-literaturesource-language-code:

<code>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-fileresource:

<fileResource>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><analysis-resonanceFrequencyReference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><analysis-resonanceFrequencyReference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-fileresource-description:

<description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-resonancefrequencyreference-fileresource-url:

<url>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30:

<velocityS30>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30




   **Sub Elements of <velocityS30>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-velocityS30-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-velocityS30-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30qindex1:

<velocityS30Qindex1>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Qindex1




   **Sub Elements of <velocityS30Qindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-velocityS30Qindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-velocityS30Qindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30qindex1-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30qindex1-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30method:

<velocityS30Method>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Method

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30methodcombindex:

<velocityS30MethodCombIndex>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30MethodCombIndex

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30manualindex:

<velocityS30ManualIndex>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30ManualIndex

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference:

<velocityS30Reference>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference




   **Sub Elements of <velocityS30Reference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><analysis-velocityS30Reference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><analysis-velocityS30Reference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource:

<literatureSource>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><analysis-velocityS30Reference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><analysis-velocityS30Reference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><analysis-velocityS30Reference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><analysis-velocityS30Reference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><analysis-velocityS30Reference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><analysis-velocityS30Reference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><analysis-velocityS30Reference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource-title:

<title>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource-secondaryauthors:

<secondaryAuthors>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource-year:

<year>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource-booktitle:

<booktitle>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource-doi:

<doi>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource-language:

<language>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><analysis-velocityS30Reference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-literaturesource-language-code:

<code>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-fileresource:

<fileResource>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><analysis-velocityS30Reference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><analysis-velocityS30Reference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-fileresource-description:

<description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocitys30reference-fileresource-url:

<url>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilecount:

<velocityProfileCount>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: velocityProfileCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: velocityProfileCount :math:`\ge` 0


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-sptlogscount:

<sptLogsCount>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` sptLogsCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: sptLogsCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: sptLogsCount :math:`\ge` 0


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-cptlogscount:

<cptLogsCount>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` cptLogsCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: cptLogsCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: cptLogsCount :math:`\ge` 0


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-boreholelogscount:

<boreholeLogsCount>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` boreholeLogsCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: boreholeLogsCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: boreholeLogsCount :math:`\ge` 0


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile:

<velocityProfile>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile




   **Attributes of <velocityProfile>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, :red:`yes`, "", "" 




   **Sub Elements of <velocityProfile>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<layerCount\><analysis-velocityProfile-layerCount>`, decimal, ":red:`required`" 
      :ref:`\<velocityProfileData\><analysis-velocityProfile-velocityProfileData>`, , ":red:`required, many`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-layercount:

<layerCount>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: layerCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: layerCount :math:`\ge` 0


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata:

<velocityProfileData>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData




   **Sub Elements of <velocityProfileData>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<velocityP\><analysis-velocityProfile-velocityProfileData-velocityP>`, , "optional" 
      :ref:`\<velocityS\><analysis-velocityProfile-velocityProfileData-velocityS>`, , "optional" 
      :ref:`\<density\><analysis-velocityProfile-velocityProfileData-density>`, , "optional" 
      :ref:`\<layerThickness\><analysis-velocityProfile-velocityProfileData-layerThickness>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-velocityp:

<velocityP>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityP




   **Sub Elements of <velocityP>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-velocityProfile-velocityProfileData-velocityP-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-velocityProfile-velocityProfileData-velocityP-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-velocityp-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityP :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-velocityp-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityP :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-velocitys:

<velocityS>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS




   **Sub Elements of <velocityS>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-velocityProfile-velocityProfileData-velocityS-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-velocityProfile-velocityProfileData-velocityS-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-velocitys-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-velocitys-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-density:

<density>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` density




   **Sub Elements of <density>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-velocityProfile-velocityProfileData-density-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-velocityProfile-velocityProfileData-density-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-density-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` density :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-density-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` density :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-layerthickness:

<layerThickness>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness




   **Sub Elements of <layerThickness>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<layerTopDepth\><analysis-velocityProfile-velocityProfileData-layerThickness-layerTopDepth>`, , ":red:`required`" 
      :ref:`\<layerBottomDepth\><analysis-velocityProfile-velocityProfileData-layerThickness-layerBottomDepth>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-layerthickness-layertopdepth:

<layerTopDepth>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerTopDepth




   **Sub Elements of <layerTopDepth>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-velocityProfile-velocityProfileData-layerThickness-layerTopDepth-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-velocityProfile-velocityProfileData-layerThickness-layerTopDepth-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-layerthickness-layertopdepth-value:

<value>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerTopDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-layerthickness-layertopdepth-uncertainty:

<uncertainty>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerTopDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-layerthickness-layerbottomdepth:

<layerBottomDepth>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerBottomDepth




   **Sub Elements of <layerBottomDepth>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-velocityProfile-velocityProfileData-layerThickness-layerBottomDepth-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-velocityProfile-velocityProfileData-layerThickness-layerBottomDepth-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-layerthickness-layerbottomdepth-value:

<value>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerBottomDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofile-velocityprofiledata-layerthickness-layerbottomdepth-uncertainty:

<uncertainty>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerBottomDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofileqindex1:

<velocityProfileQindex1>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileQindex1




   **Sub Elements of <velocityProfileQindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><analysis-velocityProfileQindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><analysis-velocityProfileQindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofileqindex1-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofileqindex1-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference:

<velocityProfileReference>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference




   **Sub Elements of <velocityProfileReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><analysis-velocityProfileReference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><analysis-velocityProfileReference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource:

<literatureSource>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><analysis-velocityProfileReference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><analysis-velocityProfileReference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><analysis-velocityProfileReference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><analysis-velocityProfileReference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><analysis-velocityProfileReference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><analysis-velocityProfileReference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><analysis-velocityProfileReference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource-title:

<title>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource-secondaryauthors:

<secondaryAuthors>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource-year:

<year>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource-booktitle:

<booktitle>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource-doi:

<doi>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource-language:

<language>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><analysis-velocityProfileReference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-literaturesource-language-code:

<code>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-fileresource:

<fileResource>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><analysis-velocityProfileReference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><analysis-velocityProfileReference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-fileresource-description:

<description>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _analysis-velocityprofilereference-fileresource-url:

<url>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_

