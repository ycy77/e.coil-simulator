---
entity_id: "protein.P0ACP5"
entity_type: "protein"
name: "gntR"
source_database: "UniProt"
source_id: "P0ACP5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gntR b3438 JW5946"
---

# gntR

`protein.P0ACP5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACP5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Negative regulator for the gluconate utilization system GNT-I, the gntUKR operon. The Gluconate repressor," GntR, is a transcription factor that negatively regulates the operon involved in the catabolism of D-gluconate via the Entner-Doudoroff pathway and also represses genes involved in two different systems related to D-gluconate uptake: gluconate I and gluconate II . This regulator is part of the gntRKU operon, yet it can also be constitutively expressed as an independent (gntR) transcription unit . In addition, the genes regulated by GntR are induced when Escherichia coli is grown in the presence of the inducer, D-gluconate, and in the absence of glucose. In the absence of inducer, this repressor binds in tandem to inverted repeat sequences that consist of 20-nucleotide-long DNA target sites . Binding of GntR to DNA is diminished in the presence of the inducer D-gluconate. By using synthetic gene circuits, it was demonstrated that GntR represses transcription through stabilization of RNA polymerase (RNAP) at both positions upstream and downstream from the promoter . GntR is closely homologous to IdnR (53% identity) and belongs to the LacI/GalR family of transcriptional regulators...

## Biological Role

Component of GntR-D-gluconate (complex.ecocyc.MONOMER-55).

## Annotation

FUNCTION: Negative regulator for the gluconate utilization system GNT-I, the gntUKR operon.

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.MONOMER-55|complex.ecocyc.MONOMER-55]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1850|gene.b1850]] `RegulonDB` `S` - regulator=GntR; target=eda; function=-
- `represses` --> [[gene.b1851|gene.b1851]] `RegulonDB` `S` - regulator=GntR; target=edd; function=-
- `represses` --> [[gene.b3415|gene.b3415]] `RegulonDB` `S` - regulator=GntR; target=gntT; function=-
- `represses` --> [[gene.b3437|gene.b3437]] `RegulonDB` `C` - regulator=GntR; target=gntK; function=-
- `represses` --> [[gene.b4476|gene.b4476]] `RegulonDB` `C` - regulator=GntR; target=gntU; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3438|gene.b3438]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACP5`
- `KEGG:ecj:JW5946;eco:b3438;ecoc:C3026_18630;`
- `GeneID:75059978;947946;`
- `GO:GO:0000976; GO:0003700; GO:0005829; GO:0006355; GO:0006974; GO:0045892; GO:0045893`

## Notes

HTH-type transcriptional regulator GntR (Gluconate utilization system GNT-I transcriptional repressor)
