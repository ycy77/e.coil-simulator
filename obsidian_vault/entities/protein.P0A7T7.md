---
entity_id: "protein.P0A7T7"
entity_type: "protein"
name: "rpsR"
source_database: "UniProt"
source_id: "P0A7T7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsR b4202 JW4160"
---

# rpsR

`protein.P0A7T7`

## Static

- Type: `protein`
- Source: `UniProt:P0A7T7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Binds as a heterodimer with protein bS6 to the central domain of the 16S rRNA, where it helps stabilize the platform of the 30S subunit. The S18 protein is a component of the 30S subunit of the ribosome. The N-terminal alanine residue of S18 is acetylated by the EG10850-MONOMER RimI enzyme . N-terminal acetylation of S18 and S5 correlates with correct folding of the platform and central pseudoknot domains of 16S rRNA . S18 interacts with the central domain of 16S rRNA; the interaction is dependent on S8 and S15 . S18 may be involved in binding of aminoacyl-tRNA to the P site of the ribosome . S18 is photoaffinity labeled by puromycin, an analog of the 3' end of aminoacylated tRNA . S18 was also shown to crosslink to IF3 , IF1 and 4.5S RNA . Expression analysis of rpsFp indicates that it may be autoregulated by one or more of its operon components . Coexpressed S6:S18 were found to bind to the rpsF 5'-UTR in a region with structural similarity to their binding site in 16S rRNA . The S6:S18 complex was shown to repress translation of rpsF . Review:

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953), S6:S18 ribosomal subunit complex (complex.ecocyc.CPLX0-8208).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Binds as a heterodimer with protein bS6 to the central domain of the 16S rRNA, where it helps stabilize the platform of the 30S subunit.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8208|complex.ecocyc.CPLX0-8208]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4202|gene.b4202]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7T7`
- `KEGG:ecj:JW4160;eco:b4202;`
- `GeneID:948721;99704136;99808816;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0006412; GO:0022627; GO:0048027; GO:0070181`

## Notes

Small ribosomal subunit protein bS18 (30S ribosomal protein S18)
