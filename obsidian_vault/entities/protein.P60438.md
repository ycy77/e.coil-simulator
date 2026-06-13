---
entity_id: "protein.P60438"
entity_type: "protein"
name: "rplC"
source_database: "UniProt"
source_id: "P60438"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplC b3320 JW3282"
---

# rplC

`protein.P60438`

## Static

- Type: `protein`
- Source: `UniProt:P60438`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of two assembly initiator proteins, it binds directly near the 3'-end of the 23S rRNA, where it nucleates assembly of the 50S subunit. {ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:6760192}. The L3 protein is a component of the 50S subunit of the ribosome. L3 and L24 are the two proteins that initiate assembly of the 50S subunit . The L3 protein is methylated at the glutamine residue in position 150 . A prmB mutant which lacks methylation of L3 has a cold-sensitive growth phenotype and accumulates abnormal ribosomal particles; however, lack of L3 methylation does not appear to affect ribosome function once the ribosome is assembled . L3 interacts with 23S rRNA ; this interaction appears to be cooperative with L6 . An L3 mutant strain is resistant to the antibiotics tiamulin (a peptidyl transferase inhibitor) and pleuromutilin, but not valnemulin . An amber mutation in rplC exerts a polar effect on the genes distal to the rplC gene in the S10 operon .

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of two assembly initiator proteins, it binds directly near the 3'-end of the 23S rRNA, where it nucleates assembly of the 50S subunit. {ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:6760192}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3320|gene.b3320]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60438`
- `KEGG:ecj:JW3282;eco:b3320;ecoc:C3026_18040;`
- `GeneID:86862282;86948184;947817;`
- `GO:GO:0000027; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0019843; GO:0022625`

## Notes

Large ribosomal subunit protein uL3 (50S ribosomal protein L3)
