---
entity_id: "protein.P09373"
entity_type: "protein"
name: "pflB"
source_database: "UniProt"
source_id: "P09373"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pflB pfl b0903 JW0886"
---

# pflB

`protein.P09373`

## Static

- Type: `protein`
- Source: `UniProt:P09373`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the conversion of pyruvate to formate and acetyl-CoA (PubMed:4615902). In addition, may be involved in the control of the activity of the formate channel FocA, via direct interaction with FocA (PubMed:24887098). {ECO:0000269|PubMed:24887098, ECO:0000269|PubMed:4615902}. Escherichia coli pyruvate-formate lyase (PflB) is a central enzyme of anaerobic metabolism. It catalyzes the coenzyme A-dependent, non-oxidative cleavage of pyruvate to acetyl-CoA and formate in anaerobically growing cells (see pathway FERMENTATION-PWY). Under anaerobic conditions, induction of transcription of pflB involves CPLX0-7797 and the PHOSPHO-ARCA and ARCB-CPLX regulatory proteins . At the post-translational level the enzyme is regulated by activation . Activation of the inactive enzyme is catalyzed by the same PFLACTENZ-MONOMER that also activates KETOBUTFORMLY-INACT-MONOMER . This activation process requires reduced flavodoxin that is generated via a coenzyme A-acylating PYRUFLAVREDUCT-MONOMER, or FLAVONADPREDUCT-MONOMER . Activation introduces a free radical into the enzyme (see below). PflB utilizes a "ping-pong" mechanism that proceeds via two half-reactions. The enzyme is also active with 2-oxobutanoate as substrate, but pyruvate is the preferred substrate . An active site Gly734 radical is used to reversibly cleave the C1-C2 bond of pyruvate...

## Biological Role

Catalyzes acetyl-CoA:formate C-acetyltransferase (reaction.R00212), propanoyl-CoA:formate C-propanoyltransferase (reaction.R06987). Component of PFL-GrcA complex (complex.ecocyc.CPLX0-9871), activated pyruvate-formate lyase (complex.ecocyc.PYRUVFORMLY-CPLX), pyruvate formate-lyase (inactive) (complex.ecocyc.PYRUVFORMLY-INACTIVE-CPLX).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of pyruvate to formate and acetyl-CoA (PubMed:4615902). In addition, may be involved in the control of the activity of the formate channel FocA, via direct interaction with FocA (PubMed:24887098). {ECO:0000269|PubMed:24887098, ECO:0000269|PubMed:4615902}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00212|reaction.R00212]] `KEGG` `database` - via EC:2.3.1.54
- `catalyzes` --> [[reaction.R06987|reaction.R06987]] `KEGG` `database` - via EC:2.3.1.54
- `is_component_of` --> [[complex.ecocyc.CPLX0-9871|complex.ecocyc.CPLX0-9871]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PYRUVFORMLY-CPLX|complex.ecocyc.PYRUVFORMLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PYRUVFORMLY-INACTIVE-CPLX|complex.ecocyc.PYRUVFORMLY-INACTIVE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0903|gene.b0903]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09373`
- `KEGG:ecj:JW0886;eco:b0903;ecoc:C3026_05575;`
- `GeneID:86863428;93776515;945514;`
- `GO:GO:0005829; GO:0006006; GO:0008861; GO:0016020; GO:0044814`
- `EC:2.3.1.54`

## Notes

Formate acetyltransferase 1 (EC 2.3.1.54) (Pyruvate formate-lyase 1)
