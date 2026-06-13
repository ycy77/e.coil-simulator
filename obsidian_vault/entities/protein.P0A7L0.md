---
entity_id: "protein.P0A7L0"
entity_type: "protein"
name: "rplA"
source_database: "UniProt"
source_id: "P0A7L0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplA b3984 JW3947"
---

# rplA

`protein.P0A7L0`

## Static

- Type: `protein`
- Source: `UniProt:P0A7L0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of the primary rRNA binding proteins, it binds very close to the 3'-end of the 23S rRNA. Forms part of the L1 stalk. It is often not seen in high-resolution crystal structures, but can be seen in cryo_EM and 3D reconstruction models. These indicate that the distal end of the stalk moves by approximately 20 angstroms (PubMed:12859903, PubMed:16272117). This stalk movement is thought to be coupled to movement of deacylated tRNA into and out of the E site, and thus to participate in tRNA translocation (PubMed:12859903, PubMed:16272117). Contacts the P and E site tRNAs. {ECO:0000269|PubMed:12859903, ECO:0000269|PubMed:16272117}.; FUNCTION: Protein L1 is also a translational repressor protein, it controls the translation of the L11 operon by binding to its mRNA. The L1 protein is a component of the 50S subunit of the ribosome and also functions in the post-transcriptional regulation of the ribosomal protein genes encoded in the L11 operon. Ribosomes lacking L1 show a lower translation activity than wild type and are defective in binding of aminoacylated tRNA . L1 has been identified within a 3-D map of the 70S ribosome constructed by cryo-electron microscopy . L1 interacts with a region in the 5' end of 23S rRNA . It also can be crosslinked to a region near the central fold of aminoacylated tRNA in the P and E site...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of the primary rRNA binding proteins, it binds very close to the 3'-end of the 23S rRNA. Forms part of the L1 stalk. It is often not seen in high-resolution crystal structures, but can be seen in cryo_EM and 3D reconstruction models. These indicate that the distal end of the stalk moves by approximately 20 angstroms (PubMed:12859903, PubMed:16272117). This stalk movement is thought to be coupled to movement of deacylated tRNA into and out of the E site, and thus to participate in tRNA translocation (PubMed:12859903, PubMed:16272117). Contacts the P and E site tRNAs. {ECO:0000269|PubMed:12859903, ECO:0000269|PubMed:16272117}.; FUNCTION: Protein L1 is also a translational repressor protein, it controls the translation of the L11 operon by binding to its mRNA.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3984|gene.b3984]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7L0`
- `KEGG:ecj:JW3947;eco:b3984;`
- `GeneID:93777910;948483;`
- `GO:GO:0000027; GO:0000049; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0019843; GO:0022625; GO:0045947`

## Notes

Large ribosomal subunit protein uL1 (50S ribosomal protein L1)
