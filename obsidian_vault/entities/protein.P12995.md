---
entity_id: "protein.P12995"
entity_type: "protein"
name: "bioA"
source_database: "UniProt"
source_id: "P12995"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bioA b0774 JW0757"
---

# bioA

`protein.P12995`

## Static

- Type: `protein`
- Source: `UniProt:P12995`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of the alpha-amino group from S-adenosyl-L-methionine (SAM) to 7-keto-8-aminopelargonic acid (KAPA) to form 7,8-diaminopelargonic acid (DAPA) (PubMed:1092681, PubMed:1092682). It is the only animotransferase known to utilize SAM as an amino donor (PubMed:1092681, PubMed:1092682). Complements a bioU deletion in Synechocystis PCC 6803 (PubMed:32042199). {ECO:0000269|PubMed:1092681, ECO:0000269|PubMed:1092682, ECO:0000269|PubMed:32042199}.

## Biological Role

Component of adenosylmethionine-8-amino-7-oxononanoate aminotransferase (complex.ecocyc.DAPASYN-CPLX).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of the alpha-amino group from S-adenosyl-L-methionine (SAM) to 7-keto-8-aminopelargonic acid (KAPA) to form 7,8-diaminopelargonic acid (DAPA) (PubMed:1092681, PubMed:1092682). It is the only animotransferase known to utilize SAM as an amino donor (PubMed:1092681, PubMed:1092682). Complements a bioU deletion in Synechocystis PCC 6803 (PubMed:32042199). {ECO:0000269|PubMed:1092681, ECO:0000269|PubMed:1092682, ECO:0000269|PubMed:32042199}.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DAPASYN-CPLX|complex.ecocyc.DAPASYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0774|gene.b0774]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12995`
- `KEGG:ecj:JW0757;eco:b0774;`
- `GeneID:93776656;945376;`
- `GO:GO:0004015; GO:0005737; GO:0009102; GO:0030170; GO:0042803`
- `EC:2.6.1.62`

## Notes

Adenosylmethionine-8-amino-7-oxononanoate aminotransferase (EC 2.6.1.62) (7,8-diamino-pelargonic acid aminotransferase) (DAPA AT) (DAPA aminotransferase) (7,8-diaminononanoate synthase) (DANS) (Diaminopelargonic acid synthase)
