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

.. _sitedescription:

<siteDescription>     :red:`required`
============================================================
.. container:: hatnote hatnote-gray




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

      :ref:`\<station\><siteDescription-station>`, string, "optional" 
      :ref:`\<latitude\><siteDescription-latitude>`, , ":red:`required`" 
      :ref:`\<longitude\><siteDescription-longitude>`, , ":red:`required`" 
      :ref:`\<altitude\><siteDescription-altitude>`, , "optional" 
      :ref:`\<minDistanceFromStation\><siteDescription-minDistanceFromStation>`, , "optional" 
      :ref:`\<maxDistanceFromStation\><siteDescription-maxDistanceFromStation>`, , "optional" 
      :ref:`\<siteTopography\><siteDescription-siteTopography>`, , "optional" 
      :ref:`\<siteMorphology\><siteDescription-siteMorphology>`, , "optional" 
      :ref:`\<preferredSiteAnalysisID\><siteDescription-preferredSiteAnalysisID>`, anyURI, ":red:`required`" 
      :ref:`\<preferredVelocityProfileID\><siteDescription-preferredVelocityProfileID>`, anyURI, ":red:`required`" 
      :ref:`\<overallQindex\><siteDescription-overallQindex>`, , "optional" 
      :ref:`\<comment\><siteDescription-comment>`, , "optional, many" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-station:

<station>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` station

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-latitude:

<latitude>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` latitude




   **Sub Elements of <latitude>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-latitude-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-latitude-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-latitude-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` latitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-latitude-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` latitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-longitude:

<longitude>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` longitude




   **Sub Elements of <longitude>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-longitude-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-longitude-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-longitude-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` longitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-longitude-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` longitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-altitude:

<altitude>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` altitude




   **Sub Elements of <altitude>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-altitude-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-altitude-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-altitude-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` altitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-altitude-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` altitude :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-mindistancefromstation:

<minDistanceFromStation>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` minDistanceFromStation




   **Sub Elements of <minDistanceFromStation>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-minDistanceFromStation-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-minDistanceFromStation-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-mindistancefromstation-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` minDistanceFromStation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-mindistancefromstation-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` minDistanceFromStation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-maxdistancefromstation:

<maxDistanceFromStation>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` maxDistanceFromStation




   **Sub Elements of <maxDistanceFromStation>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-maxDistanceFromStation-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-maxDistanceFromStation-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-maxdistancefromstation-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` maxDistanceFromStation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-maxdistancefromstation-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` maxDistanceFromStation :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitetopography:

<siteTopography>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteTopography




   **Sub Elements of <siteTopography>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<schemaA\><siteDescription-siteTopography-schemaA>`, string, ":red:`required`" 
      :ref:`\<schemaB\><siteDescription-siteTopography-schemaB>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitetopography-schemaa:

<schemaA>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteTopography :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` schemaA

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      This is not included in 2.0




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitetopography-schemab:

<schemaB>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteTopography :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` schemaB

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology:

<siteMorphology>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology




   **Sub Elements of <siteMorphology>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<morphology\><siteDescription-siteMorphology-morphology>`, string, "optional" 
      :ref:`\<siteClassEC8\><siteDescription-siteMorphology-siteClassEC8>`, string, "optional" 
      :ref:`\<siteClassEC8Qindex1\><siteDescription-siteMorphology-siteClassEC8Qindex1>`, , "optional" 
      :ref:`\<siteClassEC8Reference\><siteDescription-siteMorphology-siteClassEC8Reference>`, , "optional" 
      :ref:`\<bedrockDepth\><siteDescription-siteMorphology-bedrockDepth>`, , "optional" 
      :ref:`\<bedrockDepthQindex1\><siteDescription-siteMorphology-bedrockDepthQindex1>`, , "optional" 
      :ref:`\<bedrockDepthReference\><siteDescription-siteMorphology-bedrockDepthReference>`, , "optional" 
      :ref:`\<h800\><siteDescription-siteMorphology-h800>`, , "optional" 
      :ref:`\<h800Qindex1\><siteDescription-siteMorphology-h800Qindex1>`, , "optional" 
      :ref:`\<h800Reference\><siteDescription-siteMorphology-h800Reference>`, , "optional" 
      :ref:`\<geologicalUnit\><siteDescription-siteMorphology-geologicalUnit>`, string, "optional" 
      :ref:`\<geologicalUnitQindex1\><siteDescription-siteMorphology-geologicalUnitQindex1>`, , "optional" 
      :ref:`\<geologicalMapScale\><siteDescription-siteMorphology-geologicalMapScale>`, string, "optional" 
      :ref:`\<geologicalUnitOGE\><siteDescription-siteMorphology-geologicalUnitOGE>`, string, "optional" 
      :ref:`\<geologicalUnitReference\><siteDescription-siteMorphology-geologicalUnitReference>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-morphology:

