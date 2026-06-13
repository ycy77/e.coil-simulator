---
entity_id: "protein.P0AGG0"
entity_type: "protein"
name: "thiL"
source_database: "UniProt"
source_id: "P0AGG0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiL b0417 JW0407"
---

# thiL

`protein.P0AGG0`

## Static

- Type: `protein`
- Source: `UniProt:P0AGG0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent phosphorylation of thiamine-monophosphate (TMP) to form thiamine-pyrophosphate (TPP), the active form of vitamin B1. Cannot use thiamine as substrate. Is highly specific for ATP as phosphate donor. {ECO:0000269|PubMed:4567662, ECO:0000269|PubMed:6284709}. Thiamine phosphate kinase (ThiL) is involved in the final step of thiamine biosynthesis. ThiL catalyzes the phosphorylation of thiamine monophosphate to yield thiamine diphosphate in the presence of ATP and Mg2+ . Mutations in thiL resulted in a requirement for thiamine pyrophosphate for growth . In Salmonella typhimurium, altered ThiL activity resulted in decreased repression of transcription of thiamine pyrophosphate-regulated genes . The ThiL structure with substrate and product complexes in Aquifex aeolicus was determined .

## Biological Role

Catalyzes ATP:thiamin-phosphate phosphotransferase (reaction.R00617), THI-P-KIN-RXN (reaction.ecocyc.THI-P-KIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent phosphorylation of thiamine-monophosphate (TMP) to form thiamine-pyrophosphate (TPP), the active form of vitamin B1. Cannot use thiamine as substrate. Is highly specific for ATP as phosphate donor. {ECO:0000269|PubMed:4567662, ECO:0000269|PubMed:6284709}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00617|reaction.R00617]] `KEGG` `database` - via EC:2.7.4.16
- `catalyzes` --> [[reaction.ecocyc.THI-P-KIN-RXN|reaction.ecocyc.THI-P-KIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0417|gene.b0417]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGG0`
- `KEGG:ecj:JW0407;eco:b0417;ecoc:C3026_02035;`
- `GeneID:947387;`
- `GO:GO:0000287; GO:0005524; GO:0009030; GO:0009228; GO:0009229; GO:0046872`
- `EC:2.7.4.16`

## Notes

Thiamine-monophosphate kinase (TMP kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16)
