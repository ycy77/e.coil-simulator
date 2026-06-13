---
entity_id: "protein.P0A746"
entity_type: "protein"
name: "msrB"
source_database: "UniProt"
source_id: "P0A746"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "msrB yeaA b1778 JW1767"
---

# msrB

`protein.P0A746`

## Static

- Type: `protein`
- Source: `UniProt:P0A746`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Peptide methionine sulfoxide reductase MsrB (EC 1.8.4.12) (Peptide-methionine (R)-S-oxide reductase) MsrB is one of several methionine sulfoxide reductases in E. coli . Methionine residues in proteins can be damaged by oxidation and can be repaired by methionine sulfoxide reductases . Modification of chemically oxidized N-terminal methionines by formylation or acetylation significantly increases the catalytic efficiency of reduction by MsrB and EG11433-MONOMER MsrA in redox kinetic studies in vitro . MsrA and MsrB are also important for keeping EG10823-MONOMER RecA active under oxidative stress conditions . Conversely, the transcription factor G7924 HypT is activated by methionine oxidation and inactivated by MsrA/MsrB activity . The CXXC motifs in MsrB are essential for metal binding and catalytic activity . Some organisms produce a methionine sulfoxide reductase composed of two domains with similarity to MsrA and MsrB, respectively, whereas E. coli produces these two distinct polypeptides. MsrB exhibits 1000-fold lower catalytic efficiency than MsrA toward free methionine sulfoxide . MsrA and MsrB exhibit similar activity (quantitatively) toward an oxidized peptide substrate, though they appear to exhibit some differences in specificity for substrate sites within the peptide . The E...

## Biological Role

Catalyzes 1.8.4.12-RXN (reaction.ecocyc.1.8.4.12-RXN), 1.8.4.14-RXN (reaction.ecocyc.1.8.4.14-RXN).

## Annotation

Peptide methionine sulfoxide reductase MsrB (EC 1.8.4.12) (Peptide-methionine (R)-S-oxide reductase)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.1.8.4.12-RXN|reaction.ecocyc.1.8.4.12-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.1.8.4.14-RXN|reaction.ecocyc.1.8.4.14-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1778|gene.b1778]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A746`
- `KEGG:ecj:JW1767;eco:b1778;ecoc:C3026_10145;`
- `GeneID:93775987;947188;`
- `GO:GO:0005506; GO:0005737; GO:0005829; GO:0006979; GO:0008270; GO:0030091; GO:0033743; GO:0033745; GO:0046686`
- `EC:1.8.4.12`

## Notes

Peptide methionine sulfoxide reductase MsrB (EC 1.8.4.12) (Peptide-methionine (R)-S-oxide reductase)
