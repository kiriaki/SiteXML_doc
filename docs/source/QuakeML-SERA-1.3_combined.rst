QuakeML-SERA 1.3 - Types and Elements
=====================================

.. note:: This file was auto-generated from the XSD. Sections use Sphinx domain markup.


.. contents:: Table of contents
   :local:


Global Elements
----------------

.. _SERA_quakeml:

SERA_quakeml
^^^^^^^^^^^^

.. class:: SERA_quakeml


Types
-----

.. _AffiliationType:

AffiliationType
---------------

.. class:: AffiliationType

Child elements
~~~~~~~~~~~~~~

.. attribute:: institution
   :type: :ref:`InstitutionType`

.. attribute:: department
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: function
   :type: ``string``
   :occurs: (min: 0, max: 1)


.. _AnalysisType:

AnalysisType
------------

.. class:: AnalysisType

Attributes
~~~~~~~~~~

.. attribute:: publicID
   :type: :ref:`ResourceIdentifier`

Child elements
~~~~~~~~~~~~~~

.. attribute:: siteDescriptionID
   :type: :ref:`ResourceIdentifier`

   The Site Description this Analysis object refers to.

.. attribute:: creationInfo
   :type: :ref:`CreationInfoType`
   :occurs: (min: 0, max: 1)

   Date that this analysis was generated. You may not include this information if you provide referencies for the individual site indicators.

.. attribute:: comment
   :type: :ref:`CommentType`
   :occurs: (min: 0, max: unbounded)

.. attribute:: resonanceFrequency
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: resonanceFrequencyQindex1
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: resonanceFrequencyMethod
   :type: :ref:`ResonanceFrequencyMethodType`
   :occurs: (min: 0, max: unbounded)

.. attribute:: resonanceFrequencyReference
   :type: :ref:`ReferenceType`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityS30
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityS30Qindex1
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityS30Method
   :type: :ref:`VelocityS30MethodType`
   :occurs: (min: 0, max: unbounded)

.. attribute:: velocityS30MethodCombIndex
   :type: :ref:`velocityS30MethodCombIndexType`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityS30ManualIndex
   :type: :ref:`velocityS30ManualIndexType`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityS30Reference
   :type: :ref:`ReferenceType`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityProfileCount
   :type: :ref:`CounterType`
   :occurs: (min: 0, max: 1)

.. attribute:: sptLogsCount
   :type: :ref:`CounterType`
   :occurs: (min: 0, max: 1)

.. attribute:: cptLogsCount
   :type: :ref:`CounterType`
   :occurs: (min: 0, max: 1)

.. attribute:: boreholeLogsCount
   :type: :ref:`CounterType`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityProfile
   :type: :ref:`VelocityProfile`
   :occurs: (min: 0, max: unbounded)

.. attribute:: velocityProfileQindex1
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityProfileReference
   :type: :ref:`ReferenceType`
   :occurs: (min: 0, max: 1)


.. _CommentType:

CommentType
-----------

.. class:: CommentType

Child elements
~~~~~~~~~~~~~~

.. attribute:: text
   :type: ``string``

.. attribute:: creationInfo
   :type: :ref:`CreationInfoType`
   :occurs: (min: 0, max: 1)


.. _ContactType:

ContactType
-----------

.. class:: ContactType

Child elements
~~~~~~~~~~~~~~

.. attribute:: person
   :type: :ref:`PersonType`

.. attribute:: affiliation
   :type: :ref:`AffiliationType`


.. _CounterType:

CounterType
-----------

.. class:: CounterType

   Integers greater than or equal to 0.


.. _CountryType:

CountryType
-----------

.. class:: CountryType

Child elements
~~~~~~~~~~~~~~

.. attribute:: code
   :type: ``string``

.. attribute:: country
   :type: ``string``


.. _CreationInfoType:

CreationInfoType
----------------

.. class:: CreationInfoType

Child elements
~~~~~~~~~~~~~~

.. attribute:: author
   :type: :ref:`PersonType`
   :occurs: (min: 0, max: 1)

.. attribute:: agency
   :type: :ref:`InstitutionType`
   :occurs: (min: 0, max: 1)

.. attribute:: creationTime
   :type: ``dateTime``


.. _EC8ClassType:

EC8ClassType
------------

.. class:: EC8ClassType

   Ground type according to Eurocode 8 (EC8 § 3.1.2, Table 3.1), based on the velocityS30Value and geotechnical description

   :Members:

   * ``A`` — 
   * ``B`` — 
   * ``C`` — 
   * ``D`` — 
   * ``E`` — 
   * ``S1`` — 
   * ``S2`` — 
   * ``Undefined`` — 


.. _ExternalReferenceType:

ExternalReferenceType
---------------------

.. class:: ExternalReferenceType

   This type contains a URI and description for external data that users may want to reference in SiteXML.

