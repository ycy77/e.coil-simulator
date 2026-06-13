---
entity_id: "protein.P0AB96"
entity_type: "protein"
name: "arsC"
source_database: "UniProt"
source_id: "P0AB96"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arsC arsG b3503 JW3470"
---

# arsC

`protein.P0AB96`

## Static

- Type: `protein`
- Source: `UniProt:P0AB96`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in resistance to arsenate. Catalyzes the reduction of arsenate [As(V)] to arsenite [As(III)]. {ECO:0000250|UniProtKB:P08692}. Based on sequence similarity with the R773-encoded enzyme, ArsC is thought to catalyze the reduction of arsenate to arsenite using glutathione with glutaredoxin as electron donors. The resulting arsenite is then removed from the cell via the ArsB transport protein. Unlike the chromosomally-encoded ArsC described here, the R773 plasmid-encoded enzyme has been studied experimentally. The arsenate reductase reaction involves sequential action of three different thiolate nucleophiles that function as a redox cascade . All three glutaredoxins in E. coli can participate in the arsenate reductase reaction, but glutaredoxin 2 appears the most effective . Crystal structures of ArsC have been solved , and residues involved in arsenate binding and transition-state stabilization were identified . Based on sequence similarity with the R773-plasmid encoded arsenite resistance operon, ArsB is a transporter and ArsC is an arsenate reductase . The chromosomally encoded operon, however, is lacking arsA, which encodes a putative ATP-binding protein. Expression of arsRBC is induced by exposure to arsenite ; transcription is negatively regulated by ArsR...

## Biological Role

Catalyzes glutharedoxin:arsenate oxidoreductase (reaction.R05747), RXN-982 (reaction.ecocyc.RXN-982).

## Annotation

FUNCTION: Involved in resistance to arsenate. Catalyzes the reduction of arsenate [As(V)] to arsenite [As(III)]. {ECO:0000250|UniProtKB:P08692}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05747|reaction.R05747]] `KEGG` `database` - via EC:1.20.4.1
- `catalyzes` --> [[reaction.ecocyc.RXN-982|reaction.ecocyc.RXN-982]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3503|gene.b3503]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB96`
- `KEGG:ecj:JW3470;eco:b3503;ecoc:C3026_18975;`
- `GeneID:93778489;948018;`
- `GO:GO:0006974; GO:0008794; GO:0046685`
- `EC:1.20.4.1`

## Notes

Arsenate reductase (EC 1.20.4.1) (Arsenical pump modifier)
