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

      This type contains a URI and a description for external data that users
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
      :ref:`\<preferredSiteAnalysisID\><SERA_quakeml-siteDescription-preferredSiteAnalysisID>`, anyURI, "optional" 
      :ref:`\<preferredVelocityProfileID\><SERA_quakeml-siteDescription-preferredVelocityProfileID>`, anyURI, "optional" 
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

   .. container:: description

      This type is used to represent real values with uncertainty.






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

   .. container:: description

      This type is used to represent real values with uncertainty.






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

   .. container:: description

      This type is used to represent real values with uncertainty.






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

   .. container:: description

      This type is used to represent real values with uncertainty.






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

   .. container:: description

      This type is used to represent real values with uncertainty.






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

   .. container:: description

      Quantitative description of the surface.






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

   .. container:: description

      Site Indicators related to the morpohology of a site.






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

   .. container:: description

      Ground type according to Eurocode 8 (EC8 § 3.1.2, Table 3.1),
      based on the velocityS30 value and the geotechnical description.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8qindex1:

<siteClassEC8Qindex1>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Qindex1

   .. container:: description

      This type is used to represent real values with uncertainty.






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

   .. container:: description

      This type is used to provide reference information for site indicators.






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
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-fileresource:

<fileResource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><SERA_quakeml-siteDescription-siteMorphology-siteClassEC8Reference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-fileresource-description:

<description>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-siteclassec8reference-fileresource-url:

<url>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepth:

<bedrockDepth>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepth

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <bedrockDepth>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepth-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepth-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepth-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepth-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthqindex1:

<bedrockDepthQindex1>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthQindex1

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <bedrockDepthQindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthQindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthQindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthqindex1-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthqindex1-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference:

<bedrockDepthReference>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference

   .. container:: description

      This type is used to provide reference information for site indicators.






   **Sub Elements of <bedrockDepthReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource:

<literatureSource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource-title:

<title>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource-secondaryauthors:

<secondaryAuthors>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource-year:

<year>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource-booktitle:

<booktitle>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource-doi:

<doi>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource-language:

<language>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-literaturesource-language-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-fileresource:

<fileResource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><SERA_quakeml-siteDescription-siteMorphology-bedrockDepthReference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-fileresource-description:

<description>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-bedrockdepthreference-fileresource-url:

<url>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800:

<h800>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <h800>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-siteMorphology-h800-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-siteMorphology-h800-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800qindex1:

<h800Qindex1>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Qindex1

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <h800Qindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-siteMorphology-h800Qindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-siteMorphology-h800Qindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800qindex1-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800qindex1-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference:

<h800Reference>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference

   .. container:: description

      This type is used to provide reference information for site indicators.






   **Sub Elements of <h800Reference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource:

<literatureSource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource-title:

<title>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource-secondaryauthors:

<secondaryAuthors>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource-year:

<year>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource-booktitle:

<booktitle>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource-doi:

<doi>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource-language:

<language>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-literaturesource-language-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-fileresource:

<fileResource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><SERA_quakeml-siteDescription-siteMorphology-h800Reference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-fileresource-description:

<description>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-h800reference-fileresource-url:

<url>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunit:

<geologicalUnit>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnit

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Free text description of the surface geology of a site




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitqindex1:

<geologicalUnitQindex1>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitQindex1

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <geologicalUnitQindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitQindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitQindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitqindex1-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitqindex1-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalmapscale:

<geologicalMapScale>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalMapScale

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Scale of geological map used for the description of
      surface geology provided in geologicalUnit




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitoge:

<geologicalUnitOGE>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitOGE

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      Description of the surface geology according to a
      Unified, Pan-European Map




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference:

<geologicalUnitReference>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference

   .. container:: description

      This type is used to provide reference information for site indicators.






   **Sub Elements of <geologicalUnitReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource:

<literatureSource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource-title:

<title>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource-secondaryauthors:

<secondaryAuthors>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource-year:

<year>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource-booktitle:

<booktitle>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource-doi:

<doi>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource-language:

<language>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-literaturesource-language-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-fileresource:

<fileResource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><SERA_quakeml-siteDescription-siteMorphology-geologicalUnitReference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-fileresource-description:

<description>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-sitemorphology-geologicalunitreference-fileresource-url:

<url>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-preferredsiteanalysisid:

<preferredSiteAnalysisID>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` preferredSiteAnalysisID

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-preferredvelocityprofileid:

<preferredVelocityProfileID>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` preferredVelocityProfileID

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-overallqindex:

