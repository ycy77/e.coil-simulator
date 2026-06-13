---
entity_id: "protein.P0ACB4"
entity_type: "protein"
name: "hemG"
source_database: "UniProt"
source_id: "P0ACB4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00853, ECO:0000305|PubMed:20484676}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_00853, ECO:0000305|PubMed:20484676}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemG yihB b3850 JW3827"
---

# hemG

`protein.P0ACB4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACB4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00853, ECO:0000305|PubMed:20484676}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_00853, ECO:0000305|PubMed:20484676}.

## Enriched Summary

FUNCTION: Catalyzes the 6-electron oxidation of protoporphyrinogen IX to form protoporphyrin IX; under anaerobic conditions uses menaquinone as an electron acceptor, under aerobic condition uses ubiquinone as an electron acceptor. {ECO:0000255|HAMAP-Rule:MF_00853}.; FUNCTION: Anaerobically in vitro transfers electrons to fumarate reductase and nitrate reductase; transfer to nitrate reductase couples this reaction to electron transfer across the cell inner membrane and thus ATP synthesis (PubMed:19583219, PubMed:20484676). Neither mesoporphyrinogen nor coproporphyrinogen are substrates (PubMed:19583219). Under aerobic conditions in vitro forms protoporphyrin IX using ubiquinone as an electron acceptor, is able to transfer electrons to cytochrome bd oxidase and cytochrome bo oxidase; transfer to these oxidases couples this reaction to electron transfer across the cell inner membrane and thus ATP synthesis. In cell free extracts deletion of both cytochrome oxidases prevents formation of protoporphyrin IX (PubMed:20484676). {ECO:0000269|PubMed:19583219, ECO:0000269|PubMed:20484676}.

## Biological Role

Component of protoporphyrinogen oxidase (complex.ecocyc.CPLX0-7811).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the 6-electron oxidation of protoporphyrinogen IX to form protoporphyrin IX; under anaerobic conditions uses menaquinone as an electron acceptor, under aerobic condition uses ubiquinone as an electron acceptor. {ECO:0000255|HAMAP-Rule:MF_00853}.; FUNCTION: Anaerobically in vitro transfers electrons to fumarate reductase and nitrate reductase; transfer to nitrate reductase couples this reaction to electron transfer across the cell inner membrane and thus ATP synthesis (PubMed:19583219, PubMed:20484676). Neither mesoporphyrinogen nor coproporphyrinogen are substrates (PubMed:19583219). Under aerobic conditions in vitro forms protoporphyrin IX using ubiquinone as an electron acceptor, is able to transfer electrons to cytochrome bd oxidase and cytochrome bo oxidase; transfer to these oxidases couples this reaction to electron transfer across the cell inner membrane and thus ATP synthesis. In cell free extracts deletion of both cytochrome oxidases prevents formation of protoporphyrin IX (PubMed:20484676). {ECO:0000269|PubMed:19583219, ECO:0000269|PubMed:20484676}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7811|complex.ecocyc.CPLX0-7811]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3850|gene.b3850]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACB4`
- `KEGG:ecj:JW3827;eco:b3850;ecoc:C3026_20815;`
- `GeneID:75174084;948331;`
- `GO:GO:0004729; GO:0005886; GO:0006779; GO:0006782; GO:0006783; GO:0006785; GO:0009055; GO:0010181; GO:0016020; GO:0070819`
- `EC:1.3.5.3`

## Notes

Protoporphyrinogen IX dehydrogenase [quinone] (EC 1.3.5.3) (Protoporphyrinogen IX dehydrogenase [menaquinone]) (Protoporphyrinogen IX dehydrogenase [ubiquinone]) (Protoporphyrinogen oxidase) (PPO)
