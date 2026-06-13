---
entity_id: "protein.P0AF36"
entity_type: "protein"
name: "zapB"
source_database: "UniProt"
source_id: "P0AF36"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:18394147}. Note=Localizes to the septum at mid-cell, in a FtsZ-like pattern."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zapB yiiU b3928 JW3899"
---

# zapB

`protein.P0AF36`

## Static

- Type: `protein`
- Source: `UniProt:P0AF36`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:18394147}. Note=Localizes to the septum at mid-cell, in a FtsZ-like pattern.

## Enriched Summary

FUNCTION: Non-essential, abundant cell division factor that is required for proper Z-ring formation. It is recruited early to the divisome by direct interaction with FtsZ, stimulating Z-ring assembly and thereby promoting cell division earlier in the cell cycle. Its recruitment to the Z-ring requires functional FtsA or ZipA. {ECO:0000269|PubMed:18394147}. The ZapB protein is a cell division factor that is required for proper Z ring formation and is recruited to the inner face of the Z ring by ZapA . The N terminus of ZapB is required for its interaction with ZapA . ZapB interacts with EG12855-MONOMER MatP, thereby anchoring the Ter macrodomain in mid-cell . In the absence of functional Min and nucleoid exclusion (SlmA) systems, the MatP-ZapB-ZapA system positions the Z ring over the nucleoid in mid-cell . The protein network formed by the divisome proteins FtsZ, ZapA, ZapB and MatP has been studied using superresolution imaging, showing that these proteins form a multi-layered protein network that extends from the cell membrane to the chromosome and that stabilizes the FtsZ ring . The ZapA and ZapB proteins are able to form an FtsZ-independent structure at midcell which appears to provide positional information to FtsZ; ZapB appears to be recruited to midcell by MatP...

## Biological Role

Component of cell division factor ZapB (complex.ecocyc.CPLX0-7686).

## Annotation

FUNCTION: Non-essential, abundant cell division factor that is required for proper Z-ring formation. It is recruited early to the divisome by direct interaction with FtsZ, stimulating Z-ring assembly and thereby promoting cell division earlier in the cell cycle. Its recruitment to the Z-ring requires functional FtsA or ZipA. {ECO:0000269|PubMed:18394147}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7686|complex.ecocyc.CPLX0-7686]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3928|gene.b3928]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF36`
- `KEGG:ecj:JW3899;eco:b3928;`
- `GeneID:86861678;93777970;948420;`
- `GO:GO:0000917; GO:0005829; GO:0032153; GO:0042802; GO:0043093`

## Notes

Cell division protein ZapB