Child elements
~~~~~~~~~~~~~~

.. attribute:: URI
   :type: ``anyURI``

.. attribute:: Description
   :type: ``string``


.. _FileResourceType:

FileResourceType
----------------

.. class:: FileResourceType

Child elements
~~~~~~~~~~~~~~

.. attribute:: description
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: url
   :type: ``anyURI``
   :occurs: (min: 0, max: 1)


.. _InstitutionType:

InstitutionType
---------------

.. class:: InstitutionType

Attributes
~~~~~~~~~~

.. attribute:: publicID
   :type: :ref:`ResourceIdentifier`

Child elements
~~~~~~~~~~~~~~

.. attribute:: name
   :type: ``string``

.. attribute:: mbox
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: phone
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: homepage
   :type: ``anyURI``
   :occurs: (min: 0, max: 1)

.. attribute:: postalAddress
   :type: :ref:`PostalAddressType`
   :occurs: (min: 0, max: 1)


.. _IntegerQuantity:

IntegerQuantity
---------------

.. class:: IntegerQuantity

Child elements
~~~~~~~~~~~~~~

.. attribute:: value
   :type: ``int``

.. attribute:: uncertainty
   :type: ``int``
   :occurs: (min: 0, max: 1)


.. _LanguageType:

LanguageType
------------

.. class:: LanguageType

Child elements
~~~~~~~~~~~~~~

.. attribute:: code
   :type: ``string``


.. _LayerGeometry:

LayerGeometry
-------------

.. class:: LayerGeometry

Child elements
~~~~~~~~~~~~~~

.. attribute:: layerTopDepth
   :type: :ref:`RealQuantity`

.. attribute:: layerBottomDepth
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)


.. _LiteratureSourceType:

LiteratureSourceType
--------------------

.. class:: LiteratureSourceType

Child elements
~~~~~~~~~~~~~~

.. attribute:: title
   :type: ``string``

.. attribute:: firstAuthor
   :type: ``string``

.. attribute:: secondaryAuthors
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: year
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: booktitle
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: doi
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: language
   :type: :ref:`LanguageType`
   :occurs: (min: 0, max: 1)


.. _MorphologyType:

MorphologyType
--------------

.. class:: MorphologyType

   Qualitative description of the shape of the earth's surface

   :Members:

   * ``Plain`` — 
   * ``Valley - Basin`` — 
   * ``Slope`` — 
   * ``Ridge`` — 


.. _PersonType:

PersonType
----------

.. class:: PersonType

Attributes
~~~~~~~~~~

.. attribute:: publicID
   :type: :ref:`ResourceIdentifier`

Child elements
~~~~~~~~~~~~~~

.. attribute:: firstname
   :type: ``string``

.. attribute:: lastname
   :type: ``string``

.. attribute:: mbox
   :type: ``string``

.. attribute:: homepage
   :type: ``anyURI``
   :occurs: (min: 0, max: 1)


.. _PostalAddressType:

PostalAddressType
-----------------

.. class:: PostalAddressType

Child elements
~~~~~~~~~~~~~~

.. attribute:: streetAddress
   :type: ``string``

.. attribute:: locality
   :type: ``string``

.. attribute:: postalCode
   :type: ``string``

.. attribute:: country
   :type: :ref:`CountryType`


.. _RealQuantity:

RealQuantity
------------

.. class:: RealQuantity

Child elements
~~~~~~~~~~~~~~

.. attribute:: value
   :type: ``double``

.. attribute:: uncertainty
   :type: ``double``
   :occurs: (min: 0, max: 1)


.. _ReferenceType:

ReferenceType
-------------

.. class:: ReferenceType

Child elements
~~~~~~~~~~~~~~

.. attribute:: literatureSource
   :type: :ref:`LiteratureSourceType`
   :occurs: (min: 0, max: 1)

.. attribute:: fileResource
   :type: :ref:`FileResourceType`
   :occurs: (min: 0, max: 1)


.. _ResonanceFrequencyMethodType:

ResonanceFrequencyMethodType
----------------------------

.. class:: ResonanceFrequencyMethodType

   Method by which resonance frequency (dominant_frequency) has been determined. Used to determine the Quality Index of the provided f0 of a site. For more information, see SERA Deliverable 7.1, Appendix II.

   :Members:

   * ``HVSR EARTHQUAKE RECORDS`` — 
   * ``HVSR NOISE`` — 
   * ``SSR EARTHQUAKE RECORDS`` — 
   * ``SSR NOISE`` — 
   * ``INFERRED`` — 


.. _ResourceIdentifier:

ResourceIdentifier
------------------

.. class:: ResourceIdentifier


.. _SiteDescriptionType:

SiteDescriptionType
-------------------

.. class:: SiteDescriptionType

