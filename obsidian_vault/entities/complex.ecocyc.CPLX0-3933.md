---
entity_id: "complex.ecocyc.CPLX0-3933"
entity_type: "complex"
name: "outer membrane protein assembly complex"
source_database: "EcoCyc"
source_id: "CPLX0-3933"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Bam complex"
---

# outer membrane protein assembly complex

`complex.ecocyc.CPLX0-3933`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3933`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A937|protein.P0A937]], [[protein.P0A903|protein.P0A903]], [[protein.P0AC02|protein.P0AC02]], [[protein.P0A940|protein.P0A940]], [[protein.P77774|protein.P77774]]

## Enriched Summary

BamABCDE is an outer membrane, multi-protein complex that is responsible for the assembly and insertion of β-barrel proteins into the outer membrane. Following their synthesis in the cytoplasm, unfolded outer membrane proteins (OMPS) are translocated across the inner membrane by the SECE-G-Y-CPLX and delivered to the Bam complex which folds and inserts β-barrels into the outer membrane. The periplasmic chaperones EG10985-MONOMER "SurA", CPLX0-7711 "Skp" and CPLX0-2921 "DegP" prevent misfolding and aggregation of the OMPS as they cross the periplasm. The Bam complex interacts physically with the SEC-SECRETION-CPLX to form a structure that bridges the inner and outer membranes and facilitates delivery and insertion of outer membrane proteins (OMPs); the periplasmic domains of SecD, YidC and SecF extend to interact with the BAM lipoproteins and the proton-translocating activity of SecD is required for efficient OMP insertion (see also ). Immunolabeling experiments suggest that the Bam complex localises in foci along the cell periphery, that it is produced to maintain a constant concentration during the cell cycle and that it interacts with peptidoglycan The Bam complex is implicated in assembly of RCSF-MONOMER RcsF-OMP complexes (see further ). BamA is an OMP; BamB, BamC, BamD and BamE are outer membrane lipoproteins...

## Annotation

BamABCDE is an outer membrane, multi-protein complex that is responsible for the assembly and insertion of β-barrel proteins into the outer membrane. Following their synthesis in the cytoplasm, unfolded outer membrane proteins (OMPS) are translocated across the inner membrane by the SECE-G-Y-CPLX and delivered to the Bam complex which folds and inserts β-barrels into the outer membrane. The periplasmic chaperones EG10985-MONOMER "SurA", CPLX0-7711 "Skp" and CPLX0-2921 "DegP" prevent misfolding and aggregation of the OMPS as they cross the periplasm. The Bam complex interacts physically with the SEC-SECRETION-CPLX to form a structure that bridges the inner and outer membranes and facilitates delivery and insertion of outer membrane proteins (OMPs); the periplasmic domains of SecD, YidC and SecF extend to interact with the BAM lipoproteins and the proton-translocating activity of SecD is required for efficient OMP insertion (see also ). Immunolabeling experiments suggest that the Bam complex localises in foci along the cell periphery, that it is produced to maintain a constant concentration during the cell cycle and that it interacts with peptidoglycan The Bam complex is implicated in assembly of RCSF-MONOMER RcsF-OMP complexes (see further ). BamA is an OMP; BamB, BamC, BamD and BamE are outer membrane lipoproteins. BamA and BamD are essential and depletion of either results in severe outer membrane defects. BamB, BamC and BamE are non-essential and cells lacking these lipoproteins exhibit only minor outer membrane defects . The essentiality of BamD results from its role in preventing BamA 'jamming' by specific substrates such as RCSF-MONOMER RcsF . The relative stoichiometry of the Bam proteins (ABC and D) is believed to be 1:1:1:1 . Membranes from wild-type cells solub

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P0A903|protein.P0A903]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A937|protein.P0A937]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A940|protein.P0A940]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AC02|protein.P0AC02]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77774|protein.P77774]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-3933`
- `PDB:5EKQ`
- `PDB:5D0Q`
- `PDB:5D0O`
- `PDB:5AYW`
- `PDB:5LJO`
- `PDB:6V05`
- `PDB:6SN9`
- `PDB:6LYU`
- `QSPROTEOME:QS00049422`

## Notes

1*protein.P0A937|1*protein.P0A903|1*protein.P0AC02|1*protein.P0A940|1*protein.P77774
