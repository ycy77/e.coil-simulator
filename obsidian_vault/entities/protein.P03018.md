---
entity_id: "protein.P03018"
entity_type: "protein"
name: "uvrD"
source_database: "UniProt"
source_id: "P03018"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uvrD mutU pdeB rad recL b3813 JW3786"
---

# uvrD

`protein.P03018`

## Static

- Type: `protein`
- Source: `UniProt:P03018`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A helicase with DNA-dependent ATPase activity (PubMed:6319401, PubMed:8419285). Unwinds DNA duplexes with 3'-5' polarity (PubMed:2170128, PubMed:8419285). Translocates on single-stranded DNA with 3'-5' polarity (PubMed:2942537). Initiates unwinding more efficiently from a nicked substrate than double-stranded DNA (PubMed:2170128, PubMed:8419285). Involved in the post-incision events of nucleotide excision repair and methyl-directed mismatch repair, and probably also in repair of alkylated DNA (Probable) (PubMed:25484163). {ECO:0000269|PubMed:2170128, ECO:0000269|PubMed:2942537, ECO:0000269|PubMed:8419285, ECO:0000305|PubMed:25484163}.

## Biological Role

Component of DNA helicase II (complex.ecocyc.CPLX0-8111).

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: A helicase with DNA-dependent ATPase activity (PubMed:6319401, PubMed:8419285). Unwinds DNA duplexes with 3'-5' polarity (PubMed:2170128, PubMed:8419285). Translocates on single-stranded DNA with 3'-5' polarity (PubMed:2942537). Initiates unwinding more efficiently from a nicked substrate than double-stranded DNA (PubMed:2170128, PubMed:8419285). Involved in the post-incision events of nucleotide excision repair and methyl-directed mismatch repair, and probably also in repair of alkylated DNA (Probable) (PubMed:25484163). {ECO:0000269|PubMed:2170128, ECO:0000269|PubMed:2942537, ECO:0000269|PubMed:8419285, ECO:0000305|PubMed:25484163}.

## Pathways

- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8111|complex.ecocyc.CPLX0-8111]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3813|gene.b3813]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03018`
- `KEGG:ecj:JW3786;eco:b3813;ecoc:C3026_20640;`
- `GeneID:75204806;948347;`
- `GO:GO:0000725; GO:0003677; GO:0003678; GO:0005524; GO:0005829; GO:0006289; GO:0006298; GO:0009314; GO:0009432; GO:0015616; GO:0016887; GO:0017116; GO:0017117; GO:0031297; GO:0033202; GO:0042803; GO:0043138; GO:0070581; GO:0070716`
- `EC:5.6.2.4`

## Notes

DNA helicase II (EC 5.6.2.4) (DNA 3'-5' helicase II)
