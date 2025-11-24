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

.. _sera_quakeml:

<SERA_quakeml>     :red:`required`
============================================================
.. container:: hatnote hatnote-gray




   **Sub Elements of <SERA_quakeml>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<schemaVersion\><SERA_quakeml-schemaVersion>`, string, ":red:`required`" 
      :ref:`\<creationTime\><SERA_quakeml-creationTime>`, dateTime, ":red:`required`" 
      :ref:`\<externalReference\><SERA_quakeml-externalReference>`, , "optional, many" 
      :ref:`\<siteOwner\><siteOwner>`, , ":red:`required`" 
      :ref:`\<siteDescription\><SERA_quakeml-siteDescription>`, , ":red:`required`" 
      :ref:`\<siteCharacterizationParameters\><SERA_quakeml-siteCharacterizationParameters>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-schemaversion:

<schemaVersion>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` schemaVersion

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      The SiteXML schema version of this document.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-creationtime:

<creationTime>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

   .. container:: description

      Date that this document was generated




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-externalreference:

<externalReference>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` externalReference

   .. container:: description

      URI of any type of external resource that may include
      site characterization information on this site. May occur more than one time.

      This type contains a URI and description for external data that users
      may want to reference in SiteXML.






   **Sub Elements of <externalReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<URI\><SERA_quakeml-externalReference-URI>`, anyURI, ":red:`required`" 
      :ref:`\<Description\><SERA_quakeml-externalReference-Description>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-externalreference-uri:

<URI>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` externalReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` URI

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-externalreference-description:

<Description>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` externalReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` Description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription:

<siteDescription>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription




   **Attributes of <siteDescription>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <siteDescription>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<station\><SERA_quakeml-siteDescription-station>`, string, "optional" 
      :ref:`\<latitude\><SERA_quakeml-siteDescription-latitude>`, , ":red:`required`" 
      :ref:`\<longitude\><SERA_quakeml-siteDescription-longitude>`, , ":red:`required`" 
      :ref:`\<altitude\><SERA_quakeml-siteDescription-altitude>`, , "optional" 
      :ref:`\<minDistanceFromStation\><SERA_quakeml-siteDescription-minDistanceFromStation>`, , "optional" 
      :ref:`\<maxDistanceFromStation\><SERA_quakeml-siteDescription-maxDistanceFromStation>`, , "optional" 
      :ref:`\<siteTopography\><SERA_quakeml-siteDescription-siteTopography>`, , "optional" 
      :ref:`\<siteMorphology\><SERA_quakeml-siteDescription-siteMorphology>`, , "optional" 
      :ref:`\<preferredSiteAnalysisID\><SERA_quakeml-siteDescription-preferredSiteAnalysisID>`, anyURI, ":red:`required`" 
      :ref:`\<preferredVelocityProfileID\><SERA_quakeml-siteDescription-preferredVelocityProfileID>`, anyURI, ":red:`required`" 
      :ref:`\<overallQindex\><SERA_quakeml-siteDescription-overallQindex>`, , "optional" 
      :ref:`\<comment\><SERA_quakeml-siteDescription-comment>`, , "optional, many" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-station:

<station>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` station

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-latitude:

<latitude>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` latitude




   **Sub Elements of <latitude>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-latitude-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-latitude-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-latitude-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` latitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-latitude-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` latitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-longitude:

<longitude>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` longitude




   **Sub Elements of <longitude>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-longitude-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-longitude-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-longitude-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` longitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-longitude-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` longitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-altitude:

<altitude>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` altitude




   **Sub Elements of <altitude>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-altitude-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-altitude-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-altitude-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` altitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-altitude-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` altitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-mindistancefromstation:

<minDistanceFromStation>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` minDistanceFromStation




   **Sub Elements of <minDistanceFromStation>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-minDistanceFromStation-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-minDistanceFromStation-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-mindistancefromstation-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` minDistanceFromStation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-mindistancefromstation-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` minDistanceFromStation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-maxdistancefromstation:

<maxDistanceFromStation>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` maxDistanceFromStation




   **Sub Elements of <maxDistanceFromStation>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-maxDistanceFromStation-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-maxDistanceFromStation-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-maxdistancefromstation-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` maxDistanceFromStation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-maxdistancefromstation-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` maxDistanceFromStation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitetopography:

<siteTopography>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteTopography




   **Sub Elements of <siteTopography>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<schemaA\><SERA_quakeml-siteDescription-siteTopography-schemaA>`, string, ":red:`required`" 
      :ref:`\<schemaB\><SERA_quakeml-siteDescription-siteTopography-schemaB>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitetopography-schemaa:

<schemaA>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteTopography :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` schemaA

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      This is not included in 2.0




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitetopography-schemab:

<schemaB>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteTopography :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` schemaB

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology:

<siteMorphology>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology




   **Sub Elements of <siteMorphology>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<morphology\><SERA_quakeml-siteDescription-siteMorphology-morphology>`, string, "optional" 
      :ref:`\<siteClassEC8\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8>`, string, "optional" 
      :ref:`\<siteClassEC8Qindex1\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Qindex1>`, , "optional" 
      :ref:`\<siteClassEC8Reference\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference>`, , "optional" 
      :ref:`\<bedrockDepth\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepth>`, , "optional" 
      :ref:`\<bedrockDepthQindex1\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthQindex1>`, , "optional" 
      :ref:`\<bedrockDepthReference\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference>`, , "optional" 
      :ref:`\<h800\><SERA_quakeml-siteDescription-siteMorphology-h800>`, , "optional" 
      :ref:`\<h800Qindex1\><SERA_quakeml-siteDescription-siteMorphology-h800Qindex1>`, , "optional" 
      :ref:`\<h800Reference\><SERA_quakeml-siteDescription-siteMorphology-h800Reference>`, , "optional" 
      :ref:`\<geologicalUnit\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnit>`, string, "optional" 
      :ref:`\<geologicalUnitQindex1\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitQindex1>`, , "optional" 
      :ref:`\<geologicalMapScale\><SERA_quakeml-siteDescription-siteMorphology-geologicalMapScale>`, string, "optional" 
      :ref:`\<geologicalUnitOGE\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitOGE>`, string, "optional" 
      :ref:`\<geologicalUnitReference\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-morphology:

<morphology>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` morphology

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      This in not included in the QuakeML 2.0 draft




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8:

<siteClassEC8>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8qindex1:

<siteClassEC8Qindex1>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Qindex1




   **Sub Elements of <siteClassEC8Qindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Qindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Qindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8qindex1-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8qindex1-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference:

<siteClassEC8Reference>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference




   **Sub Elements of <siteClassEC8Reference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource:

<literatureSource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource-title:

<title>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource-secondaryauthors:

<secondaryAuthors>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource-year:

<year>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource-booktitle:

<booktitle>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource-doi:

<doi>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource-language:

<language>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-literaturesource-language-code:

<code>     :red:`required`
