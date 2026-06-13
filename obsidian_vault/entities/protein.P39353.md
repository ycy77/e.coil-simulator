---
entity_id: "protein.P39353"
entity_type: "protein"
name: "nanY"
source_database: "UniProt"
source_id: "P39353"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanY yjhC b4280 JW5769"
---

# nanY

`protein.P39353`

## Static

- Type: `protein`
- Source: `UniProt:P39353`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydratase involved in the degradation of sialic acids (PubMed:32542330, PubMed:32669363). Catalyzes the reversible conversion of the dehydrated form of N-acetylneuraminate (Neu5Ac), 2,7-anhydro-N-acetylneuraminate (2,7-AN), to Neu5Ac (PubMed:32542330, PubMed:32669363). Also catalyzes the irreversible conversion of 2-deoxy-2,3-didehydro-N-acetylneuraminate (2,3-EN) to Neu5Ac (PubMed:32542330). The reaction mechanism involves keto intermediates and the transient formation of NADH (PubMed:32542330). {ECO:0000269|PubMed:32542330, ECO:0000269|PubMed:32669363}.

## Biological Role

Component of KpLE2 phage-like element; 2,7-anhydro-N-acetylneuraminate hydratase (complex.ecocyc.CPLX0-8544).

## Annotation

FUNCTION: Hydratase involved in the degradation of sialic acids (PubMed:32542330, PubMed:32669363). Catalyzes the reversible conversion of the dehydrated form of N-acetylneuraminate (Neu5Ac), 2,7-anhydro-N-acetylneuraminate (2,7-AN), to Neu5Ac (PubMed:32542330, PubMed:32669363). Also catalyzes the irreversible conversion of 2-deoxy-2,3-didehydro-N-acetylneuraminate (2,3-EN) to Neu5Ac (PubMed:32542330). The reaction mechanism involves keto intermediates and the transient formation of NADH (PubMed:32542330). {ECO:0000269|PubMed:32542330, ECO:0000269|PubMed:32669363}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8544|complex.ecocyc.CPLX0-8544]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4280|gene.b4280]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39353`
- `KEGG:ecj:JW5769;eco:b4280;ecoc:C3026_23080;`
- `GeneID:948808;`
- `GO:GO:0000166; GO:0006974; GO:0016836; GO:0019262; GO:0042803`
- `EC:4.2.1.-`

## Notes

2,7-anhydro-N-acetylneuraminate hydratase (EC 4.2.1.-) (EcNanOx)
