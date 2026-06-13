---
entity_id: "protein.P36561"
entity_type: "protein"
name: "cobS"
source_database: "UniProt"
source_id: "P36561"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cobS b1992 JW1970"
---

# cobS

`protein.P36561`

## Static

- Type: `protein`
- Source: `UniProt:P36561`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Joins adenosylcobinamide-GDP and alpha-ribazole to generate adenosylcobalamin (Ado-cobalamin). Also synthesizes adenosylcobalamin 5'-phosphate from adenosylcobinamide-GDP and alpha-ribazole 5'-phosphate (By similarity). {ECO:0000250}. E. coli K-12, as well as natural isolates, can synthesize cobalamin only when supplied with the intermediate cobinamide . cobS encodes a cobalamin 5'-phosphate synthase that carries out the penultimate step in adenosylcobalamin synthesis. Expression of the cobUST operon is induced by cobinamide .

## Biological Role

Catalyzes R05223 (reaction.R05223), COBALAMIN5PSYN-RXN (reaction.ecocyc.COBALAMIN5PSYN-RXN).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Joins adenosylcobinamide-GDP and alpha-ribazole to generate adenosylcobalamin (Ado-cobalamin). Also synthesizes adenosylcobalamin 5'-phosphate from adenosylcobinamide-GDP and alpha-ribazole 5'-phosphate (By similarity). {ECO:0000250}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05223|reaction.R05223]] `KEGG` `database` - via EC:2.7.8.26
- `catalyzes` --> [[reaction.ecocyc.COBALAMIN5PSYN-RXN|reaction.ecocyc.COBALAMIN5PSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1992|gene.b1992]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36561`
- `KEGG:ecj:JW1970;eco:b1992;ecoc:C3026_11240;`
- `GeneID:946520;`
- `GO:GO:0005886; GO:0008818; GO:0009236; GO:0051073`
- `EC:2.7.8.26`

## Notes

Adenosylcobinamide-GDP ribazoletransferase (EC 2.7.8.26) (Cobalamin synthase) (Cobalamin-5'-phosphate synthase)
