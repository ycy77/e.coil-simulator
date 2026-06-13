---
entity_id: "protein.P64604"
entity_type: "protein"
name: "mlaD"
source_database: "UniProt"
source_id: "P64604"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:19383799}; Single-pass type II membrane protein {ECO:0000305|PubMed:19383799}; Periplasmic side {ECO:0000305|PubMed:19383799}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mlaD yrbD b3193 JW3160"
---

# mlaD

`protein.P64604`

## Static

- Type: `protein`
- Source: `UniProt:P64604`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:19383799}; Single-pass type II membrane protein {ECO:0000305|PubMed:19383799}; Periplasmic side {ECO:0000305|PubMed:19383799}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane (PubMed:19383799, PubMed:27529189). MlaD functions in substrate binding with strong affinity for phospholipids and modulates ATP hydrolytic activity of the complex (PubMed:27529189). {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}. mlaD encodes an inner membrane anchored subunit of the MlaFEDB transporter complex which functions as part of a retrograde and/or anterograde intermembrane phospholipid trafficking system. MlaD is implicated in a retrograde phospholipid trafficking pathway; a ΔmlaD mutant displays increased SDS-EDTA sensitivity . MlaD is predicted to be a periplasmic facing, inner membrane protein . MlaD is a member of the mammalian cell entry (MCE) family of proteins; MlaD consists of a predicted membrane-anchoring N-terminal α-helix, followed by an MCE domain and a C-terminal α-helical domain, both located in the periplasm . MlaD forms a stable complex with MlaF, MlaE and MlaB; MlaD exists as an oligomer in the complex; the periplasmic, substrate binding domain of MlaD (sMlaD) forms hexamers in vitro; hexameric sMlaD binds phospholipids (phosphatidylglycerol and phosphatidylethanolamine)...

## Biological Role

Component of intermembrane phospholipid transport system (complex.ecocyc.ABC-45-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane (PubMed:19383799, PubMed:27529189). MlaD functions in substrate binding with strong affinity for phospholipids and modulates ATP hydrolytic activity of the complex (PubMed:27529189). {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-45-CPLX|complex.ecocyc.ABC-45-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3193|gene.b3193]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64604`
- `KEGG:ecj:JW3160;eco:b3193;ecoc:C3026_17380;`
- `GeneID:93778788;947712;`
- `GO:GO:0005543; GO:0005886; GO:0015914; GO:0016020; GO:0120010; GO:0120014; GO:1990531`

## Notes

Intermembrane phospholipid transport system binding protein MlaD
