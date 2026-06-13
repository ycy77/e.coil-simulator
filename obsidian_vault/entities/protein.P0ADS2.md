---
entity_id: "protein.P0ADS2"
entity_type: "protein"
name: "zapA"
source_database: "UniProt"
source_id: "P0ADS2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12368265}. Note=Localizes at mid-cell."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zapA ygfE b2910 JW2878"
---

# zapA

`protein.P0ADS2`

## Static

- Type: `protein`
- Source: `UniProt:P0ADS2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12368265}. Note=Localizes at mid-cell.

## Enriched Summary

FUNCTION: Activator of cell division through the inhibition of FtsZ GTPase activity, therefore promoting FtsZ assembly into bundles of protofilaments necessary for the formation of the division Z ring. It is recruited early at mid-cell but it is not essential for cell division. {ECO:0000269|PubMed:15060045}. ZapA binds to FtsZ polymers and promotes the coherence of the Z-ring by cross-linking FtsZ polymers and stabilizing longitudinal interactions between FtsZ molecules . This effect is counteracted by ZapB . In the absence of functional Min and nucleoid exclusion (SlmA) systems, the MatP-ZapB-ZapA system positions the Z ring over the nucleoid in mid-cell . The protein network formed by the divisome proteins FtsZ, ZapA, ZapB and MatP has been studied using superresolution imaging, showing that these proteins form a multi-layered protein network that extends from the cell membrane to the chromosome and that stabilizes the FtsZ ring . The ZapA and ZapB proteins are able to form an FtsZ-independent structure at midcell which appears to provide positional information to FtsZ . Localization of the chromosomal Ter region at the divisome is dependent on the MatP-ZapB-ZapA system . Before septum formation, a complex of the early-division proteins ZipA, ZapA, and ZapB oscillates along the cell with a periodicity that is opposite that of MinC...

## Biological Role

Component of cell division protein ZapA (complex.ecocyc.CPLX0-7538).

## Annotation

FUNCTION: Activator of cell division through the inhibition of FtsZ GTPase activity, therefore promoting FtsZ assembly into bundles of protofilaments necessary for the formation of the division Z ring. It is recruited early at mid-cell but it is not essential for cell division. {ECO:0000269|PubMed:15060045}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7538|complex.ecocyc.CPLX0-7538]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2910|gene.b2910]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADS2`
- `KEGG:ecj:JW2878;eco:b2910;ecoc:C3026_15950;`
- `GeneID:86860993;93779091;947404;`
- `GO:GO:0000917; GO:0000921; GO:0005829; GO:0005886; GO:0030428; GO:0032153; GO:0042802; GO:0043093; GO:0051301`

## Notes

Cell division protein ZapA (Z ring-associated protein ZapA)
