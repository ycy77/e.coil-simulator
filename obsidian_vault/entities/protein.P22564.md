---
entity_id: "protein.P22564"
entity_type: "protein"
name: "rihC"
source_database: "UniProt"
source_id: "P22564"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rihC yaaF b0030 JW0028"
---

# rihC

`protein.P22564`

## Static

- Type: `protein`
- Source: `UniProt:P22564`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes both purine and pyrimidine ribonucleosides with a broad-substrate specificity with decreasing activity in the order uridine, xanthosine, inosine, adenosine, cytidine, guanosine. rihC encodes a ribonucleoside hydrolase with a broad substrate specificity. It has decreasing activity on substrates in the order uridine > xanthosine > inosine > adenosine > cytidine . The enzyme has no activity with deoxyribonucleosides . E. coli contains two other nucleoside hydrolases with differing specificities, encoded by rihA and rihB . The transition state of the enzyme has been modeled based on kinetic isotope effects . Potential active and catalytic sites and the catalytic mechanism of RihC have been computationally predicted . An rihA rihB rihC triple mutant does not exhibit an obvious growth defect . The rihA and rihC genes are subject to catabolite repression . Transcription is induced by nalidixic acid, but not by mitomycin C, and induction does not require LexA .

## Biological Role

Catalyzes ADENOSINE-NUCLEOSIDASE-RXN (reaction.ecocyc.ADENOSINE-NUCLEOSIDASE-RXN), INOSINE-NUCLEOSIDASE-RXN (reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN), RXN0-361 (reaction.ecocyc.RXN0-361), RXN0-363 (reaction.ecocyc.RXN0-363), URIDINE-NUCLEOSIDASE-RXN (reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Hydrolyzes both purine and pyrimidine ribonucleosides with a broad-substrate specificity with decreasing activity in the order uridine, xanthosine, inosine, adenosine, cytidine, guanosine.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ADENOSINE-NUCLEOSIDASE-RXN|reaction.ecocyc.ADENOSINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN|reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-361|reaction.ecocyc.RXN0-361]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-363|reaction.ecocyc.RXN0-363]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN|reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0030|gene.b0030]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22564`
- `KEGG:ecj:JW0028;eco:b0030;ecoc:C3026_00145;`
- `GeneID:75169929;944796;`
- `GO:GO:0005829; GO:0006144; GO:0006152; GO:0006206; GO:0006974; GO:0008477; GO:0042454; GO:0045437; GO:0047622; GO:0047724; GO:0050263`
- `EC:3.2.-.-`

## Notes

Non-specific ribonucleoside hydrolase RihC (EC 3.2.-.-) (Purine/pyrimidine ribonucleoside hydrolase)
