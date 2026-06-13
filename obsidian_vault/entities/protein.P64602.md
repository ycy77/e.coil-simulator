---
entity_id: "protein.P64602"
entity_type: "protein"
name: "mlaB"
source_database: "UniProt"
source_id: "P64602"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:19383799}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mlaB yrbB b3191 JW5535"
---

# mlaB

`protein.P64602`

## Static

- Type: `protein`
- Source: `UniProt:P64602`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:19383799}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane (PubMed:19383799, PubMed:27529189). MlaB plays critical roles in both the assembly and activity of the complex. May act by modulating MlaF structure and stability (PubMed:27529189). {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}. mlaB encodes a cytoplasmic subunit of the MlaFEDB transporter complex which functions as part of a retrograde and/or anterograde intermembrane phospholipid trafficking system. MlaB is implicated in a retrograde phospholipid trafficking pathway; MlaB is a predicted cytoplasmic protein with a STAS domain . MlaB forms a stable complex with MlaF, MlaE and MlaD; MlaB is required for the stability and/or assembly of the complex; an MlaFEB complex containing an MlaB variant with a mutation in the STAS domain (MlaBT52A) has no intrinsic ATPase activity in vitro . Purified, recombinant MlaFB (expressed from a single transcript) forms a complex with 1:1 stoichiometry and structures of both MlaF1B1 - the inactive 'half-transporter' - and MlaF2B2 - the fully assembled complex - have been solved...

## Biological Role

Component of intermembrane phospholipid transport system (complex.ecocyc.ABC-45-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane (PubMed:19383799, PubMed:27529189). MlaB plays critical roles in both the assembly and activity of the complex. May act by modulating MlaF structure and stability (PubMed:27529189). {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-45-CPLX|complex.ecocyc.ABC-45-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3191|gene.b3191]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64602`
- `KEGG:ecj:JW5535;eco:b3191;`
- `GeneID:93778790;947954;`
- `GO:GO:0005829; GO:0006974; GO:0015914; GO:0016020; GO:0046677; GO:0120010; GO:0120014; GO:1990531`

## Notes

Intermembrane phospholipid transport system binding protein MlaB