<morphology>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` morphology

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_

   .. container:: description

      This in not included in the QuakeML 2.0 draft




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8:

<siteClassEC8>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8qindex1:

<siteClassEC8Qindex1>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Qindex1




   **Sub Elements of <siteClassEC8Qindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-siteMorphology-siteClassEC8Qindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-siteMorphology-siteClassEC8Qindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8qindex1-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8qindex1-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference:

<siteClassEC8Reference>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference




   **Sub Elements of <siteClassEC8Reference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><siteDescription-siteMorphology-siteClassEC8Reference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource:

<literatureSource>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource-title:

<title>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource-secondaryauthors:

<secondaryAuthors>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource-year:

<year>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource-booktitle:

<booktitle>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource-doi:

<doi>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource-language:

<language>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><siteDescription-siteMorphology-siteClassEC8Reference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-literaturesource-language-code:

<code>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-fileresource:

<fileResource>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><siteDescription-siteMorphology-siteClassEC8Reference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><siteDescription-siteMorphology-siteClassEC8Reference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-fileresource-description:

<description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-siteclassec8reference-fileresource-url:

<url>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteClassEC8Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepth:

<bedrockDepth>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepth




   **Sub Elements of <bedrockDepth>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-siteMorphology-bedrockDepth-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-siteMorphology-bedrockDepth-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepth-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepth-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepth :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthqindex1:

<bedrockDepthQindex1>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthQindex1




   **Sub Elements of <bedrockDepthQindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-siteMorphology-bedrockDepthQindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-siteMorphology-bedrockDepthQindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthqindex1-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthqindex1-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference:

<bedrockDepthReference>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference




   **Sub Elements of <bedrockDepthReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><siteDescription-siteMorphology-bedrockDepthReference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource:

<literatureSource>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource-title:

<title>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource-secondaryauthors:

<secondaryAuthors>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource-year:

<year>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource-booktitle:

<booktitle>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource-doi:

<doi>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource-language:

<language>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><siteDescription-siteMorphology-bedrockDepthReference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-literaturesource-language-code:

<code>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-fileresource:

<fileResource>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><siteDescription-siteMorphology-bedrockDepthReference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><siteDescription-siteMorphology-bedrockDepthReference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-fileresource-description:

<description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-bedrockdepthreference-fileresource-url:

<url>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` bedrockDepthReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800:

<h800>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800

   .. container:: description

      This is not included in the QuakeML 2.0 draft






   **Sub Elements of <h800>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-siteMorphology-h800-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-siteMorphology-h800-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800qindex1:

<h800Qindex1>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Qindex1




   **Sub Elements of <h800Qindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-siteMorphology-h800Qindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-siteMorphology-h800Qindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800qindex1-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800qindex1-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Qindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference:

<h800Reference>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference




   **Sub Elements of <h800Reference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><siteDescription-siteMorphology-h800Reference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><siteDescription-siteMorphology-h800Reference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource:

<literatureSource>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><siteDescription-siteMorphology-h800Reference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><siteDescription-siteMorphology-h800Reference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><siteDescription-siteMorphology-h800Reference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><siteDescription-siteMorphology-h800Reference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><siteDescription-siteMorphology-h800Reference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><siteDescription-siteMorphology-h800Reference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><siteDescription-siteMorphology-h800Reference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource-title:

<title>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource-secondaryauthors:

<secondaryAuthors>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource-year:

<year>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource-booktitle:

