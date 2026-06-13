---
entity_id: "complex.ecocyc.CPLX0-2502"
entity_type: "complex"
name: "molybdopterin synthase"
source_database: "EcoCyc"
source_id: "CPLX0-2502"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MPT synthase"
---

# molybdopterin synthase

`complex.ecocyc.CPLX0-2502`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2502`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P30748|protein.P30748]], [[protein.P30749|protein.P30749]]

## Enriched Summary

Molybdopterin synthase complex (MPT synthase) catalyzes the conversion of cyclic pyranopterin phosphate (cPTP) to molybdopterin (MPT) in the PWY-6823, which involves incorporation of two sulfur atoms into cPTP at the C1' and C2' positions. G7325-MONOMER receives the initial sulfur from L-cysteine with L-alanine being the by-product . The MoaD sulfur carrier subunit of the MPT synthase must be thiocarboxylated before it is considered active; this occurs while attached to MoeB. Once it is active, it receives a thiol group from either EG12216-MONOMER or G6952-MONOMER (YnjE), which have received the thiol group from IscS . The MoaD subunit then associates with MoaE to form MPT synthase and transfers the sulfur atoms to cPTP, as measured in E. coli strain ER2566 . In its active form, MPT synthase carries a sulfur atom on the C-terminal glycine residue of each of its small MoaD subunits. The crystal structure of the heterotetrameric molybdopterin synthase complex has been determined at 1.45 Å resolution and 1.9 Å resolution . Within the complex the MoaE subunits form a central dimer and the MoaD subunits are located at the opposite ends of the dimer . The active site of MPT synthase has the C terminus of each MoaD subunit inserted into a MoaE subunit . The stoichiometry of the subunits was determined...

## Biological Role

Catalyzes RXN-8342 (reaction.ecocyc.RXN-8342).

## Annotation

Molybdopterin synthase complex (MPT synthase) catalyzes the conversion of cyclic pyranopterin phosphate (cPTP) to molybdopterin (MPT) in the PWY-6823, which involves incorporation of two sulfur atoms into cPTP at the C1' and C2' positions. G7325-MONOMER receives the initial sulfur from L-cysteine with L-alanine being the by-product . The MoaD sulfur carrier subunit of the MPT synthase must be thiocarboxylated before it is considered active; this occurs while attached to MoeB. Once it is active, it receives a thiol group from either EG12216-MONOMER or G6952-MONOMER (YnjE), which have received the thiol group from IscS . The MoaD subunit then associates with MoaE to form MPT synthase and transfers the sulfur atoms to cPTP, as measured in E. coli strain ER2566 . In its active form, MPT synthase carries a sulfur atom on the C-terminal glycine residue of each of its small MoaD subunits. The crystal structure of the heterotetrameric molybdopterin synthase complex has been determined at 1.45 Å resolution and 1.9 Å resolution . Within the complex the MoaE subunits form a central dimer and the MoaD subunits are located at the opposite ends of the dimer . The active site of MPT synthase has the C terminus of each MoaD subunit inserted into a MoaE subunit . The stoichiometry of the subunits was determined . Thermodynamics of protein folding and binding efficiency of subunits have been measured . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-8342|reaction.ecocyc.RXN-8342]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P30748|protein.P30748]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P30749|protein.P30749]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-2502`
- `PDB:3BII`
- `PDB:1NVI`
- `PDB:1FMA`
- `PDB:1FM0`
- `QSPROTEOME:QS00177495`

## Notes

2*protein.P30748|2*protein.P30749
