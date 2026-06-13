---
entity_id: "protein.P24188"
entity_type: "protein"
name: "trhO"
source_database: "UniProt"
source_id: "P24188"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trhO yceA b1055 JW1042"
---

# trhO

`protein.P24188`

## Static

- Type: `protein`
- Source: `UniProt:P24188`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes oxygen-dependent 5-hydroxyuridine (ho5U) modification at position 34 in tRNAs, the first step in 5-carboxymethoxyuridine (cmo5U) biosynthesis (PubMed:31253794). May be part of an alternate pathway, which is able to bypass cmo5U biogenesis in a subset of tRNAs under aerobic conditions (PubMed:31253794). {ECO:0000269|PubMed:31253794}. TrhP is involved in the formation of the cmo5U34 modification on tRNAs during anaerobic growth conditions, while TrhO-mediated formation of ho5U34 utilizes molecular oxygen as the oxygen atom donor . A ΔtrhP trhO double mutant has lost all modification of the U34 wobble base of tRNAVal1 and grows more slowly than wild type. Additional knockout of EG30094 serU, EG30104 thrW or EG30066 proK, which encode tRNAs responsible for decoding G-ending codons, results in further reduction of growth . Mutagenesis of the predicted active site residues C200, T201, G203, and R205, and residues K112 and R114 predicted to be involved in substrate binding of TrhO results in loss of activity in the mutant strain . TrhO: "tRNA hydroxylation O"

## Biological Role

Catalyzes RXN0-7349 (reaction.ecocyc.RXN0-7349).

## Annotation

FUNCTION: Catalyzes oxygen-dependent 5-hydroxyuridine (ho5U) modification at position 34 in tRNAs, the first step in 5-carboxymethoxyuridine (cmo5U) biosynthesis (PubMed:31253794). May be part of an alternate pathway, which is able to bypass cmo5U biogenesis in a subset of tRNAs under aerobic conditions (PubMed:31253794). {ECO:0000269|PubMed:31253794}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7349|reaction.ecocyc.RXN0-7349]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1055|gene.b1055]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24188`
- `KEGG:ecj:JW1042;eco:b1055;ecoc:C3026_06420;`
- `GeneID:75203642;945601;`
- `GO:GO:0002098; GO:0006400; GO:0016491; GO:0016705`
- `EC:1.14.-.-`

## Notes

tRNA uridine(34) hydroxylase (EC 1.14.-.-) (ORF39.9) (tRNA hydroxylation protein O)
