---
entity_id: "protein.P0A6J5"
entity_type: "protein"
name: "dadA"
source_database: "UniProt"
source_id: "P0A6J5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:13292, ECO:0000269|PubMed:15358424}; Peripheral membrane protein {ECO:0000269|PubMed:13292, ECO:0000269|PubMed:15358424}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dadA dadR b1189 JW1178"
---

# dadA

`protein.P0A6J5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6J5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:13292, ECO:0000269|PubMed:15358424}; Peripheral membrane protein {ECO:0000269|PubMed:13292, ECO:0000269|PubMed:15358424}.

## Enriched Summary

FUNCTION: Catalyzes the oxidative deamination of D-amino acids. Has broad substrate specificity; is mostly active on D-alanine, and to a lesser extent, on several other D-amino acids such as D-methionine, D-serine and D-proline, but not on L-alanine. Participates in the utilization of L-alanine and D-alanine as the sole source of carbon, nitrogen and energy for growth. Is also able to oxidize D-amino acid analogs such as 3,4-dehydro-D-proline, D-2-aminobutyrate, D-norvaline, D-norleucine, cis-4-hydroxy-D-proline, and DL-ethionine. {ECO:0000269|PubMed:13292, ECO:0000269|PubMed:15358424}.

## Biological Role

Component of D-amino acid dehydrogenase (complex.ecocyc.DALADEHYDROG-CPLX).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidative deamination of D-amino acids. Has broad substrate specificity; is mostly active on D-alanine, and to a lesser extent, on several other D-amino acids such as D-methionine, D-serine and D-proline, but not on L-alanine. Participates in the utilization of L-alanine and D-alanine as the sole source of carbon, nitrogen and energy for growth. Is also able to oxidize D-amino acid analogs such as 3,4-dehydro-D-proline, D-2-aminobutyrate, D-norvaline, D-norleucine, cis-4-hydroxy-D-proline, and DL-ethionine. {ECO:0000269|PubMed:13292, ECO:0000269|PubMed:15358424}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DALADEHYDROG-CPLX|complex.ecocyc.DALADEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1189|gene.b1189]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6J5`
- `KEGG:ecj:JW1178;eco:b1189;ecoc:C3026_07000;`
- `GeneID:93776243;945752;`
- `GO:GO:0005737; GO:0005886; GO:0008718; GO:0019480; GO:0042803; GO:0055130`
- `EC:1.4.99.-`

## Notes

D-amino acid dehydrogenase (EC 1.4.99.-) (D-alanine dehydrogenase)