<overallQindex>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` overallQindex

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <overallQindex>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteDescription-overallQindex-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteDescription-overallQindex-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-overallqindex-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` overallQindex :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-overallqindex-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` overallQindex :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment:

<comment>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment




   **Sub Elements of <comment>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<text\><SERA_quakeml-siteDescription-comment-text>`, string, ":red:`required`" 
      :ref:`\<creationInfo\><SERA_quakeml-siteDescription-comment-creationInfo>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-text:

<text>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` text

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo:

<creationInfo>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo




   **Sub Elements of <creationInfo>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<author\><SERA_quakeml-siteDescription-comment-creationInfo-author>`, , "optional" 
      :ref:`\<agency\><SERA_quakeml-siteDescription-comment-creationInfo-agency>`, , "optional" 
      :ref:`\<creationTime\><SERA_quakeml-siteDescription-comment-creationInfo-creationTime>`, dateTime, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-author:

<author>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author

   .. container:: description

      Contact information for a person.






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

      :ref:`\<firstname\><SERA_quakeml-siteDescription-comment-creationInfo-author-firstname>`, string, ":red:`required`" 
      :ref:`\<lastname\><SERA_quakeml-siteDescription-comment-creationInfo-author-lastname>`, string, ":red:`required`" 
      :ref:`\<mbox\><SERA_quakeml-siteDescription-comment-creationInfo-author-mbox>`, string, ":red:`required`" 
      :ref:`\<homepage\><SERA_quakeml-siteDescription-comment-creationInfo-author-homepage>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-author-firstname:

<firstname>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-author-lastname:

<lastname>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` lastname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-author-mbox:

<mbox>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-author-homepage:

<homepage>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency:

<agency>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency




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

      :ref:`\<name\><SERA_quakeml-siteDescription-comment-creationInfo-agency-name>`, string, ":red:`required`" 
      :ref:`\<mbox\><SERA_quakeml-siteDescription-comment-creationInfo-agency-mbox>`, string, "optional" 
      :ref:`\<phone\><SERA_quakeml-siteDescription-comment-creationInfo-agency-phone>`, string, "optional" 
      :ref:`\<homepage\><SERA_quakeml-siteDescription-comment-creationInfo-agency-homepage>`, anyURI, "optional" 
      :ref:`\<postalAddress\><SERA_quakeml-siteDescription-comment-creationInfo-agency-postalAddress>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-name:

<name>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-mbox:

<mbox>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-phone:

<phone>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` phone

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-homepage:

<homepage>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-postaladdress:

<postalAddress>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress




   **Sub Elements of <postalAddress>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<streetAddress\><SERA_quakeml-siteDescription-comment-creationInfo-agency-postalAddress-streetAddress>`, string, ":red:`required`" 
      :ref:`\<locality\><SERA_quakeml-siteDescription-comment-creationInfo-agency-postalAddress-locality>`, string, ":red:`required`" 
      :ref:`\<postalCode\><SERA_quakeml-siteDescription-comment-creationInfo-agency-postalAddress-postalCode>`, string, ":red:`required`" 
      :ref:`\<country\><SERA_quakeml-siteDescription-comment-creationInfo-agency-postalAddress-country>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-postaladdress-streetaddress:

<streetAddress>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` streetAddress

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-postaladdress-locality:

<locality>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` locality

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-postaladdress-postalcode:

<postalCode>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalCode

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-postaladdress-country:

<country>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country




   **Sub Elements of <country>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteDescription-comment-creationInfo-agency-postalAddress-country-code>`, string, ":red:`required`" 
      :ref:`\<country\><SERA_quakeml-siteDescription-comment-creationInfo-agency-postalAddress-country-country>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-postaladdress-country-code:

<code>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-agency-postaladdress-country-country:

<country>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitedescription-comment-creationinfo-creationtime:

<creationTime>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters:

<siteCharacterizationParameters>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters




   **Attributes of <siteCharacterizationParameters>**: 

   .. tabularcolumns::|l|l|l|1|1| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "attribute", "type", "required", "description", "example"
      :widths: auto

      **publicID**, :ref:`ResourceIdentifier<type-glossary>`, no, "", "" 




   **Sub Elements of <siteCharacterizationParameters>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<analysis\><SERA_quakeml-siteCharacterizationParameters-analysis>`, , "optional, many" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis:

