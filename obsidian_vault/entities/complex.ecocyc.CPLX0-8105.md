---
entity_id: "complex.ecocyc.CPLX0-8105"
entity_type: "complex"
name: "methyl-accepting chemotaxis protein Trg - ribose/galactose/glucose-sensing"
source_database: "EcoCyc"
source_id: "CPLX0-8105"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methyl-accepting chemotaxis protein Trg - ribose/galactose/glucose-sensing

`complex.ecocyc.CPLX0-8105`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8105`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05704|protein.P05704]]

## Enriched Summary

The trg gene product is one of four methyl-accepting chemotaxis proteins (MCPs) in E. coli (EG11034 Tsr, EG10988 Tar, EG11018 Trg, and EG10987 Tap). Trg, also known as MCP-III, is the receptor for the attractants ribose and galactose. MCP-III interacts with the periplasmic ribose- or galactose-binding proteins to mediate taxis to these attractants . It is also thermosensitive . trg expressed from a plasmid in an E. coli strain lacking all four MCPs, mediates a repellent response to phenol . Trg mediates the chemotactic response to FRUCTOSELYSINE fructoselysine . E. coli Trg is a homodimeric inner membrane protein; the Trg monomer consists of a periplasmic, ligand-sensing domain, two trans-membrane segments (TM1 and TM2) and a cytoplasmic signaling domain predicted to contain 5 methylation sites . Methylation and demethylation of MCPs in E. coli K-12 is catalysed by the CHER-MONOMER "CheR methyltransferase" and the CHEB-MONOMER "CheB methylesterase". Two methyl accepting residues arise from CheB catalysed post-translational deamidation of glutamines to yield glutamates . The cytoplasmic domains of the four E. coli MCPs have a high degree of sequence similarity...

## Biological Role

Component of chemotaxis signaling complex core unit - ribose/galactose/glucose sensing (complex.ecocyc.TRG-CPLX).

## Annotation

The trg gene product is one of four methyl-accepting chemotaxis proteins (MCPs) in E. coli (EG11034 Tsr, EG10988 Tar, EG11018 Trg, and EG10987 Tap). Trg, also known as MCP-III, is the receptor for the attractants ribose and galactose. MCP-III interacts with the periplasmic ribose- or galactose-binding proteins to mediate taxis to these attractants . It is also thermosensitive . trg expressed from a plasmid in an E. coli strain lacking all four MCPs, mediates a repellent response to phenol . Trg mediates the chemotactic response to FRUCTOSELYSINE fructoselysine . E. coli Trg is a homodimeric inner membrane protein; the Trg monomer consists of a periplasmic, ligand-sensing domain, two trans-membrane segments (TM1 and TM2) and a cytoplasmic signaling domain predicted to contain 5 methylation sites . Methylation and demethylation of MCPs in E. coli K-12 is catalysed by the CHER-MONOMER "CheR methyltransferase" and the CHEB-MONOMER "CheB methylesterase". Two methyl accepting residues arise from CheB catalysed post-translational deamidation of glutamines to yield glutamates . The cytoplasmic domains of the four E. coli MCPs have a high degree of sequence similarity .Trg contains a HAMP domain (present in histidine kinases, adenylate cyclases, methyl accepting chemotaxis proteins, phosphatases) which is located between the transmembrane region of the molecule and the cytoplasmic signalling region. HAMP domains are thought to mediate input/ouptut signaling (reviewed in . Trg and CPLX0-8104 "Tap" are considered to be low-abundance receptors while CPLX0-8103 "Tsr" and CPLX0-8102 "Tar" are considered to be high-abundance . trg: taxis to ribose and galactose

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRG-CPLX|complex.ecocyc.TRG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P05704|protein.P05704]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8105`
- `QSPROTEOME:QS00049365`

## Notes

2*protein.P05704