Attributes
~~~~~~~~~~

.. attribute:: publicID
   :type: :ref:`ResourceIdentifier`

Child elements
~~~~~~~~~~~~~~

.. attribute:: station
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: latitude
   :type: :ref:`RealQuantity`

.. attribute:: longitude
   :type: :ref:`RealQuantity`

.. attribute:: altitude
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: minDistanceFromStation
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: maxDistanceFromStation
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: siteTopography
   :type: :ref:`SiteTopographyType`
   :occurs: (min: 0, max: 1)

.. attribute:: siteMorphology
   :type: :ref:`SiteMorphologyType`
   :occurs: (min: 0, max: 1)

.. attribute:: preferredSiteAnalysisID
   :type: :ref:`ResourceIdentifier`

   It is mandatory to select one Site Analysis object as the preferred. The Overall Quality index of the Site Characterization will be calculated using the preferred analysis.

.. attribute:: preferredVelocityProfileID
   :type: :ref:`ResourceIdentifier`

.. attribute:: overallQindex
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: comment
   :type: :ref:`CommentType`
   :occurs: (min: 0, max: unbounded)


.. _SiteMorphologyType:

SiteMorphologyType
------------------

.. class:: SiteMorphologyType

   **Extends:** ``string``

Child elements
~~~~~~~~~~~~~~

.. attribute:: morphology
   :type: :ref:`MorphologyType`
   :occurs: (min: 0, max: 1)

   This in not included in the QuakeML 2.0 draft

.. attribute:: siteClassEC8
   :type: :ref:`EC8ClassType`
   :occurs: (min: 0, max: 1)

.. attribute:: siteClassEC8Qindex1
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: siteClassEC8Reference
   :type: :ref:`ReferenceType`
   :occurs: (min: 0, max: 1)

.. attribute:: bedrockDepth
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: bedrockDepthQindex1
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: bedrockDepthReference
   :type: :ref:`ReferenceType`
   :occurs: (min: 0, max: 1)

.. attribute:: h800
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

   This is not included in the QuakeML 2.0 draft

.. attribute:: h800Qindex1
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: h800Reference
   :type: :ref:`ReferenceType`
   :occurs: (min: 0, max: 1)

.. attribute:: geologicalUnit
   :occurs: (min: 0, max: 1)

.. attribute:: geologicalUnitQindex1
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: geologicalMapScale
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: geologicalUnitOGE
   :type: ``string``
   :occurs: (min: 0, max: 1)

.. attribute:: geologicalUnitReference
   :type: :ref:`ReferenceType`
   :occurs: (min: 0, max: 1)


.. _SiteOwnerType:

SiteOwnerType
-------------

.. class:: SiteOwnerType

Attributes
~~~~~~~~~~

.. attribute:: publicID
   :type: :ref:`ResourceIdentifier`

Child elements
~~~~~~~~~~~~~~

.. attribute:: codeName
   :type: ``string``

.. attribute:: fullName
   :type: ``string``

.. attribute:: contact
   :type: :ref:`ContactType`


.. _SiteTopographyType:

SiteTopographyType
------------------

.. class:: SiteTopographyType

Child elements
~~~~~~~~~~~~~~

.. attribute:: schemaA
   :type: :ref:`TopographySchemaAType`

   This is not included in 2.0

.. attribute:: schemaB
   :type: :ref:`TopographySchemaBType`


.. _TopographySchemaAType:

TopographySchemaAType
---------------------

.. class:: TopographySchemaAType

   Topography is a precise (quantitative) description of the ground surface features of a site. Schema A is the topography description schema of the Italian Code. T1 : Flat surface, isolated slopes and cliffs with average slop angle T2 : Slopes with average slope angle i>15 T3 : Ridges with crest width significantly less than the base width and average slope angle 15 T4 : Ridges with crest width significantly less than the base width and average slope angle i>30

   :Members:

   * ``T1`` — 
   * ``T2`` — 
   * ``T3`` — 
   * ``T4`` — 


.. _TopographySchemaBType:

TopographySchemaBType
---------------------

.. class:: TopographySchemaBType

   Topography is a precise (quantitative) description of the ground surface features of a site. Schema B is the one proposed by Burjanek et al. (2014). For the precise definition of the allowed values refer to SERA Deliverable D7.1.

   :Members:

   * ``Valley`` — 
   * ``Lower slope`` — 
   * ``Flat`` — 
   * ``Middle slope`` — 
   * ``Upper slope`` — 
   * ``Ridge`` — 


.. _VelocityProfile:

VelocityProfile
---------------

.. class:: VelocityProfile

Attributes
~~~~~~~~~~

.. attribute:: publicID
   :type: :ref:`ResourceIdentifier`

Child elements
~~~~~~~~~~~~~~

.. attribute:: layerCount
   :type: :ref:`CounterType`

