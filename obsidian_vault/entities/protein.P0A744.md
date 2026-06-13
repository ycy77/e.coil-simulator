---
entity_id: "protein.P0A744"
entity_type: "protein"
name: "msrA"
source_database: "UniProt"
source_id: "P0A744"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "msrA pms b4219 JW4178"
---

# msrA

`protein.P0A744`

## Static

- Type: `protein`
- Source: `UniProt:P0A744`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Could have an important function as a repair enzyme for proteins that have been inactivated by oxidation. Catalyzes the reversible oxidation-reduction of methionine sulfoxide in proteins to methionine. {ECO:0000269|PubMed:10964927}. MsrA is one of several methionine sulfoxide reductases in E. coli . Methionine residues in proteins, including the N-terminal methionine, can be damaged by oxidation and can be repaired (reduced) by methionine sulfoxide reductases . Modification of chemically oxidized N-terminal methionines by formylation or acetylation significantly increases the catalytic efficiency of reduction by MsrA and EG12394-MONOMER MsrB in redox kinetic studies in vitro . MsrA and MsrB are also important for keeping EG10823-MONOMER RecA active under oxidative stress conditions . Conversely, the transcription factor G7924 HypT is activated by methionine oxidation and inactivated by MsrA/MsrB activity . MsrA appears to use RED-THIOREDOXIN-MONOMER thioredoxin 1 (Trx1) as the electron donor in vivo . Overexpressed RED-THIOREDOXIN2-MONOMER thioredoxin 2 (Trx2) can substitute for Trx1 . Cys51, Cys198, and Cys206 are involved in catalysis. A three-step ping-pong reaction mechanism involving a sulfenic acid intermediate on Cys51 has been proposed...

## Biological Role

Catalyzes peptide-L-methionine:thioredoxin-disulfide S-oxidoreductase [L-methionine (S)-S-oxide-forming] (reaction.R04120), 1.8.4.13-RXN (reaction.ecocyc.1.8.4.13-RXN), RXN-8668 (reaction.ecocyc.RXN-8668).

## Annotation

FUNCTION: Could have an important function as a repair enzyme for proteins that have been inactivated by oxidation. Catalyzes the reversible oxidation-reduction of methionine sulfoxide in proteins to methionine. {ECO:0000269|PubMed:10964927}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04120|reaction.R04120]] `KEGG` `database` - via EC:1.8.4.11
- `catalyzes` --> [[reaction.ecocyc.1.8.4.13-RXN|reaction.ecocyc.1.8.4.13-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8668|reaction.ecocyc.RXN-8668]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4219|gene.b4219]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A744`
- `KEGG:ecj:JW4178;eco:b4219;ecoc:C3026_22785;`
- `GeneID:93777602;948734;`
- `GO:GO:0005737; GO:0005829; GO:0006979; GO:0008113; GO:0016671; GO:0030091; GO:0033744; GO:0034599`
- `EC:1.8.4.11`

## Notes

Peptide methionine sulfoxide reductase MsrA (Protein-methionine-S-oxide reductase) (EC 1.8.4.11) (Peptide-methionine (S)-S-oxide reductase) (Peptide Met(O) reductase)
