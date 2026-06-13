---
entity_id: "complex.ecocyc.CPLX0-8187"
entity_type: "complex"
name: "periplasmic serine endoprotease"
source_database: "EcoCyc"
source_id: "CPLX0-8187"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# periplasmic serine endoprotease

`complex.ecocyc.CPLX0-8187`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8187`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39099|protein.P39099]]

## Enriched Summary

DegQ is a serine endoprotease that may be involved in degrading transiently denatured proteins . E. coli DegQ, DegP and DegS are homologous members of the HtrA (High temperature requirement A) family of proteins. These proteins function as both molecular chaperones and proteases, performing protein quality control in the periplasm by refolding or degrading misfolded proteins . In vivo DegQ was shown to exist primarily as a trimer when it is substrate-free and as a dodecamer when substrate is present . In addition to dodecamers, DegQ can also form tetracosamers (24-mers) in the presence of substrate . However, there is disagreement as to the oligomeric state of DegQ in the absence of substrate. Inactive hexamers rather than trimers were reported by whereas observed only trimers and no hexamers. Evidence for a pH effect on DegQ oligomerization suggests a dynamic, pH-dependent equilibrium . In addition to cryo-electron microscopy structures of DegQ multimers presented by , crystal structures of the DegQ protease domain (PDB 3STI), and the protease and PDZ1 domain (3STJ), have been solved at 2.60 Å resolution . The two PDZ domains appear to be required for chaperone activity . DegQ expression increases during anaerobic growth at pH 8.5 . DegQ is a multi-copy suppressor of prc deficiency...

## Biological Role

Catalyzes RXN0-3182 (reaction.ecocyc.RXN0-3182).

## Annotation

DegQ is a serine endoprotease that may be involved in degrading transiently denatured proteins . E. coli DegQ, DegP and DegS are homologous members of the HtrA (High temperature requirement A) family of proteins. These proteins function as both molecular chaperones and proteases, performing protein quality control in the periplasm by refolding or degrading misfolded proteins . In vivo DegQ was shown to exist primarily as a trimer when it is substrate-free and as a dodecamer when substrate is present . In addition to dodecamers, DegQ can also form tetracosamers (24-mers) in the presence of substrate . However, there is disagreement as to the oligomeric state of DegQ in the absence of substrate. Inactive hexamers rather than trimers were reported by whereas observed only trimers and no hexamers. Evidence for a pH effect on DegQ oligomerization suggests a dynamic, pH-dependent equilibrium . In addition to cryo-electron microscopy structures of DegQ multimers presented by , crystal structures of the DegQ protease domain (PDB 3STI), and the protease and PDZ1 domain (3STJ), have been solved at 2.60 Å resolution . The two PDZ domains appear to be required for chaperone activity . DegQ expression increases during anaerobic growth at pH 8.5 . DegQ is a multi-copy suppressor of prc deficiency . The phenotypes under different growth conditions of a degQ single knockout mutant, and degQ double knockout mutants with the proteases or folding factors ppiD, fkpA, degP, surA, ppiA, dsbA, dsbC, skp, ptrA, tsp (prc), yfgC, ydgD, yggG and ycaL, have been reported . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3182|reaction.ecocyc.RXN0-3182]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P39099|protein.P39099]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## External IDs

- `EcoCyc:CPLX0-8187`

## Notes

12*protein.P39099
