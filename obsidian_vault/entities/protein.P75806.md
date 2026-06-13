---
entity_id: "protein.P75806"
entity_type: "protein"
name: "ybjG"
source_database: "UniProt"
source_id: "P75806"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybjG b0841 JW5112"
---

# ybjG

`protein.P75806`

## Static

- Type: `protein`
- Source: `UniProt:P75806`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Overexpression leads to increased undecaprenyl diphosphatase activity and to increased resistance to bacitracin. May have a preferred substrate other than undecaprenyl diphosphate in vivo. {ECO:0000269|PubMed:15778224}. YbjG is similar to the bacitracin resistance protein BcrC of Bacillus licheniformis. Disruption of ybjG causes increased bacitracin sensitivity, and overexpression causes increased resistance to bacitracin . Simultaneous inactivation of ybjG, EG11665 bacA, and EG10705 pgpB is lethal. Depletion of BacA in the triple mutant strain causes changes in cell morphology and lysis. Overexpression of ybjG, G7146 lpxT, bacA, or pgpB leads to increased undecaprenyl diphosphate (C55PP) phosphatase activity in crude membrane extracts. Expression of C55PP phosphatase activity from one of the three genes ybjG, bacA, and pgpB appears to be sufficient for synthesis of undecaprenyl phosphate and survival . bacA ybjG double and bacA ybjG lpxT triple deletion mutants are hypersensitive to the undecaprenyl phosphate biosynthesis inhibitor fosmidomycin . YbjG is an inner membrane protein with four transmembrane domains . The C terminus is located in the cytoplasm . The acid phosphatase domain of YbjG is located on the periplasmic side of the plasma membrane . ybjG expression is increased in the constitutively active evgS1 mutant and may be directly regulated by PhoP...

## Biological Role

Catalyzes UNDECAPRENYL-DIPHOSPHATASE-RXN (reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Annotation

FUNCTION: Overexpression leads to increased undecaprenyl diphosphatase activity and to increased resistance to bacitracin. May have a preferred substrate other than undecaprenyl diphosphate in vivo. {ECO:0000269|PubMed:15778224}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN|reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0841|gene.b0841]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75806`
- `KEGG:ecj:JW5112;eco:b0841;ecoc:C3026_05260;`
- `GeneID:945450;`
- `GO:GO:0005886; GO:0008360; GO:0009252; GO:0046677; GO:0050380; GO:0071555`
- `EC:3.6.1.27`

## Notes

Putative undecaprenyl-diphosphatase YbjG (EC 3.6.1.27) (Undecaprenyl pyrophosphate phosphatase)