<analysis>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis

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

      :ref:`\<siteDescriptionID\><SERA_quakeml-siteCharacterizationParameters-analysis-siteDescriptionID>`, anyURI, ":red:`required`" 
      :ref:`\<creationInfo\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo>`, , "optional" 
      :ref:`\<comment\><SERA_quakeml-siteCharacterizationParameters-analysis-comment>`, , "optional, many" 
      :ref:`\<resonanceFrequency\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequency>`, , "optional" 
      :ref:`\<resonanceFrequencyQindex1\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyQindex1>`, , "optional" 
      :ref:`\<resonanceFrequencyMethod\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyMethod>`, string, "optional, many" 
      :ref:`\<resonanceFrequencyReference\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference>`, , "optional" 
      :ref:`\<velocityS30\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30>`, , "optional" 
      :ref:`\<velocityS30Qindex1\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Qindex1>`, , "optional" 
      :ref:`\<velocityS30Method\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Method>`, string, "optional, many" 
      :ref:`\<velocityS30MethodCombIndex\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30MethodCombIndex>`, double, "optional" 
      :ref:`\<velocityS30ManualIndex\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30ManualIndex>`, double, "optional" 
      :ref:`\<velocityS30Reference\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference>`, , "optional" 
      :ref:`\<velocityProfileCount\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileCount>`, decimal, "optional" 
      :ref:`\<sptLogsCount\><SERA_quakeml-siteCharacterizationParameters-analysis-sptLogsCount>`, decimal, "optional" 
      :ref:`\<cptLogsCount\><SERA_quakeml-siteCharacterizationParameters-analysis-cptLogsCount>`, decimal, "optional" 
      :ref:`\<boreholeLogsCount\><SERA_quakeml-siteCharacterizationParameters-analysis-boreholeLogsCount>`, decimal, "optional" 
      :ref:`\<velocityProfile\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile>`, , "optional, many" 
      :ref:`\<velocityProfileQindex1\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileQindex1>`, , "optional" 
      :ref:`\<velocityProfileReference\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-sitedescriptionid:

<siteDescriptionID>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteDescriptionID

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo:

<creationInfo>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo

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

      :ref:`\<author\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-author>`, , "optional" 
      :ref:`\<agency\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency>`, , "optional" 
      :ref:`\<creationTime\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-creationTime>`, dateTime, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-author:

<author>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author

   .. container:: description

      Contact information for a person.






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

      :ref:`\<firstname\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-author-firstname>`, string, ":red:`required`" 
      :ref:`\<lastname\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-author-lastname>`, string, ":red:`required`" 
      :ref:`\<mbox\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-author-mbox>`, string, ":red:`required`" 
      :ref:`\<homepage\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-author-homepage>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-author-firstname:

<firstname>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-author-lastname:

<lastname>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` lastname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-author-mbox:

<mbox>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-author-homepage:

<homepage>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency:

<agency>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency




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

      :ref:`\<name\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-name>`, string, ":red:`required`" 
      :ref:`\<mbox\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-mbox>`, string, "optional" 
      :ref:`\<phone\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-phone>`, string, "optional" 
      :ref:`\<homepage\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-homepage>`, anyURI, "optional" 
      :ref:`\<postalAddress\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-postalAddress>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-name:

<name>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-mbox:

<mbox>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-phone:

<phone>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` phone

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-homepage:

<homepage>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-postaladdress:

<postalAddress>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress




   **Sub Elements of <postalAddress>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<streetAddress\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-postalAddress-streetAddress>`, string, ":red:`required`" 
      :ref:`\<locality\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-postalAddress-locality>`, string, ":red:`required`" 
      :ref:`\<postalCode\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-postalAddress-postalCode>`, string, ":red:`required`" 
      :ref:`\<country\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-postalAddress-country>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-postaladdress-streetaddress:

<streetAddress>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` streetAddress

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-postaladdress-locality:

<locality>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` locality

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-postaladdress-postalcode:

<postalCode>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalCode

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-postaladdress-country:

<country>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country




   **Sub Elements of <country>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-postalAddress-country-code>`, string, ":red:`required`" 
      :ref:`\<country\><SERA_quakeml-siteCharacterizationParameters-analysis-creationInfo-agency-postalAddress-country-country>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-postaladdress-country-code:

<code>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-agency-postaladdress-country-country:

<country>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-creationinfo-creationtime:

<creationTime>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment:

<comment>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment




   **Sub Elements of <comment>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<text\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-text>`, string, ":red:`required`" 
      :ref:`\<creationInfo\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-text:

<text>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` text

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo:

