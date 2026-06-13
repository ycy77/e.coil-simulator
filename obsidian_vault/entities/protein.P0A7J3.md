---
entity_id: "protein.P0A7J3"
entity_type: "protein"
name: "rplJ"
source_database: "UniProt"
source_id: "P0A7J3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplJ b3985 JW3948"
---

# rplJ

`protein.P0A7J3`

## Static

- Type: `protein`
- Source: `UniProt:P0A7J3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Forms part of the ribosomal stalk, playing a central role in the interaction of the ribosome with GTP-bound translation factors. {ECO:0000269|PubMed:15923259}.; FUNCTION: Protein L10 is also a translational repressor protein. It controls the translation of the rplJL-rpoBC operon by binding to its mRNA. {ECO:0000269|PubMed:2448482}. The L10 protein is a component of the 50S subunit of the ribosome and also regulates the expression of the L10 (β) operon at the posttranscriptional level. L10 forms a complex with L7/L12; this complex was originally identified as the L8 subunit . L10 and L7/L12 bind to the 23S rRNA early during assembly of the 50S subunit . Binding of L10 to 23S rRNA can be separated from binding to L7/L12 ; two binding sites in the C terminus of L10 are required for the binding of two L7/L12 dimers, but not for assembly of L10 into the ribosome . Synthesis of L10 and L7/L12 is regulated at the level of translation initiation . Expression of L12 is closely linked to expression of L10 , and a region within the leader sequence of the L10 operon mRNA regulates the translation efficiency of L10 and L7/L12 . The L10 protein acts at a single site in the leader mRNA...

## Biological Role

Component of 50S ribosomal protein complex L8 (complex.ecocyc.CPLX0-3956).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Forms part of the ribosomal stalk, playing a central role in the interaction of the ribosome with GTP-bound translation factors. {ECO:0000269|PubMed:15923259}.; FUNCTION: Protein L10 is also a translational repressor protein. It controls the translation of the rplJL-rpoBC operon by binding to its mRNA. {ECO:0000269|PubMed:2448482}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3956|complex.ecocyc.CPLX0-3956]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3985|gene.b3985]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7J3`
- `KEGG:ecj:JW3948;eco:b3985;ecoc:C3026_21525;`
- `GeneID:86861614;93777909;948490;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0006412; GO:0015934; GO:0017148; GO:0022625; GO:0043022; GO:0070180`

## Notes

Large ribosomal subunit protein uL10 (50S ribosomal protein L10) (50S ribosomal protein L8)
