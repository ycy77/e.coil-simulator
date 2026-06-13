---
entity_id: "protein.P76541"
entity_type: "protein"
name: "eutL"
source_database: "UniProt"
source_id: "P76541"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000305|PubMed:19451619, ECO:0000305|PubMed:20044574, ECO:0000305|PubMed:20851901}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eutL yffJ b2439 JW2432"
---

# eutL

`protein.P76541`

## Static

- Type: `protein`
- Source: `UniProt:P76541`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000305|PubMed:19451619, ECO:0000305|PubMed:20044574, ECO:0000305|PubMed:20851901}.

## Enriched Summary

FUNCTION: A component of the bacterial microcompartment (BMC) shell dedicated to ethanolamine degradation (Probable). Two crystal forms have been seen; a form with a closed central pore that has 3 very small (1.1-2.2 Angstroms) channels per trimer lined by acidic and aromatic residues (PubMed:19451619, PubMed:20044574). A form with a large central pore (8-12 Angstroms) has also been seen; this is probably a functional pore which allows molecules to enter and exit the BMC in a selective, gated manner (PubMed:20044574, PubMed:20851901). Another group only sees the central pore in the presence of Zn(2+); soaking crystals in ZnCl(2) leads to dramatic conformational changes that open a central pore of about 12 Angstroms. Whether Zn(2+) binding is physiologically relevant is unclear, however it suggests a gating mechanism exists (PubMed:20851901). Ethanolamine-binding by the small channels has been hypothesized to stabilize the EutL central pore in a closed (non-transporting) state. An open pore is thought to be large enough to transport ATP and/or cobalamin (By similarity). {ECO:0000250|UniProtKB:Q8XLZ0, ECO:0000269|PubMed:19451619, ECO:0000269|PubMed:20044574, ECO:0000269|PubMed:20851901, ECO:0000305|PubMed:19451619, ECO:0000305|PubMed:20044574, ECO:0000305|PubMed:20851901, ECO:0007744|PDB:3GFH, ECO:0007744|PDB:3I82, ECO:0007744|PDB:3MPV}.

## Biological Role

Component of predicted structural protein, ethanolamine utilization microcompartment (complex.ecocyc.CPLX0-7801).

## Annotation

FUNCTION: A component of the bacterial microcompartment (BMC) shell dedicated to ethanolamine degradation (Probable). Two crystal forms have been seen; a form with a closed central pore that has 3 very small (1.1-2.2 Angstroms) channels per trimer lined by acidic and aromatic residues (PubMed:19451619, PubMed:20044574). A form with a large central pore (8-12 Angstroms) has also been seen; this is probably a functional pore which allows molecules to enter and exit the BMC in a selective, gated manner (PubMed:20044574, PubMed:20851901). Another group only sees the central pore in the presence of Zn(2+); soaking crystals in ZnCl(2) leads to dramatic conformational changes that open a central pore of about 12 Angstroms. Whether Zn(2+) binding is physiologically relevant is unclear, however it suggests a gating mechanism exists (PubMed:20851901). Ethanolamine-binding by the small channels has been hypothesized to stabilize the EutL central pore in a closed (non-transporting) state. An open pore is thought to be large enough to transport ATP and/or cobalamin (By similarity). {ECO:0000250|UniProtKB:Q8XLZ0, ECO:0000269|PubMed:19451619, ECO:0000269|PubMed:20044574, ECO:0000269|PubMed:20851901, ECO:0000305|PubMed:19451619, ECO:0000305|PubMed:20044574, ECO:0000305|PubMed:20851901, ECO:0007744|PDB:3GFH, ECO:0007744|PDB:3I82, ECO:0007744|PDB:3MPV}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7801|complex.ecocyc.CPLX0-7801]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2439|gene.b2439]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76541`
- `KEGG:ecj:JW2432;eco:b2439;ecoc:C3026_13545;`
- `GeneID:946914;`
- `GO:GO:0005198; GO:0008270; GO:0031471; GO:0042802; GO:0046336`

## Notes

Bacterial microcompartment shell protein EutL (BMC-T) (Ethanolamine utilization protein EutL)
