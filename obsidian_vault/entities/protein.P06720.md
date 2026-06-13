---
entity_id: "protein.P06720"
entity_type: "protein"
name: "melA"
source_database: "UniProt"
source_id: "P06720"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "melA mel-7 b4119 JW4080"
---

# melA

`protein.P06720`

## Static

- Type: `protein`
- Source: `UniProt:P06720`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Alpha-galactosidase (EC 3.2.1.22) (Melibiase) α-galactosidase is required for utilization of α-galactosides as nutrients . α-galactosidase was previously thought to be a tetramer , but is now believed to be a dimer . The enzymatic activity is very unstable upon purification, but can be stabilized by the addition of NAD+ . The Aes protein can bind to and inhibit the activity of α-galactosidase . melA mutants are unable to utilize melibiose as the sole source of carbon . MelA activity can be induced by three α-D-galactosides: melibiose, melibiitol and galactinol . Although melA and melB are co-transcribed, the expression of melB is much lower than that of melA. This appears to be due to a NusA binding site between the two ORFs, leading to transcription attenuation. In addition, the melA mRNA is more stable than the melAB mRNA .

## Biological Role

Catalyzes epimelibiose galactohydrolase (reaction.R01329). Component of α-galactosidase (complex.ecocyc.ALPHAGALACTOSID-CPLX).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Alpha-galactosidase (EC 3.2.1.22) (Melibiase)

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01329|reaction.R01329]] `KEGG` `database` - via EC:3.2.1.22
- `is_component_of` --> [[complex.ecocyc.ALPHAGALACTOSID-CPLX|complex.ecocyc.ALPHAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4119|gene.b4119]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06720`
- `KEGG:ecj:JW4080;eco:b4119;ecoc:C3026_22260;`
- `GeneID:948636;`
- `GO:GO:0004557; GO:0005829; GO:0005995; GO:0016616; GO:0030145; GO:0070403`
- `EC:3.2.1.22`

## Notes

Alpha-galactosidase (EC 3.2.1.22) (Melibiase)