<booktitle>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource-doi:

<doi>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource-language:

<language>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><siteDescription-siteMorphology-h800Reference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-literaturesource-language-code:

<code>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-fileresource:

<fileResource>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><siteDescription-siteMorphology-h800Reference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><siteDescription-siteMorphology-h800Reference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-fileresource-description:

<description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-h800reference-fileresource-url:

<url>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` h800Reference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunit:

<geologicalUnit>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnit

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitqindex1:

<geologicalUnitQindex1>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitQindex1




   **Sub Elements of <geologicalUnitQindex1>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-siteMorphology-geologicalUnitQindex1-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-siteMorphology-geologicalUnitQindex1-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitqindex1-value:

<value>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitqindex1-uncertainty:

<uncertainty>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitQindex1 :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalmapscale:

<geologicalMapScale>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalMapScale

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitoge:

<geologicalUnitOGE>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitOGE

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference:

<geologicalUnitReference>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference




   **Sub Elements of <geologicalUnitReference>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<literatureSource\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource>`, , "optional" 
      :ref:`\<fileResource\><siteDescription-siteMorphology-geologicalUnitReference-fileResource>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource:

<literatureSource>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource




   **Sub Elements of <literatureSource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<title\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource-title>`, string, ":red:`required`" 
      :ref:`\<firstAuthor\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource-firstAuthor>`, string, ":red:`required`" 
      :ref:`\<secondaryAuthors\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource-secondaryAuthors>`, string, "optional" 
      :ref:`\<year\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource-year>`, string, "optional" 
      :ref:`\<booktitle\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource-booktitle>`, string, "optional" 
      :ref:`\<doi\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource-doi>`, string, "optional" 
      :ref:`\<language\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource-language>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource-title:

<title>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` title

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource-firstauthor:

<firstAuthor>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstAuthor

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource-secondaryauthors:

<secondaryAuthors>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` secondaryAuthors

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource-year:

<year>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` year

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource-booktitle:

<booktitle>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` booktitle

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource-doi:

<doi>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` doi

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource-language:

<language>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language




   **Sub Elements of <language>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><siteDescription-siteMorphology-geologicalUnitReference-literatureSource-language-code>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-literaturesource-language-code:

<code>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` literatureSource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` language :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-fileresource:

<fileResource>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource




   **Sub Elements of <fileResource>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<description\><siteDescription-siteMorphology-geologicalUnitReference-fileResource-description>`, string, "optional" 
      :ref:`\<url\><siteDescription-siteMorphology-geologicalUnitReference-fileResource-url>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-fileresource-description:

<description>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` description

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-sitemorphology-geologicalunitreference-fileresource-url:

<url>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` siteMorphology :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` geologicalUnitReference :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` fileResource :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` url

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-preferredsiteanalysisid:

<preferredSiteAnalysisID>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` preferredSiteAnalysisID

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_

   .. container:: description

      It is mandatory to select one Site Analysis object as the preferred.
      The Overall Quality index of the Site Characterization will be calculated using the preferred analysis.




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-preferredvelocityprofileid:

<preferredVelocityProfileID>     :red:`required`
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` preferredVelocityProfileID

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-overallqindex:

<overallQindex>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` overallQindex




   **Sub Elements of <overallQindex>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<value\><siteDescription-overallQindex-value>`, double, ":red:`required`" 
      :ref:`\<uncertainty\><siteDescription-overallQindex-uncertainty>`, double, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-overallqindex-value:

<value>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` overallQindex :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` value

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-overallqindex-uncertainty:

<uncertainty>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` overallQindex :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` uncertainty

   .. container:: type

			.. only:: latex

					content type: :ref:`double<type-glossary>`

			.. only:: html

					content type: `double <appendices.html#glossary-double>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment:

<comment>
------------------------------------------------------------
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment




   **Sub Elements of <comment>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<text\><siteDescription-comment-text>`, string, ":red:`required`" 
      :ref:`\<creationInfo\><siteDescription-comment-creationInfo>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-text:

