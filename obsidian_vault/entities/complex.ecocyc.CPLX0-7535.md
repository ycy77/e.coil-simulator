---
entity_id: "complex.ecocyc.CPLX0-7535"
entity_type: "complex"
name: "arginine:agmatine antiporter"
source_database: "EcoCyc"
source_id: "CPLX0-7535"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "AdiC"
---

# arginine:agmatine antiporter

`complex.ecocyc.CPLX0-7535`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7535`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60061|protein.P60061]]

## Enriched Summary

AdiC is the arginine:agmatine antiporter of an arginine-dependent acid resistance (AR) system that contributes to E. coli survival under extreme acid stress (up to pH 2). This system employs the adiA-encoded ARGDECARBOXDEG-CPLX "arginine decarboxylase" and the AdiC antiporter to exchange extracellular arginine for the intracellular product of arginine decarboxylation, agmatine. Protection from acid stress by amino acid-dependent AR systems may occur by two mechanisms: generation of a less acidic cytoplasmic pH as protons are consumed by the decarboxylation reaction plus a short term reversal of transmembrane potential (positive inside) to slow proton movement into the cell (and see ). A ΔadiC strain is defective in arginine-dependent acid resistance and unable to withstand pH 2 acid challenge in the presence of external arginine; measurements of extracellular arginine and agmatine indicate that this strain is unable to exchange extracellular arginine for intracellular agmatine (see also ). adiC expression is induced under anaerobic conditions at low pH ; agmatine extrusion is maximal at pH 2.5, falling below the detection limit at pH 4.0 . Purified AdiC is homodimeric in phospolipid membranes and mediates an electrogenic arginine:agmatine exchange; the protein supports some antiport at neutral pH but has an increased rate at pH 4...

## Biological Role

Catalyzes arginine:agmatine antiport (reaction.ecocyc.RXN0-2162). Transports L-Arginine (molecule.C00062), Agmatine (molecule.C00179).

## Annotation

AdiC is the arginine:agmatine antiporter of an arginine-dependent acid resistance (AR) system that contributes to E. coli survival under extreme acid stress (up to pH 2). This system employs the adiA-encoded ARGDECARBOXDEG-CPLX "arginine decarboxylase" and the AdiC antiporter to exchange extracellular arginine for the intracellular product of arginine decarboxylation, agmatine. Protection from acid stress by amino acid-dependent AR systems may occur by two mechanisms: generation of a less acidic cytoplasmic pH as protons are consumed by the decarboxylation reaction plus a short term reversal of transmembrane potential (positive inside) to slow proton movement into the cell (and see ). A ΔadiC strain is defective in arginine-dependent acid resistance and unable to withstand pH 2 acid challenge in the presence of external arginine; measurements of extracellular arginine and agmatine indicate that this strain is unable to exchange extracellular arginine for intracellular agmatine (see also ). adiC expression is induced under anaerobic conditions at low pH ; agmatine extrusion is maximal at pH 2.5, falling below the detection limit at pH 4.0 . Purified AdiC is homodimeric in phospolipid membranes and mediates an electrogenic arginine:agmatine exchange; the protein supports some antiport at neutral pH but has an increased rate at pH 4 . Assays using tandem constructs of purified wild-type and mutant AdiC monomers suggest that each monomer is independently capable of arginine transport . AdiC preferentially binds the monovalent form of L-arginine (Arg+) over the divalent form (Arg+2) at typical gastric pH . In the Transporter Classification Database AdiC is a member of the Basic Amino Acid/Polyamine Antiporter (APA) family within the Amino Acid-Polyamine-Organocation (APC) Su

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2162|reaction.ecocyc.RXN0-2162]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00179|molecule.C00179]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P60061|protein.P60061]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-7535`
- `QSPROTEOME:QS00203787`

## Notes

2*protein.P60061
