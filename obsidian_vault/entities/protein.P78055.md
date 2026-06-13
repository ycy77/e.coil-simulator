---
entity_id: "protein.P78055"
entity_type: "protein"
name: "fsaA"
source_database: "UniProt"
source_id: "P78055"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fsaA fsa mipB ybiZ b0825 JW5109"
---

# fsaA

`protein.P78055`

## Static

- Type: `protein`
- Source: `UniProt:P78055`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the reversible formation of fructose 6-phosphate from dihydroxyacetone (DHA) and D-glyceraldehyde 3-phosphate via an aldolization reaction. Can utilize several aldehydes as acceptor compounds in vitro, and hydroxyacetone (HA) or 1-hydroxy-butan-2-one as alternative donor substrate. Is also able to catalyze the direct stereoselective self-aldol addition of glycolaldehyde to furnish D-(-)-threose, and cross-aldol reactions of glycolaldehyde to other aldehyde acceptors. Is not able to cleave fructose, fructose 1-phosphate, glucose 6-phosphate, sedoheptulose 1,7-bisphosphate, xylulose 5-phosphate, ribulose 5-phosphate, and fructose 1,6-bisphosphate; cannot use dihydroxyacetone phosphate as donor compound nor D-glyceraldehyde as acceptor. Does not display transaldolase activity. {ECO:0000269|PubMed:11120740, ECO:0000269|PubMed:17985886, ECO:0000269|PubMed:19554584, ECO:0000269|Ref.6}.

## Biological Role

Component of fructose-6-phosphate aldolase 1 (complex.ecocyc.CPLX0-201).

## Annotation

FUNCTION: Catalyzes the reversible formation of fructose 6-phosphate from dihydroxyacetone (DHA) and D-glyceraldehyde 3-phosphate via an aldolization reaction. Can utilize several aldehydes as acceptor compounds in vitro, and hydroxyacetone (HA) or 1-hydroxy-butan-2-one as alternative donor substrate. Is also able to catalyze the direct stereoselective self-aldol addition of glycolaldehyde to furnish D-(-)-threose, and cross-aldol reactions of glycolaldehyde to other aldehyde acceptors. Is not able to cleave fructose, fructose 1-phosphate, glucose 6-phosphate, sedoheptulose 1,7-bisphosphate, xylulose 5-phosphate, ribulose 5-phosphate, and fructose 1,6-bisphosphate; cannot use dihydroxyacetone phosphate as donor compound nor D-glyceraldehyde as acceptor. Does not display transaldolase activity. {ECO:0000269|PubMed:11120740, ECO:0000269|PubMed:17985886, ECO:0000269|PubMed:19554584, ECO:0000269|Ref.6}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-201|complex.ecocyc.CPLX0-201]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b0825|gene.b0825]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P78055`
- `KEGG:ecj:JW5109;eco:b0825;ecoc:C3026_05180;`
- `GeneID:945449;`
- `GO:GO:0005737; GO:0006000; GO:0042182; GO:0042802; GO:0097023`
- `EC:4.1.2.-`

## Notes

Fructose-6-phosphate aldolase 1 (EC 4.1.2.-) (Fructose-6-phosphate aldolase A) (FSAA)
