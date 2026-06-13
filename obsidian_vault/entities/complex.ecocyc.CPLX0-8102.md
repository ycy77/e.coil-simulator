---
entity_id: "complex.ecocyc.CPLX0-8102"
entity_type: "complex"
name: "methyl-accepting chemotaxis protein Tar"
source_database: "EcoCyc"
source_id: "CPLX0-8102"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methyl-accepting chemotaxis protein Tar

`complex.ecocyc.CPLX0-8102`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8102`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07017|protein.P07017]]

## Enriched Summary

The tar gene product is one of four methyl-accepting chemotaxis proteins (MCPs) in E. coli K-12 (EG11034 Tsr, EG10988 Tar, EG11018 Trg, and EG10987 Tap). Tar, also known as MCP-II, is the receptor for the attractants aspartate and maltose and the repellents nickel and cobalt . Tar is the primary receptor for the amino acids aspartate, asparagine and glutamate; in strains lacking the Tsr receptor, Tar can mediate a chemotactic response to serine, cysteine, glycine, alanine and asparagine . Tar is responsible for mediating an attractant response to phenol and Tsr and Tar mediate the chemotactic response to pH . E. coli Tar is a homodimeric inner membrane protein; the Tar monomer consists of a periplasmic, ligand-sensing domain, two trans-membrane segments (TM1 and TM2) and a cytoplasmic signaling domain which is predominantly alpha-helical in structure and is predicted to contain 4 methylation sites . The cytoplasmic domain of Tar is subject to methylation and demethylation at the carboxyl groups of glutamic acid residues . Methylation and demethylation of MCPs in E. coli K-12 is catalysed by the CHER-MONOMER "CheR methyltransferase" and the CHEB-MONOMER "CheB methylesterase". Aspartate binds directly to the Tar receptor whereas maltose detection is mediated via the MALE-MONOMER "periplasmic maltose binding protein"...

## Biological Role

Component of chemotaxis signaling complex core unit - aspartate sensing (complex.ecocyc.TAR-CPLX).

## Annotation

The tar gene product is one of four methyl-accepting chemotaxis proteins (MCPs) in E. coli K-12 (EG11034 Tsr, EG10988 Tar, EG11018 Trg, and EG10987 Tap). Tar, also known as MCP-II, is the receptor for the attractants aspartate and maltose and the repellents nickel and cobalt . Tar is the primary receptor for the amino acids aspartate, asparagine and glutamate; in strains lacking the Tsr receptor, Tar can mediate a chemotactic response to serine, cysteine, glycine, alanine and asparagine . Tar is responsible for mediating an attractant response to phenol and Tsr and Tar mediate the chemotactic response to pH . E. coli Tar is a homodimeric inner membrane protein; the Tar monomer consists of a periplasmic, ligand-sensing domain, two trans-membrane segments (TM1 and TM2) and a cytoplasmic signaling domain which is predominantly alpha-helical in structure and is predicted to contain 4 methylation sites . The cytoplasmic domain of Tar is subject to methylation and demethylation at the carboxyl groups of glutamic acid residues . Methylation and demethylation of MCPs in E. coli K-12 is catalysed by the CHER-MONOMER "CheR methyltransferase" and the CHEB-MONOMER "CheB methylesterase". Aspartate binds directly to the Tar receptor whereas maltose detection is mediated via the MALE-MONOMER "periplasmic maltose binding protein" . Aspartate binding to a purified Tar receptor generates a downward piston motion of TM1 relative to TM2 The cytoplasmic domains of the four E. coli MCPs have a high degree of sequence similarity . Tar contains a HAMP domain (present in histidine kinases, adenylate cyclases, methyl accepting chemotaxis proteins, phosphatases) which is located between the transmembrane region of the molecule and the cytoplasmic signalling region. Tsr HAMP domains have been show

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TAR-CPLX|complex.ecocyc.TAR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07017|protein.P07017]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8102`
- `QSPROTEOME:QS00049368`

## Notes

2*protein.P07017