<creationInfo>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo




   **Sub Elements of <creationInfo>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<author\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-author>`, , "optional" 
      :ref:`\<agency\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency>`, , "optional" 
      :ref:`\<creationTime\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-creationTime>`, dateTime, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-author:

<author>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author

   .. container:: description

      Contact information for a person.






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

      :ref:`\<firstname\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-author-firstname>`, string, ":red:`required`" 
      :ref:`\<lastname\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-author-lastname>`, string, ":red:`required`" 
      :ref:`\<mbox\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-author-mbox>`, string, ":red:`required`" 
      :ref:`\<homepage\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-author-homepage>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-author-firstname:

<firstname>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-author-lastname:

<lastname>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` lastname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-author-mbox:

<mbox>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-author-homepage:

<homepage>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency:

<agency>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency




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

      :ref:`\<name\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-name>`, string, ":red:`required`" 
      :ref:`\<mbox\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-mbox>`, string, "optional" 
      :ref:`\<phone\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-phone>`, string, "optional" 
      :ref:`\<homepage\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-homepage>`, anyURI, "optional" 
      :ref:`\<postalAddress\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-postalAddress>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-name:

<name>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-mbox:

<mbox>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-phone:

<phone>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` phone

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-homepage:

<homepage>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-postaladdress:

<postalAddress>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress




   **Sub Elements of <postalAddress>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<streetAddress\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-postalAddress-streetAddress>`, string, ":red:`required`" 
      :ref:`\<locality\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-postalAddress-locality>`, string, ":red:`required`" 
      :ref:`\<postalCode\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-postalAddress-postalCode>`, string, ":red:`required`" 
      :ref:`\<country\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-postalAddress-country>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-postaladdress-streetaddress:

<streetAddress>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` streetAddress

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-postaladdress-locality:

<locality>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` locality

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-postaladdress-postalcode:

<postalCode>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalCode

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-postaladdress-country:

<country>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country




   **Sub Elements of <country>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-postalAddress-country-code>`, string, ":red:`required`" 
      :ref:`\<country\><SERA_quakeml-siteCharacterizationParameters-analysis-comment-creationInfo-agency-postalAddress-country-country>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-postaladdress-country-code:

<code>     :red:`required`
############################################################
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-agency-postaladdress-country-country:

<country>     :red:`required`
############################################################
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-comment-creationinfo-creationtime:

<creationTime>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequency:

<resonanceFrequency>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequency

   .. container:: description

      Resonance frequency of the soil column at each location/site.

      This type is used to represent real values with uncertainty.






   **Sub Elements of <resonanceFrequency>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequency-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequency-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequency-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequency-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyqindex1:

<resonanceFrequencyQindex1>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyQindex1

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <resonanceFrequencyQindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyQindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyQindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyqindex1-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyqindex1-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencymethod:

<resonanceFrequencyMethod>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyMethod

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference:

<resonanceFrequencyReference>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference

   .. container:: description

      Literature or web reference providing detailed information
      on the methodology adopted for determining the resonance frequency.

      This type is used to provide reference information for site indicators.






   **Sub Elements of <resonanceFrequencyReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource:

<literatureSource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource-title:

<title>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource-secondaryauthors:

<secondaryAuthors>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource-year:

<year>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource-booktitle:

<booktitle>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource-doi:

<doi>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource-language:

<language>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-literaturesource-language-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-fileresource:

<fileResource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><SERA_quakeml-siteCharacterizationParameters-analysis-resonanceFrequencyReference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-fileresource-description:

<description>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-resonancefrequencyreference-fileresource-url:

<url>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` resonanceFrequencyReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30:

<velocityS30>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30

   .. container:: description

      Average shear-wave velocity between 0 and 30 meters depth.

      This type is used to represent real values with uncertainty.






   **Sub Elements of <velocityS30>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30qindex1:

<velocityS30Qindex1>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Qindex1

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <velocityS30Qindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Qindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Qindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30qindex1-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30qindex1-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30method:

<velocityS30Method>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Method

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30methodcombindex:

<velocityS30MethodCombIndex>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30MethodCombIndex

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30manualindex:

<velocityS30ManualIndex>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30ManualIndex

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference:

<velocityS30Reference>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference

   .. container:: description

      Literature or web reference providing detailed information
      on the methodology adopted for determining the velocityS30 value.

      This type is used to provide reference information for site indicators.






   **Sub Elements of <velocityS30Reference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource:

<literatureSource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource-title:

<title>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource-secondaryauthors:

<secondaryAuthors>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource-year:

<year>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource-booktitle:

<booktitle>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource-doi:

<doi>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource-language:

<language>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-literaturesource-language-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-fileresource:

<fileResource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityS30Reference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-fileresource-description:

