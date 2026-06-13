---
entity_id: "protein.P77781"
entity_type: "protein"
name: "menI"
source_database: "UniProt"
source_id: "P77781"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "menI ydiI b1686 JW1676"
---

# menI

`protein.P77781`

## Static

- Type: `protein`
- Source: `UniProt:P77781`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of 1,4-dihydroxy-2-naphthoyl-CoA (DHNA-CoA) to 1,4-dihydroxy-2-naphthoate (DHNA). Also shows significant activity toward a wide range of acyl-CoA thioesters, and minimal activity toward benzoyl-holoEntB. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:23564174, ECO:0000269|PubMed:24992697}.

## Biological Role

Component of 1,4-dihydroxy-2-naphthoyl-CoA hydrolase (complex.ecocyc.CPLX0-8128).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of 1,4-dihydroxy-2-naphthoyl-CoA (DHNA-CoA) to 1,4-dihydroxy-2-naphthoate (DHNA). Also shows significant activity toward a wide range of acyl-CoA thioesters, and minimal activity toward benzoyl-holoEntB. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:23564174, ECO:0000269|PubMed:24992697}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8128|complex.ecocyc.CPLX0-8128]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1686|gene.b1686]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77781`
- `KEGG:ecj:JW1676;eco:b1686;ecoc:C3026_09655;`
- `GeneID:75204532;946190;`
- `GO:GO:0005829; GO:0009234; GO:0016289; GO:0016787; GO:0061522`
- `EC:3.1.2.28`

## Notes

1,4-dihydroxy-2-naphthoyl-CoA hydrolase (DHNA-CoA hydrolase) (EC 3.1.2.28) (DHNA-CoA thioesterase)
