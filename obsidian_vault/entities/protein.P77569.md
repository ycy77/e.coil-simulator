---
entity_id: "protein.P77569"
entity_type: "protein"
name: "mhpR"
source_database: "UniProt"
source_id: "P77569"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mhpR b0346 JW0337"
---

# mhpR

`protein.P77569`

## Static

- Type: `protein`
- Source: `UniProt:P77569`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Activator of the mhpABCDFE operon coding for components of the 3-hydroxyphenylpropionate degradation pathway. {ECO:0000269|PubMed:9098055}.

## Biological Role

Component of DNA-binding transcriptional activator MhpR-3-(3-hydroxyphenyl)propanoate (complex.ecocyc.MONOMER0-1441).

## Annotation

FUNCTION: Activator of the mhpABCDFE operon coding for components of the 3-hydroxyphenylpropionate degradation pathway. {ECO:0000269|PubMed:9098055}.

## Outgoing Edges (7)

- `activates` --> [[gene.b0347|gene.b0347]] `RegulonDB` `C` - regulator=MhpR; target=mhpA; function=+
- `activates` --> [[gene.b0348|gene.b0348]] `RegulonDB` `C` - regulator=MhpR; target=mhpB; function=+
- `activates` --> [[gene.b0349|gene.b0349]] `RegulonDB` `C` - regulator=MhpR; target=mhpC; function=+
- `activates` --> [[gene.b0350|gene.b0350]] `RegulonDB` `C` - regulator=MhpR; target=mhpD; function=+
- `activates` --> [[gene.b0351|gene.b0351]] `RegulonDB` `C` - regulator=MhpR; target=mhpF; function=+
- `activates` --> [[gene.b0352|gene.b0352]] `RegulonDB` `C` - regulator=MhpR; target=mhpE; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-1441|complex.ecocyc.MONOMER0-1441]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b0346|gene.b0346]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77569`
- `KEGG:ecj:JW0337;eco:b0346;ecoc:C3026_01705;ecoc:C3026_24865;`
- `GeneID:945938;`
- `GO:GO:0003677; GO:0003700; GO:0045892`

## Notes

DNA-binding transcriptional activator MhpR (mhp operon transcriptional activator)