<description>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocitys30reference-fileresource-url:

<url>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS30Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilecount:

<velocityProfileCount>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: velocityProfileCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: velocityProfileCount :math:`\ge` 0

   .. container:: description

      Number of Velocity profile(s) that are available for this site.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-sptlogscount:

<sptLogsCount>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` sptLogsCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: sptLogsCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: sptLogsCount :math:`\ge` 0

   .. container:: description

      Number of SPT log profile(s) that are available for this site.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-cptlogscount:

<cptLogsCount>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` cptLogsCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: cptLogsCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: cptLogsCount :math:`\ge` 0

   .. container:: description

      Number of CPT log profile(s) that are available for this site.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-boreholelogscount:

<boreholeLogsCount>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` boreholeLogsCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: boreholeLogsCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: boreholeLogsCount :math:`\ge` 0

   .. container:: description

      Number of borehole log profile(s) that are available for this site.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile:

<velocityProfile>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile

   .. container:: description

      One or more velocity profiles associated with this analysis.






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

      :ref:`\<layerCount\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-layerCount>`, decimal, ":red:`required`" 
      :ref:`\<velocityProfileData\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData>`, , ":red:`required, many`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-layercount:

<layerCount>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerCount

   .. container:: type

			.. only:: latex

					content type: :ref:`decimal<type-glossary>`

					range: layerCount :math:`\ge` 0

			.. only:: html

					content type: `decimal <appendices.html#glossary-decimal>`_

					range: layerCount :math:`\ge` 0


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata:

<velocityProfileData>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData




   **Sub Elements of <velocityProfileData>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<velocityP\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-velocityP>`, , "optional" 
      :ref:`\<velocityS\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-velocityS>`, , "optional" 
      :ref:`\<density\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-density>`, , "optional" 
      :ref:`\<layerThickness\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-layerThickness>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-velocityp:

<velocityP>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityP

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <velocityP>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-velocityP-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-velocityP-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-velocityp-value:

<value>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityP :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-velocityp-uncertainty:

<uncertainty>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityP :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-velocitys:

<velocityS>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <velocityS>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-velocityS-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-velocityS-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-velocitys-value:

<value>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-velocitys-uncertainty:

<uncertainty>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityS :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-density:

<density>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` density

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <density>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-density-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-density-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-density-value:

<value>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` density :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-density-uncertainty:

<uncertainty>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` density :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-layerthickness:

<layerThickness>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness




   **Sub Elements of <layerThickness>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<layerTopDepth\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-layerThickness-layerTopDepth>`, , ":red:`required`" 
      :ref:`\<layerBottomDepth\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-layerThickness-layerBottomDepth>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-layerthickness-layertopdepth:

<layerTopDepth>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerTopDepth

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <layerTopDepth>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-layerThickness-layerTopDepth-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-layerThickness-layerTopDepth-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-layerthickness-layertopdepth-value:

<value>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerTopDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-layerthickness-layertopdepth-uncertainty:

<uncertainty>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerTopDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-layerthickness-layerbottomdepth:

<layerBottomDepth>
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerBottomDepth

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <layerBottomDepth>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-layerThickness-layerBottomDepth-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfile-velocityProfileData-layerThickness-layerBottomDepth-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-layerthickness-layerbottomdepth-value:

<value>     :red:`required`
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerBottomDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofile-velocityprofiledata-layerthickness-layerbottomdepth-uncertainty:

<uncertainty>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfile :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileData :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerThickness :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` layerBottomDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofileqindex1:

<velocityProfileQindex1>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileQindex1

   .. container:: description

      This type is used to represent real values with uncertainty.






   **Sub Elements of <velocityProfileQindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileQindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileQindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofileqindex1-value:

<value>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofileqindex1-uncertainty:

<uncertainty>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference:

<velocityProfileReference>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference

   .. container:: description

      This type is used to provide reference information for site indicators.






   **Sub Elements of <velocityProfileReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource:

<literatureSource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource-title:

<title>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource-secondaryauthors:

<secondaryAuthors>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource-year:

<year>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource-booktitle:

<booktitle>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource-doi:

<doi>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource-language:

<language>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-literaturesource-language-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-fileresource:

<fileResource>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><SERA_quakeml-siteCharacterizationParameters-analysis-velocityProfileReference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-fileresource-description:

<description>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sera_quakeml-sitecharacterizationparameters-analysis-velocityprofilereference-fileresource-url:

<url>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      SERA_quakeml :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteCharacterizationParameters :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` analysis :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` velocityProfileReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_

