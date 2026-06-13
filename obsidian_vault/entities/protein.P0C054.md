---
entity_id: "protein.P0C054"
entity_type: "protein"
name: "ibpA"
source_database: "UniProt"
source_id: "P0C054"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:14702418}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ibpA hslT htpN b3687 JW3664"
---

# ibpA

`protein.P0C054`

## Static

- Type: `protein`
- Source: `UniProt:P0C054`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:14702418}.

## Enriched Summary

FUNCTION: Associates with aggregated proteins, together with IbpB, to stabilize and protect them from irreversible denaturation and extensive proteolysis during heat shock and oxidative stress. Aggregated proteins bound to the IbpAB complex are more efficiently refolded and reactivated by the ATP-dependent chaperone systems ClpB and DnaK/DnaJ/GrpE. Its activity is ATP-independent. {ECO:0000269|PubMed:12055295, ECO:0000269|PubMed:12071954}.

## Biological Role

Component of small heat shock protein IbpA (complex.ecocyc.CPLX0-8108).

## Annotation

FUNCTION: Associates with aggregated proteins, together with IbpB, to stabilize and protect them from irreversible denaturation and extensive proteolysis during heat shock and oxidative stress. Aggregated proteins bound to the IbpAB complex are more efficiently refolded and reactivated by the ATP-dependent chaperone systems ClpB and DnaK/DnaJ/GrpE. Its activity is ATP-independent. {ECO:0000269|PubMed:12055295, ECO:0000269|PubMed:12071954}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8108|complex.ecocyc.CPLX0-8108]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b3687|gene.b3687]] `RegulonDB` `S` - regulator=small heat shock protein IbpA; target=ibpA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3687|gene.b3687]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C054`
- `KEGG:ecj:JW3664;eco:b3687;ecoc:C3026_19990;`
- `GeneID:86861802;93778428;948200;`
- `GO:GO:0005737; GO:0005829; GO:0009408; GO:0017148; GO:0042802; GO:0042803; GO:0048027; GO:0050821`

## Notes

Small heat shock protein IbpA (16 kDa heat shock protein A)
