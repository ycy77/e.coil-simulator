---
entity_id: "protein.P42620"
entity_type: "protein"
name: "yqjG"
source_database: "UniProt"
source_id: "P42620"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yqjG b3102 JW3073"
---

# yqjG

`protein.P42620`

## Static

- Type: `protein`
- Source: `UniProt:P42620`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes glutathione (GSH)-dependent reduction of glutathionyl-hydroquinones (GS-HQs) to the corresponding hydroquinones. Can use a variety of GS-HQs as substrates, such as GS-p-hydroquinone (GS-HQ), GS-hydroxy-p-hydroquinone (GS-HHQ), GS-methyl-p-hydroquinone (GS-MHQ), GS-menadiol, and GS-trichloro-p-hydroquinone (GS-TriCH). Also displays GSH-dependent disulfide-bond reduction activity toward HED (2-hydroxyethyl disulfide), and is able to catalyze DMA (dimethylarsinate) reduction. Exhibits no GSH transferase activity with 1-chloro-2,4-dinitrobenzene (CDNB). {ECO:0000269|PubMed:20388120, ECO:0000269|PubMed:22686328, ECO:0000269|PubMed:22955277}.

## Biological Role

Component of glutathionyl-hydroquinone reductase YqjG (complex.ecocyc.CPLX0-7984).

## Annotation

FUNCTION: Catalyzes glutathione (GSH)-dependent reduction of glutathionyl-hydroquinones (GS-HQs) to the corresponding hydroquinones. Can use a variety of GS-HQs as substrates, such as GS-p-hydroquinone (GS-HQ), GS-hydroxy-p-hydroquinone (GS-HHQ), GS-methyl-p-hydroquinone (GS-MHQ), GS-menadiol, and GS-trichloro-p-hydroquinone (GS-TriCH). Also displays GSH-dependent disulfide-bond reduction activity toward HED (2-hydroxyethyl disulfide), and is able to catalyze DMA (dimethylarsinate) reduction. Exhibits no GSH transferase activity with 1-chloro-2,4-dinitrobenzene (CDNB). {ECO:0000269|PubMed:20388120, ECO:0000269|PubMed:22686328, ECO:0000269|PubMed:22955277}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7984|complex.ecocyc.CPLX0-7984]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3102|gene.b3102]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42620`
- `KEGG:ecj:JW3073;eco:b3102;ecoc:C3026_16935;`
- `GeneID:947615;`
- `GO:GO:0004364; GO:0005737; GO:0016672; GO:0042803`
- `EC:1.8.5.7`

## Notes

Glutathionyl-hydroquinone reductase YqjG (GS-HQR) (EC 1.8.5.7)
