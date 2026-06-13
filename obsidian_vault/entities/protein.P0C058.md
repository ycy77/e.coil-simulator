---
entity_id: "protein.P0C058"
entity_type: "protein"
name: "ibpB"
source_database: "UniProt"
source_id: "P0C058"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:14702418}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ibpB hslS htpE b3686 JW3663"
---

# ibpB

`protein.P0C058`

## Static

- Type: `protein`
- Source: `UniProt:P0C058`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:14702418}.

## Enriched Summary

FUNCTION: Associates with aggregated proteins, together with IbpA, to stabilize and protect them from irreversible denaturation and extensive proteolysis during heat shock and oxidative stress. Aggregated proteins bound to the IbpAB complex are more efficiently refolded and reactivated by the ATP-dependent chaperone systems ClpB and DnaK/DnaJ/GrpE. Its activity is ATP-independent. {ECO:0000269|PubMed:12055295, ECO:0000269|PubMed:12071954, ECO:0000269|PubMed:9556585}.

## Biological Role

Component of small heat shock protein IbpB (complex.ecocyc.CPLX0-8107).

## Annotation

FUNCTION: Associates with aggregated proteins, together with IbpA, to stabilize and protect them from irreversible denaturation and extensive proteolysis during heat shock and oxidative stress. Aggregated proteins bound to the IbpAB complex are more efficiently refolded and reactivated by the ATP-dependent chaperone systems ClpB and DnaK/DnaJ/GrpE. Its activity is ATP-independent. {ECO:0000269|PubMed:12055295, ECO:0000269|PubMed:12071954, ECO:0000269|PubMed:9556585}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8107|complex.ecocyc.CPLX0-8107]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3686|gene.b3686]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C058`
- `KEGG:ecj:JW3663;eco:b3686;ecoc:C3026_19985;`
- `GeneID:86861801;93778427;948192;`
- `GO:GO:0005737; GO:0009408; GO:0042802; GO:0050821; GO:1990169`

## Notes

Small heat shock protein IbpB (16 kDa heat shock protein B)
