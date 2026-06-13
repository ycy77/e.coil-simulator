---
entity_id: "protein.P62623"
entity_type: "protein"
name: "ispH"
source_database: "UniProt"
source_id: "P62623"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ispH lytB yaaE b0029 JW0027"
---

# ispH

`protein.P62623`

## Static

- Type: `protein`
- Source: `UniProt:P62623`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate (HMBPP) into a mixture of isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP). Acts in the terminal step of the DOXP/MEP pathway for isoprenoid precursor biosynthesis (PubMed:11418107, PubMed:11818558, PubMed:12706830, PubMed:19569147, PubMed:22137895). In vitro, can also hydrate acetylenes to aldehydes and ketones via anti-Markovnikov/Markovnikov addition (PubMed:22948824). {ECO:0000269|PubMed:11418107, ECO:0000269|PubMed:11818558, ECO:0000269|PubMed:12706830, ECO:0000269|PubMed:19569147, ECO:0000269|PubMed:22137895, ECO:0000269|PubMed:22948824}.

## Biological Role

Catalyzes dimethylallyl diphosphate:ferredoxin oxidoreductase (reaction.R08210). Component of 4-hydroxy-3-methylbut-2-enyl diphosphate reductase (complex.ecocyc.CPLX0-7564).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate (HMBPP) into a mixture of isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP). Acts in the terminal step of the DOXP/MEP pathway for isoprenoid precursor biosynthesis (PubMed:11418107, PubMed:11818558, PubMed:12706830, PubMed:19569147, PubMed:22137895). In vitro, can also hydrate acetylenes to aldehydes and ketones via anti-Markovnikov/Markovnikov addition (PubMed:22948824). {ECO:0000269|PubMed:11418107, ECO:0000269|PubMed:11818558, ECO:0000269|PubMed:12706830, ECO:0000269|PubMed:19569147, ECO:0000269|PubMed:22137895, ECO:0000269|PubMed:22948824}.

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R08210|reaction.R08210]] `KEGG` `database` - via EC:1.17.7.4
- `is_component_of` --> [[complex.ecocyc.CPLX0-7564|complex.ecocyc.CPLX0-7564]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0029|gene.b0029]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P62623`
- `KEGG:ecj:JW0027;eco:b0029;ecoc:C3026_00140;`
- `GeneID:93777407;944777;`
- `GO:GO:0005829; GO:0016114; GO:0019288; GO:0046872; GO:0050992; GO:0051538; GO:0051539; GO:0051745`
- `EC:1.17.7.4`

## Notes

4-hydroxy-3-methylbut-2-enyl diphosphate reductase (HMBPP reductase) (EC 1.17.7.4) (1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate reductase)
