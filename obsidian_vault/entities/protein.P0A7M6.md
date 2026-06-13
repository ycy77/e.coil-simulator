---
entity_id: "protein.P0A7M6"
entity_type: "protein"
name: "rpmC"
source_database: "UniProt"
source_id: "P0A7M6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpmC b3312 JW3274"
---

# rpmC

`protein.P0A7M6`

## Static

- Type: `protein`
- Source: `UniProt:P0A7M6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Binds 23S rRNA. It is not essential for growth. {ECO:0000269|PubMed:12226666, ECO:0000269|PubMed:6170935}.; FUNCTION: One of the proteins that surrounds the polypeptide exit tunnel on the outside of the subunit. Contacts trigger factor (PubMed:12226666). {ECO:0000269|PubMed:12226666}. The L29 protein is a component of the 50S subunit of the ribosome . L29 interacts with 23S rRNA and is photoaffinity labeled by puromycin, an analog of the 3' end of aminoacylated tRNA . L29 crosslinks to Trigger Factor (TF) and contacts the Signal Recognition Particle , but is not required for the association of TF with the ribosome . L29 together with ACP stimulates the binding of Tn7-encoded TnsD to attTn7, the insertion site for Tn7 in the E. coli chromosome. L23 also stimulates Tn7 transposition in vitro. A mutation in L29 decreases Tn7 transposition in vivo .

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Binds 23S rRNA. It is not essential for growth. {ECO:0000269|PubMed:12226666, ECO:0000269|PubMed:6170935}.; FUNCTION: One of the proteins that surrounds the polypeptide exit tunnel on the outside of the subunit. Contacts trigger factor (PubMed:12226666). {ECO:0000269|PubMed:12226666}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3312|gene.b3312]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7M6`
- `KEGG:ecj:JW3274;eco:b3312;ecoc:C3026_18000;`
- `GeneID:86862290;93778675;947807;`
- `GO:GO:0000027; GO:0002181; GO:0003735; GO:0005737; GO:0019843; GO:0022625`

## Notes

Large ribosomal subunit protein uL29 (50S ribosomal protein L29)
