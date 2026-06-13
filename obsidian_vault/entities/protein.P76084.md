---
entity_id: "protein.P76084"
entity_type: "protein"
name: "paaI"
source_database: "UniProt"
source_id: "P76084"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaI ydbV b1396 JW1391"
---

# paaI

`protein.P76084`

## Static

- Type: `protein`
- Source: `UniProt:P76084`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Thioesterase with a preference for ring-hydroxylated phenylacetyl-CoA esters. Hydrolyzes 3,4-dihydroxyphenylacetyl-CoA, 3-hydroxyphenylacetyl-CoA and 4-hydroxyphenylacetyl-CoA. Inactive towards 4-hydroxybenzoyl-CoA and 4-hydroxyphenacyl-CoA. {ECO:0000269|PubMed:16464851, ECO:0000269|PubMed:9748275}. PaaI belongs to the acyl-CoA thioesterase subfamily of the hotdog-fold superfamily of enzymes . Among the relevant phenylacetate degradation pathway intermediates, its primary substrate appears to be phenylacetyl-CoA , although it was previously thought that its preferred substrates were ring-hydroxylated phenylacetyl-CoA thioesters . It may be involved in detoxification or salvage reactions for breakdown products of the unstable early intermediates of the phenylacetate degradation pathway . A crystal structure of PaaI has been solved at 2 Å resolution . A paaI mutant does not exhibit a defect in utilization of phenylacetate as a source of carbon . PaaI activity is increased in cells grown on phenylacetate . PaaI: "phenylacetic acid degradation"

## Biological Role

Component of phenylacetyl-CoA thioesterase (complex.ecocyc.CPLX0-3941).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Thioesterase with a preference for ring-hydroxylated phenylacetyl-CoA esters. Hydrolyzes 3,4-dihydroxyphenylacetyl-CoA, 3-hydroxyphenylacetyl-CoA and 4-hydroxyphenylacetyl-CoA. Inactive towards 4-hydroxybenzoyl-CoA and 4-hydroxyphenacyl-CoA. {ECO:0000269|PubMed:16464851, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3941|complex.ecocyc.CPLX0-3941]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1396|gene.b1396]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76084`
- `KEGG:ecj:JW1391;eco:b1396;ecoc:C3026_08145;`
- `GeneID:75057358;945265;`
- `GO:GO:0010124; GO:0016289`
- `EC:3.1.2.-`

## Notes

Acyl-coenzyme A thioesterase PaaI (EC 3.1.2.-) (Phenylacetic acid degradation protein PaaI)
