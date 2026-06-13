---
entity_id: "protein.P39161"
entity_type: "protein"
name: "uxuR"
source_database: "UniProt"
source_id: "P39161"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uxuR b4324 JW4287"
---

# uxuR

`protein.P39161`

## Static

- Type: `protein`
- Source: `UniProt:P39161`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor for the uxuRBA operon. The "hexuronate regulator," UxuR, is a transcriptional factor. This protein negatively regulates its own synthesis, and in the absence of fructuronate it represses transcription of the cluster of operons involved in transport and degradation of the sugar acids β-D-glucuronides, glucuronate, and gluconate . This regulator is subject to catabolic repression in the presence of glucose and at low levels of cyclic AMP. In addition, UxuR appears to regulate genes involved in motility and biofilm formation . Although little is known about the regulating mechanism of UxuR, it has been shown to act as a repressor, binding to a putative inverted repeat sequence from the uid operon in a cooperative process with UidR . In 1986, Blanco et al. proposed that total repression of UxuR is achieved in the presence of UidR, suggesting the possibility that UxuR and UidR form a complex. Independently, each repressor binds to DNA separately . On the other hand, UxuR is highly similar to ExuR (49% identity), and apparently both act together and are capable of cross talk to regulate expression of the uxuR regulon . ExuR is capable of binding to the uxuR promoter in the presence of glucuronate, unlike UxuR, which can bind to its own promoter in the absence of glucuronate...

## Biological Role

Component of UxuR-α-D-galacturonate,α-D-glucuronate (complex.ecocyc.CPLX0-8209), UxuR-D-fructuronate (complex.ecocyc.MONOMER0-2101).

## Annotation

FUNCTION: Repressor for the uxuRBA operon.

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8209|complex.ecocyc.CPLX0-8209]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER0-2101|complex.ecocyc.MONOMER0-2101]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1923|gene.b1923]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3094|gene.b3094]] `RegulonDB` `S` - regulator=UxuR; target=exuR; function=-
- `represses` --> [[gene.b4321|gene.b4321]] `RegulonDB` `C` - regulator=UxuR; target=gntP; function=-
- `represses` --> [[gene.b4323|gene.b4323]] `RegulonDB` `C` - regulator=UxuR; target=uxuB; function=-
- `represses` --> [[gene.b4357|gene.b4357]] `RegulonDB` `S` - regulator=UxuR; target=lgoR; function=-
- `represses` --> [[gene.b4358|gene.b4358]] `RegulonDB` `S` - regulator=UxuR; target=lgoD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4324|gene.b4324]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39161`
- `KEGG:ecj:JW4287;eco:b4324;ecoc:C3026_23365;`
- `GeneID:75169816;75202995;948849;`
- `GO:GO:0000987; GO:0003700; GO:0006351; GO:0006355`

## Notes

Uxu operon transcriptional regulator
