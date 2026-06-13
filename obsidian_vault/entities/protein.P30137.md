---
entity_id: "protein.P30137"
entity_type: "protein"
name: "thiE"
source_database: "UniProt"
source_id: "P30137"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiE b3993 JW3957"
---

# thiE

`protein.P30137`

## Static

- Type: `protein`
- Source: `UniProt:P30137`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Condenses 4-methyl-5-(beta-hydroxyethyl)thiazole monophosphate (THZ-P) and 2-methyl-4-amino-5-hydroxymethyl pyrimidine pyrophosphate (HMP-PP) to form thiamine monophosphate (TMP). {ECO:0000269|PubMed:15292217, ECO:0000269|Ref.5}. Thiamine phosphate synthase (ThiE) is involved in the biosynthesis of thiamine. Thiamine biosynthesis involves the separate formation of a pyrimidine and a thiazole precursors, which are then coupled to form thiamine phosphate. ThiE combines the pyrimidine component AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP (HMP-PP) with either THZ-P (HET-P), its carboxylated version CPD-13576 (cHET-P), or the tautomeric form CPD-13575 (cThz*-P) to generate thiamine phosphate . ThiE was identified, overexpressed and found to be required for the linkage of thiazole and pyrimidine . Null mutants of thiE require thiamine for growth . The crystal structure of ThiE from Bacillus subtilis has been determined at 1.25 Å .

## Biological Role

Catalyzes RXN-12610 (reaction.ecocyc.RXN-12610), thiamin phosphate synthase (reaction.ecocyc.RXN-12611), THI-P-SYN-RXN (reaction.ecocyc.THI-P-SYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Condenses 4-methyl-5-(beta-hydroxyethyl)thiazole monophosphate (THZ-P) and 2-methyl-4-amino-5-hydroxymethyl pyrimidine pyrophosphate (HMP-PP) to form thiamine monophosphate (TMP). {ECO:0000269|PubMed:15292217, ECO:0000269|Ref.5}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-12610|reaction.ecocyc.RXN-12610]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12611|reaction.ecocyc.RXN-12611]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THI-P-SYN-RXN|reaction.ecocyc.THI-P-SYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3993|gene.b3993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30137`
- `KEGG:ecj:JW3957;eco:b3993;ecoc:C3026_21570;`
- `GeneID:75205511;948491;`
- `GO:GO:0000287; GO:0004789; GO:0005737; GO:0009228; GO:0009229; GO:0046872`
- `EC:2.5.1.3`

## Notes

Thiamine-phosphate synthase (TP synthase) (TPS) (EC 2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphorylase) (TMP-PPase)