.. attribute:: velocityProfileData
   :type: :ref:`VelocityProfileData`
   :occurs: (min: 1, max: unbounded)


.. _VelocityProfileData:

VelocityProfileData
-------------------

.. class:: VelocityProfileData

Child elements
~~~~~~~~~~~~~~

.. attribute:: velocityP
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: velocityS
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: density
   :type: :ref:`RealQuantity`
   :occurs: (min: 0, max: 1)

.. attribute:: layerThickness
   :type: :ref:`LayerGeometry`
   :occurs: (min: 1, max: 1)


.. _VelocityS30MethodType:

VelocityS30MethodType
---------------------

.. class:: VelocityS30MethodType

   Method used for the extraction of S-wave velocity profiles and, thus, of the average shear-wave velocity over the top 30 meters of the soil column, Vs30. Used to determine the Quality Index of the provided Vs30 of a site. For more information, see SERA Deliverable 7.1, Appendix IV.

   :Members:

   * ``Geology`` — 
   * ``Topographic Slope`` — 
   * ``SPT`` — 
   * ``CPT`` — 
   * ``Laboratory`` — 
   * ``S-REFR`` — 
   * ``S-REFL`` — 
   * ``SASW`` — 
   * ``MASW`` — 
   * ``SWI`` — 
   * ``SPAC/F-K`` — 
   * ``ReMi`` — 
   * ``Crosshole`` — 
   * ``Downhole`` — 
   * ``Uphole`` — 
   * ``P-S Log`` — 
   * ``Seismic Cone`` — 
   * ``DH Strong Motion Arrays`` — 


.. _velocityS30ManualIndexType:

velocityS30ManualIndexType
--------------------------

.. class:: velocityS30ManualIndexType

   Overall qualitative factor on the knowledge of the maximum depth of Vs measurements, which is most commonly related to the depth the EC8 engineering bedrock (Vs≥800 m/s). The reasoning for introducing this index and description of its values is provided in SERA Deliverable 7.1, Appendix III.

   :Members:

   * ``0.2`` — 
   * ``0.4`` — 
   * ``0.8`` — 
   * ``1.0`` — 


.. _velocityS30MethodCombIndexType:

velocityS30MethodCombIndexType
------------------------------

.. class:: velocityS30MethodCombIndexType

   Carries the information on whether a combination of two methods or more has been applied to estimate the Vs30 value. It is used for the estimation of the Vs30 quality index. Allowed values: 1.0 : if only one method has been used to estimate the Vs30 value 1.2 : if a combination of two or more methods has been applied to estimate the Vs30 value

   :Members:

   * ``1.0`` — 
   * ``1.2`` — 


Reference labels
----------------

The following labels are available for :ref: references:

* :ref:`AffiliationType` -> AffiliationType
* :ref:`AnalysisType` -> AnalysisType
* :ref:`CommentType` -> CommentType
* :ref:`ContactType` -> ContactType
* :ref:`CounterType` -> CounterType
* :ref:`CountryType` -> CountryType
* :ref:`CreationInfoType` -> CreationInfoType
* :ref:`EC8ClassType` -> EC8ClassType
* :ref:`ExternalReferenceType` -> ExternalReferenceType
* :ref:`FileResourceType` -> FileResourceType
* :ref:`InstitutionType` -> InstitutionType
* :ref:`IntegerQuantity` -> IntegerQuantity
* :ref:`LanguageType` -> LanguageType
* :ref:`LayerGeometry` -> LayerGeometry
* :ref:`LiteratureSourceType` -> LiteratureSourceType
* :ref:`MorphologyType` -> MorphologyType
* :ref:`PersonType` -> PersonType
* :ref:`PostalAddressType` -> PostalAddressType
* :ref:`RealQuantity` -> RealQuantity
* :ref:`ReferenceType` -> ReferenceType
* :ref:`ResonanceFrequencyMethodType` -> ResonanceFrequencyMethodType
* :ref:`ResourceIdentifier` -> ResourceIdentifier
* :ref:`SiteDescriptionType` -> SiteDescriptionType
* :ref:`SiteMorphologyType` -> SiteMorphologyType
* :ref:`SiteOwnerType` -> SiteOwnerType
* :ref:`SiteTopographyType` -> SiteTopographyType
* :ref:`TopographySchemaAType` -> TopographySchemaAType
* :ref:`TopographySchemaBType` -> TopographySchemaBType
* :ref:`VelocityProfile` -> VelocityProfile
* :ref:`VelocityProfileData` -> VelocityProfileData
* :ref:`VelocityS30MethodType` -> VelocityS30MethodType
* :ref:`velocityS30ManualIndexType` -> velocityS30ManualIndexType
* :ref:`velocityS30MethodCombIndexType` -> velocityS30MethodCombIndexType
