---
entity_id: "protein.P13024"
entity_type: "protein"
name: "fdhE"
source_database: "UniProt"
source_id: "P13024"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdhE b3891 JW3862"
---

# fdhE

`protein.P13024`

## Static

- Type: `protein`
- Source: `UniProt:P13024`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Necessary for formate dehydrogenase activity. FdhE is required for formate dehydrogenase-N enzymatic activity , but not for fdnGHI and fdoGHI transcription. FdhE is not a component of membrane-bound formate dehydrogenase-N itself . FdhE is an iron-binding rubredoxin that interacts with the catalytic molybdoprotein subunits (FdnG, FdoG) of both respiratory formate dehydrogenases, FORMATEDEHYDROGN-CPLX and FORMATEDEHYDROGO-CPLX . FdhE can exist as both a monomer and a homodimer in solution; the dimeric form is stabilized by anaerobiosis. Conserved cysteine residues are involved in ligation of Fe(III) and required for activity of FdhE . Expression of fdhE is sel-dependent and shows Chl- and FNR-dependent nitrate induction .

## Biological Role

Component of formate dehydrogenase formation protein (complex.ecocyc.CPLX0-7724).

## Annotation

FUNCTION: Necessary for formate dehydrogenase activity.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7724|complex.ecocyc.CPLX0-7724]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3891|gene.b3891]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13024`
- `KEGG:ecj:JW3862;eco:b3891;ecoc:C3026_21035;`
- `GeneID:948384;`
- `GO:GO:0005737; GO:0005829; GO:0008199; GO:0042803; GO:0051604`

## Notes

Protein FdhE
