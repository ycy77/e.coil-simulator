---
entity_id: "protein.P0A7U7"
entity_type: "protein"
name: "rpsT"
source_database: "UniProt"
source_id: "P0A7U7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsT b0023 JW0022"
---

# rpsT

`protein.P0A7U7`

## Static

- Type: `protein`
- Source: `UniProt:P0A7U7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Binds directly to 16S ribosomal RNA. The S20 protein is a component of the 30S subunit of the ribosome and appears to be involved in translation initiation and the association of the 30S and 50S subunits . S20 was also identified as antizyme 1, an inhibitor of the biosynthetic ornithine and arginine decarboxylases; these enzymes are involved in the biosynthesis of polyamine . S20 is identical to L26. The synthesis of S20 is regulated at the post-transcriptional level ; in an in vitro system, S20 represses its own synthesis . However, S20 doesn't show affinity for its own mRNA . The UUG initiation codon appears to be important for regulation . Processing and degradation of rpsT mRNA have been studied extensively; see for example and references therein. rpsT mRNA stability and translational efficiency are linked . S20 physically interacts with ornithine and arginine decarboxylase, and overexpression of S20 decreases the production of polyamine in vivo . Levels of S20 increase in response to polyamines; the effect is thought to be due to an increase in the level of transcription of rpsT . S20 binds to the 5' domain and the 3' minor domain of 16S rRNA . C-terminal residues of S20 are required for binding to 16S rRNA . Hydroxyl radical footprinting provided evidence that S20 is located near the bottom of the 30S subunit...

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Binds directly to 16S ribosomal RNA.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b0023|gene.b0023]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7U7`
- `KEGG:ecj:JW0022;eco:b0023;ecoc:C3026_00110;`
- `GeneID:86862535;93777413;944759;`
- `GO:GO:0000028; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0008073; GO:0015935; GO:0022627; GO:0070181`

## Notes

Small ribosomal subunit protein bS20 (30S ribosomal protein S20)