<text>     :red:`required`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` text

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo:

<creationInfo>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo




   **Sub Elements of <creationInfo>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<author\><siteDescription-comment-creationInfo-author>`, , "optional" 
      :ref:`\<agency\><siteDescription-comment-creationInfo-agency>`, , "optional" 
      :ref:`\<creationTime\><siteDescription-comment-creationInfo-creationTime>`, dateTime, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-author:

<author>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author




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

      :ref:`\<firstname\><siteDescription-comment-creationInfo-author-firstname>`, string, ":red:`required`" 
      :ref:`\<lastname\><siteDescription-comment-creationInfo-author-lastname>`, string, ":red:`required`" 
      :ref:`\<mbox\><siteDescription-comment-creationInfo-author-mbox>`, string, ":red:`required`" 
      :ref:`\<homepage\><siteDescription-comment-creationInfo-author-homepage>`, anyURI, "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-author-firstname:

<firstname>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` firstname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-author-lastname:

<lastname>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` lastname

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-author-mbox:

<mbox>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-author-homepage:

<homepage>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` author :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency:

<agency>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency




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

      :ref:`\<name\><siteDescription-comment-creationInfo-agency-name>`, string, ":red:`required`" 
      :ref:`\<mbox\><siteDescription-comment-creationInfo-agency-mbox>`, string, "optional" 
      :ref:`\<phone\><siteDescription-comment-creationInfo-agency-phone>`, string, "optional" 
      :ref:`\<homepage\><siteDescription-comment-creationInfo-agency-homepage>`, anyURI, "optional" 
      :ref:`\<postalAddress\><siteDescription-comment-creationInfo-agency-postalAddress>`, , "optional" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-name:

<name>     :red:`required`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` name

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-mbox:

<mbox>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` mbox

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-phone:

<phone>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` phone

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-homepage:

<homepage>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` homepage

   .. container:: type

			.. only:: latex

					content type: :ref:`anyURI<type-glossary>`

			.. only:: html

					content type: `anyURI <appendices.html#glossary-anyuri>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-postaladdress:

<postalAddress>
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress




   **Sub Elements of <postalAddress>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<streetAddress\><siteDescription-comment-creationInfo-agency-postalAddress-streetAddress>`, string, ":red:`required`" 
      :ref:`\<locality\><siteDescription-comment-creationInfo-agency-postalAddress-locality>`, string, ":red:`required`" 
      :ref:`\<postalCode\><siteDescription-comment-creationInfo-agency-postalAddress-postalCode>`, string, ":red:`required`" 
      :ref:`\<country\><siteDescription-comment-creationInfo-agency-postalAddress-country>`, , ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-postaladdress-streetaddress:

<streetAddress>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` streetAddress

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-postaladdress-locality:

<locality>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` locality

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-postaladdress-postalcode:

<postalCode>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalCode

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-postaladdress-country:

<country>     :red:`required`
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country




   **Sub Elements of <country>**: 

   .. tabularcolumns::|l|l|l|l| 

   .. csv-table::
      :class: rows
      :escape: \ 
      :header: "element", "type", "number"
      :widths: auto

      :ref:`\<code\><siteDescription-comment-creationInfo-agency-postalAddress-country-code>`, string, ":red:`required`" 
      :ref:`\<country\><siteDescription-comment-creationInfo-agency-postalAddress-country-country>`, string, ":red:`required`" 




:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-postaladdress-country-code:

<code>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` code

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-agency-postaladdress-country-country:

<country>     :red:`required`
************************************************************
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` agency :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` postalAddress :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` country

   .. container:: type

			.. only:: latex

					content type: :ref:`string<type-glossary>`

			.. only:: html

					content type: `string <appendices.html#glossary-string>`_


:raw-latex:`\noindent\rule{\textwidth}{1pt}`

.. _sitedescription-comment-creationinfo-creationtime:

<creationTime>     :red:`required`
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
.. container:: hatnote hatnote-gray

   .. container:: crumb

      siteDescription :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` comment :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationInfo :raw-html:`&rarr;`:raw-latex:`$\rightarrow$` creationTime

   .. container:: type

			.. only:: latex

					content type: :ref:`dateTime<type-glossary>`

			.. only:: html

					content type: `dateTime <appendices.html#glossary-datetime>`_

