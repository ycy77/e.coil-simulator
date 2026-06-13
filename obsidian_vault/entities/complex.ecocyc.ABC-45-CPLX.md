---
entity_id: "complex.ecocyc.ABC-45-CPLX"
entity_type: "complex"
name: "intermembrane phospholipid transport system"
source_database: "EcoCyc"
source_id: "ABC-45-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# intermembrane phospholipid transport system

`complex.ecocyc.ABC-45-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-45-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P64602|protein.P64602]], [[protein.P64604|protein.P64604]], [[protein.P64606|protein.P64606]], [[protein.P63386|protein.P63386]]

## Enriched Summary

The MlaFEDB complex is an atypical member of the ATP-binding cassette (ABC) superfamily of transporters. MlaFEDB, G7216-MONOMER "MlaA" (an outer membrane lipoprotein) and G7659-MONOMER "MlaC", (a periplasmic chaperone), are implicated in a phospholipid transport pathway that is thought to maintain outer membrane lipid asymmetry by removing phospholipids from the outer membrane and transporting them back to the inner membrane . Evidence for a role in anterograde phospholipid movement has also been reported . MlaE is the predicted permease subunit and MlaF the predicted ATP binding subunit; MlaD is a periplasmic facing inner membrane protein that binds phospholids and MlaB is a cytoplasmic protein necessary for assembly and activity of the complex . MlaF, MlaE, MalD and MlaB interact to from a stable complex; MlaD exists as a hexamer in the complex (and further ). Cryo-EM structures of the complex in various states have been determined ATP-dependent retrograde phospholipid transport has been reconstituted in vitro using MlaA-OmpF outer membrane proteoliposomes, MlaFEDB inner membrane proteoliposomes and purified MlaC . MlaC transfers phospholipids to nanodisc-embedded MlaFEDB in an MlaD- and ATP-dependent manner; ATP hydrolysis is strongly coupled to retrograde phospholipid transport and prevents phospholipid transfer from MlaFEDB to MlaC...

## Annotation

The MlaFEDB complex is an atypical member of the ATP-binding cassette (ABC) superfamily of transporters. MlaFEDB, G7216-MONOMER "MlaA" (an outer membrane lipoprotein) and G7659-MONOMER "MlaC", (a periplasmic chaperone), are implicated in a phospholipid transport pathway that is thought to maintain outer membrane lipid asymmetry by removing phospholipids from the outer membrane and transporting them back to the inner membrane . Evidence for a role in anterograde phospholipid movement has also been reported . MlaE is the predicted permease subunit and MlaF the predicted ATP binding subunit; MlaD is a periplasmic facing inner membrane protein that binds phospholids and MlaB is a cytoplasmic protein necessary for assembly and activity of the complex . MlaF, MlaE, MalD and MlaB interact to from a stable complex; MlaD exists as a hexamer in the complex (and further ). Cryo-EM structures of the complex in various states have been determined ATP-dependent retrograde phospholipid transport has been reconstituted in vitro using MlaA-OmpF outer membrane proteoliposomes, MlaFEDB inner membrane proteoliposomes and purified MlaC . MlaC transfers phospholipids to nanodisc-embedded MlaFEDB in an MlaD- and ATP-dependent manner; ATP hydrolysis is strongly coupled to retrograde phospholipid transport and prevents phospholipid transfer from MlaFEDB to MlaC . Mechanistic insight into phospholipid transfer between MlaC and MlaD is reported by . Single deletion mutations in each of the mla genes (ΔmlaF/E/D/C/B/A) results in permeability defects of the outer membrane; the mutant strains show no defects in LPS or outer membrane protein levels but do have increased sensitivity to SDS-EDTA; this phenotype can be suppressed by an increase in EG10738 "pldA" transcription . A ΔmlaC mutant has increa

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P63386|protein.P63386]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P64602|protein.P64602]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P64604|protein.P64604]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P64606|protein.P64606]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ABC-45-CPLX`
- `PDB:7CH0`
- `PDB:7CGN`
- `PDB:7CGE`
- `PDB:6XGZ`
- `PDB:7CH7`
- `PDB:7CH6`
- `PDB:6ZY9`
- `PDB:7CJ0`
- `QSPROTEOME:QS00183217`

## Notes

2*protein.P64602|6*protein.P64604|2*protein.P64606|2*protein.P63386
