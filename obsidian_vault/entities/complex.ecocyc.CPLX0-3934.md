---
entity_id: "complex.ecocyc.CPLX0-3934"
entity_type: "complex"
name: "GroEL-GroES chaperonin complex"
source_database: "EcoCyc"
source_id: "CPLX0-3934"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GroE"
---

# GroEL-GroES chaperonin complex

`complex.ecocyc.CPLX0-3934`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3934`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6F5|protein.P0A6F5]], [[protein.P0A6F9|protein.P0A6F9]]

## Enriched Summary

The Escherichia coli chaperonin protein GroEL and its co-chaperonin GroES mediate the ATP dependent folding of newly translated proteins . The crystal structure of GroEL has been determined to a resolution of 2.8 Å. GroEL forms an 800 kDa cylinder from two back-to-back heptameric rings of 57 kDa subunits - the GroEL double toroid. X-ray crystallography to a resolution of 3.0 Å has determined the structure of GroEL-GroES complexed with seven ADP molecules. GroES forms a heptamer of 10 kDa subunits which can bind to either end of the GroEL complex, forming a lid on the chamber . Binding of GroES creates a large dome-shaped cavity with a highly polar inner surface in which a non-native protein has the opportunity to fold into its native form . GroEL-ES is an active chaperonin (reviewed by ). Accelerated folding is due to physical confinement of substrate and a reduction in polypeptide chain entropy in the net negatively charged chaperonin cavity . GroEL-ES accelerates the folding of double-mutant maltose binding protein 8-fold relative to it's spontaneous folding rate. A GroEL-ES mutant in which the net negative charge of the cavity wall is removed functions as a passive folding environment . GroEL-ES is a passive chaperonin which acts to confine the polypeptide chain and prevent multimolecular aggregation (and reviewed by )...

## Biological Role

Catalyzes RXN0-1061 (reaction.ecocyc.RXN0-1061).

## Annotation

The Escherichia coli chaperonin protein GroEL and its co-chaperonin GroES mediate the ATP dependent folding of newly translated proteins . The crystal structure of GroEL has been determined to a resolution of 2.8 Å. GroEL forms an 800 kDa cylinder from two back-to-back heptameric rings of 57 kDa subunits - the GroEL double toroid. X-ray crystallography to a resolution of 3.0 Å has determined the structure of GroEL-GroES complexed with seven ADP molecules. GroES forms a heptamer of 10 kDa subunits which can bind to either end of the GroEL complex, forming a lid on the chamber . Binding of GroES creates a large dome-shaped cavity with a highly polar inner surface in which a non-native protein has the opportunity to fold into its native form . GroEL-ES is an active chaperonin (reviewed by ). Accelerated folding is due to physical confinement of substrate and a reduction in polypeptide chain entropy in the net negatively charged chaperonin cavity . GroEL-ES accelerates the folding of double-mutant maltose binding protein 8-fold relative to it's spontaneous folding rate. A GroEL-ES mutant in which the net negative charge of the cavity wall is removed functions as a passive folding environment . GroEL-ES is a passive chaperonin which acts to confine the polypeptide chain and prevent multimolecular aggregation (and reviewed by ). GroEL-ES activity can be described by an iterative annealing model whereby GroEL repeatedly unfolds and refolds misfolded polypeptides (and see comment by ). GroEL-GroES functions to release proteins from 'kinetic traps' and place them under conditions that favour productive protein folding . In vitro studies into the refolding of a reporter modified protein substrate (MrcB) suggest that GroES may bind substrate and act as an 'unfoldase' before delive

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1061|reaction.ecocyc.RXN0-1061]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0A6F5|protein.P0A6F5]] `EcoCyc` `database` - EcoCyc component coefficient=14 | EcoCyc protcplxs.col coefficient=14
- `is_component_of` <-- [[protein.P0A6F9|protein.P0A6F9]] `EcoCyc` `database` - EcoCyc component coefficient=14 | EcoCyc protcplxs.col coefficient=14

## External IDs

- `EcoCyc:CPLX0-3934`
- `PDB:1AON`
- `PDB:1PF9`
- `PDB:2C7D`
- `PDB:2C7C`
- `PDB:1SX4`
- `PDB:1SVT`
- `PDB:1PCQ`
- `PDB:1GRU`

## Notes

14*protein.P0A6F5|14*protein.P0A6F9
