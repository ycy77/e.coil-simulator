---
entity_id: "protein.P0AG48"
entity_type: "protein"
name: "rplU"
source_database: "UniProt"
source_id: "P0AG48"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplU b3186 JW3153"
---

# rplU

`protein.P0AG48`

## Static

- Type: `protein`
- Source: `UniProt:P0AG48`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein binds to 23S rRNA in the presence of protein L20. {ECO:0000269|PubMed:2665813, ECO:0000269|PubMed:6170935}. The L21 protein is a component of the 50S subunit of the ribosome. L21 interacts with 23S rRNA . L4, L5, and L21 bind to erythromycin cooperatively . The rplU gene is expressed from an operon along with rpmA, yhbE, and obgE under control of the rplU promoter. This operon is mainly expressed during exponential growth and is probably indirectly regulated by ppGpp/DksA .

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: This protein binds to 23S rRNA in the presence of protein L20. {ECO:0000269|PubMed:2665813, ECO:0000269|PubMed:6170935}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3186|gene.b3186]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG48`
- `KEGG:ecj:JW3153;eco:b3186;ecoc:C3026_17345;`
- `GeneID:86862417;93778795;949057;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0019843; GO:0022625`

## Notes

Large ribosomal subunit protein bL21 (50S ribosomal protein L21)
