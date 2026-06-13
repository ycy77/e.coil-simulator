---
entity_id: "complex.ecocyc.CPLX0-8104"
entity_type: "complex"
name: "methyl-accepting chemotaxis protein - dipeptide-sensing"
source_database: "EcoCyc"
source_id: "CPLX0-8104"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methyl-accepting chemotaxis protein - dipeptide-sensing

`complex.ecocyc.CPLX0-8104`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8104`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07018|protein.P07018]]

## Enriched Summary

The tap gene product is one of four methyl-accepting chemotaxis proteins (MCPs) in E. coli K-12 (EG11034 Tsr, EG10988 Tar, EG11018 Trg, and EG10987 Tap). Tap, also known as MCP-IV, interacts with the the periplasmic dipeptide-binding protein EG10248 DppA to mediate taxis toward dipeptides. Dipeptides are good attractants, tripeptides are poor attractants. Peptides containing D-amino acids are poor attractants . E. coli Tap is predicted to be a homodimeric inner membrane protein; the Tap monomer consists of a periplasmic, ligand-sensing domain, two trans-membrane segments (TM1 and TM2) and a cytoplasmic signaling domain containing putative methylation sites . Methylation and demethylation of MCPs in E. coli K-12 is catalysed by the CHER-MONOMER CheR methyltransferase and the CHEB-MONOMER CheB methylesterase. The cytoplasmic domains of the four E. coli MCPs have a high degree of sequence similarity . Tap contains a HAMP domain (present in histidine kinases, adenylate cyclases, methyl accepting chemotaxis proteins, phosphatases) which is located between the transmembrane region of the molecule and the cytoplasmic signalling region. HAMP domains are thought to mediate input/ouptut signaling (reviewed in . E. coli Tap is predicted to form a ternary complex with the histidine autokinase CHEA-CPLX CheA and the coupling protein CHEW-MONOMER CheW...

## Biological Role

Component of chemotaxis signaling complex core unit - dipeptide sensing (complex.ecocyc.TAP-CPLX).

## Annotation

The tap gene product is one of four methyl-accepting chemotaxis proteins (MCPs) in E. coli K-12 (EG11034 Tsr, EG10988 Tar, EG11018 Trg, and EG10987 Tap). Tap, also known as MCP-IV, interacts with the the periplasmic dipeptide-binding protein EG10248 DppA to mediate taxis toward dipeptides. Dipeptides are good attractants, tripeptides are poor attractants. Peptides containing D-amino acids are poor attractants . E. coli Tap is predicted to be a homodimeric inner membrane protein; the Tap monomer consists of a periplasmic, ligand-sensing domain, two trans-membrane segments (TM1 and TM2) and a cytoplasmic signaling domain containing putative methylation sites . Methylation and demethylation of MCPs in E. coli K-12 is catalysed by the CHER-MONOMER CheR methyltransferase and the CHEB-MONOMER CheB methylesterase. The cytoplasmic domains of the four E. coli MCPs have a high degree of sequence similarity . Tap contains a HAMP domain (present in histidine kinases, adenylate cyclases, methyl accepting chemotaxis proteins, phosphatases) which is located between the transmembrane region of the molecule and the cytoplasmic signalling region. HAMP domains are thought to mediate input/ouptut signaling (reviewed in . E. coli Tap is predicted to form a ternary complex with the histidine autokinase CHEA-CPLX CheA and the coupling protein CHEW-MONOMER CheW. Tap and CPLX0-8105 Trg are considered to be low-abundance receptors while CPLX0-8103 Tsr and CPLX0-8102 Tar are considered to be high-abundance . Overexpression of tap from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid . tap: taxis associated protein

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TAP-CPLX|complex.ecocyc.TAP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07018|protein.P07018]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8104`
- `QSPROTEOME:QS00049367`

## Notes

2*protein.P07018
