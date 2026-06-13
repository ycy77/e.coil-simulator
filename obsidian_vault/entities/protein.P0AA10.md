---
entity_id: "protein.P0AA10"
entity_type: "protein"
name: "rplM"
source_database: "UniProt"
source_id: "P0AA10"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplM b3231 JW3200"
---

# rplM

`protein.P0AA10`

## Static

- Type: `protein`
- Source: `UniProt:P0AA10`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is one of the early assembly proteins of the 50S ribosomal subunit, although it is not seen to bind rRNA by itself. It is important during the early stages of 50S assembly. {ECO:0000269|PubMed:3298242}. The L13 protein is an early assembly component of the 50S subunit of the ribosome . The RNA helicase EG10975-MONOMER SrmB was initially proposed to be necessary for the assembly of L13 into the ribosome . However, it was recently shown that SrmB positively regulates expression of L13 and S9 by preventing premature transcription termination; thus, the role of SrmB in ribosome assembly may be to ensure the synthesis of adequate levels of L13 and S9 . L13 interacts with 23S rRNA and crosslinks to it in both free ribosomes and the initiation complex . L13 is located within 21 Å of nucleotide C2475 of 23S rRNA, near the peptidyltransferase center . L13 binds to 5S rRNA and can be crosslinked to L2 , L3 , L20 and L21 . L13 interacts with tRNA in the P site . EG50004-MONOMER Ribosome modulation factor binds near L2, L13, and S13 . A puromycin analog , a tobramycin analog , and a pactamycin analog can be crosslinked to L13. L13 has RNA chaperone-like activity in an in vitro trans splicing assay and binds zinc . L13 was found to be phosphorylated . L13 inhibits translation of its own mRNA...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: This protein is one of the early assembly proteins of the 50S ribosomal subunit, although it is not seen to bind rRNA by itself. It is important during the early stages of 50S assembly. {ECO:0000269|PubMed:3298242}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3230|gene.b3230]] `RegulonDB` `S` - regulator=RplM; target=rpsI; function=-
- `represses` --> [[gene.b3231|gene.b3231]] `RegulonDB` `S` - regulator=RplM; target=rplM; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3231|gene.b3231]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA10`
- `KEGG:ecj:JW3200;eco:b3231;ecoc:C3026_17580;`
- `GeneID:89518067;947828;`
- `GO:GO:0002181; GO:0003729; GO:0003735; GO:0005737; GO:0005829; GO:0005840; GO:0008270; GO:0017148; GO:0022625; GO:0048027; GO:0070180`

## Notes

Large ribosomal subunit protein uL13 (50S ribosomal protein L13)
