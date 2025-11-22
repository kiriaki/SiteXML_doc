SiteDescriptionType
===================

**Type:** ``complexType``
**Description:**
  *No documentation*

Attributes
----------

* **publicID** (``ResourceIdentifier``) – 
Child Elements
--------------

* **station** (``xs:string``) – * **latitude** (``RealQuantity``) – * **longitude** (``RealQuantity``) – * **altitude** (``RealQuantity``) – * **minDistanceFromStation** (``RealQuantity``) – * **maxDistanceFromStation** (``RealQuantity``) – * **siteTopography** (``SiteTopographyType``) – * **siteMorphology** (``SiteMorphologyType``) – * **preferredSiteAnalysisID** (``ResourceIdentifier``) – It is mandatory to select one Site Analysis object as the preferred.
					The Overall Quality index of the Site Characterization will be calculated using the preferred analysis.* **preferredVelocityProfileID** (``ResourceIdentifier``) – * **overallQindex** (``RealQuantity``) – * **comment** (``CommentType``) – 
