---
entity_id: "protein.P0AGE6"
entity_type: "protein"
name: "chrR"
source_database: "UniProt"
source_id: "P0AGE6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chrR yieF b3713 JW3691"
---

# chrR

`protein.P0AGE6`

## Static

- Type: `protein`
- Source: `UniProt:P0AGE6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of quinones (PubMed:14766567). Acts by simultaneous two-electron transfer, avoiding formation of highly reactive semiquinone intermediates and producing quinols that promote tolerance of H(2)O(2). Quinone reduction is probably the primary biological role of ChrR (By similarity). Can also reduce toxic chromate to insoluble and less toxic Cr(3+). Catalyzes the transfer of three electrons to Cr(6+) producing Cr(3+) and one electron to molecular oxygen without producing the toxic Cr(5+) species and only producing a minimal amount of reactive oxygen species (ROS). Chromate reduction protects the cell against chromate toxicity, but is likely a secondary activity (PubMed:14766567, PubMed:17088379, PubMed:22558308). Can also reduce potassium ferricyanide, 2,6-dichloroindophenol, V(5+), Mo(6+), methylene blue, cytochrome c and U(6+) (PubMed:14766567, PubMed:17088379). During chromate reduction, is able to use both NAD or NADP equally well (PubMed:14766567). {ECO:0000250|UniProtKB:Q88FF8, ECO:0000269|PubMed:14766567, ECO:0000269|PubMed:17088379, ECO:0000269|PubMed:22558308}. YieF is a flavoprotein containing the FMN cofactor; it belongs to the flavodoxin superfamily of enzymes . The enzyme is able to reduce chromate in vitro...

## Biological Role

Component of quinone reductase (complex.ecocyc.CPLX0-3121).

## Annotation

FUNCTION: Catalyzes the reduction of quinones (PubMed:14766567). Acts by simultaneous two-electron transfer, avoiding formation of highly reactive semiquinone intermediates and producing quinols that promote tolerance of H(2)O(2). Quinone reduction is probably the primary biological role of ChrR (By similarity). Can also reduce toxic chromate to insoluble and less toxic Cr(3+). Catalyzes the transfer of three electrons to Cr(6+) producing Cr(3+) and one electron to molecular oxygen without producing the toxic Cr(5+) species and only producing a minimal amount of reactive oxygen species (ROS). Chromate reduction protects the cell against chromate toxicity, but is likely a secondary activity (PubMed:14766567, PubMed:17088379, PubMed:22558308). Can also reduce potassium ferricyanide, 2,6-dichloroindophenol, V(5+), Mo(6+), methylene blue, cytochrome c and U(6+) (PubMed:14766567, PubMed:17088379). During chromate reduction, is able to use both NAD or NADP equally well (PubMed:14766567). {ECO:0000250|UniProtKB:Q88FF8, ECO:0000269|PubMed:14766567, ECO:0000269|PubMed:17088379, ECO:0000269|PubMed:22558308}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3121|complex.ecocyc.CPLX0-3121]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3713|gene.b3713]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGE6`
- `KEGG:ecj:JW3691;eco:b3713;ecoc:C3026_20130;`
- `GeneID:75173932;948225;`
- `GO:GO:0005829; GO:0006805; GO:0008753; GO:0010181; GO:0016491; GO:0042802; GO:0050136; GO:0051289`
- `EC:1.6.-.-; 1.6.5.2`

## Notes

Quinone reductase (EC 1.6.5.2) (Chromate reductase) (CHRR) (EC 1.6.-.-) (NAD(P)H dehydrogenase (quinone))
