---
entity_id: "complex.ecocyc.CPLX0-2921"
entity_type: "complex"
name: "periplasmic serine endoprotease DegP"
source_database: "EcoCyc"
source_id: "CPLX0-2921"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN|CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# periplasmic serine endoprotease DegP

`complex.ecocyc.CPLX0-2921`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2921`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN|CCI-PERI-BAC-GN
- Complex type: `structural`
- Components: [[protein.P0C0V0|protein.P0C0V0]]

## Enriched Summary

Protease Do, or DegP, is a periplasmic serine protease required for survival at high temperatures . DegP degrades abnormal proteins in the periplasm, including mutant proteins (hybrid proteins, unstable MalE mutant proteins), oxidatively damaged proteins and aggregated proteins . DegP degrades misfolded MalS and misfolded pilus subunits as well as unassembled subunits from protein complexes including HflK and LamB . DegP degrades mutant EG11569-MONOMER "LptD" (LptDY721D) that is not competent for Bam-mediated assembly; the periplasmic proteases DegP, G6470-MONOMER "YcaL" and G7311-MONOMER "BepA" degrade stalled LptD substrate at different stages in the OMP assembly process . DegP functions primarily as a protease for OMP biogenesis (see also ). DegP binds to the EG30100 "ssrA"-encoded degradation tag, though this PDZ-domain-mediated interaction does not appear to allow DegP proteolysis of tagged proteins ; the ssrA protease recognition tag increases the sequestration of unfolded substrate by DegP . Strains lacking DegP are more susceptible to the cationic antimicrobial peptide Lactoferricin B, indicating a possible role for DegP in degradation of that molecule . DegP degrades the DNA methyltransferase Ada, in vitro...

## Biological Role

Catalyzes 3.4.21.107-RXN (reaction.ecocyc.3.4.21.107-RXN).

## Annotation

Protease Do, or DegP, is a periplasmic serine protease required for survival at high temperatures . DegP degrades abnormal proteins in the periplasm, including mutant proteins (hybrid proteins, unstable MalE mutant proteins), oxidatively damaged proteins and aggregated proteins . DegP degrades misfolded MalS and misfolded pilus subunits as well as unassembled subunits from protein complexes including HflK and LamB . DegP degrades mutant EG11569-MONOMER "LptD" (LptDY721D) that is not competent for Bam-mediated assembly; the periplasmic proteases DegP, G6470-MONOMER "YcaL" and G7311-MONOMER "BepA" degrade stalled LptD substrate at different stages in the OMP assembly process . DegP functions primarily as a protease for OMP biogenesis (see also ). DegP binds to the EG30100 "ssrA"-encoded degradation tag, though this PDZ-domain-mediated interaction does not appear to allow DegP proteolysis of tagged proteins ; the ssrA protease recognition tag increases the sequestration of unfolded substrate by DegP . Strains lacking DegP are more susceptible to the cationic antimicrobial peptide Lactoferricin B, indicating a possible role for DegP in degradation of that molecule . DegP degrades the DNA methyltransferase Ada, in vitro . Differences in the reported localization of DegP may be due to variation in the methods for preparing cell fractions; DegP is not released from osmotic-shocked cells but is recovered in the periplasmic fraction after spheroplast preparation . DegP has an independent chaperone activity that functions even in proteolytically inactive mutants of DegP . DegP's proteolytic activity is increased at high temperatures but drops dramatically at low temperatures, leaving its chaperone function unaffected . DegP interacts with phosphatidylglycerol on the periplasmic f

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.107-RXN|reaction.ecocyc.3.4.21.107-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0C0V0|protein.P0C0V0]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## External IDs

- `EcoCyc:CPLX0-2921`
- `PDB:8F0U`
- `PDB:8F26`
- `PDB:8F21`
- `PDB:8F1U`
- `PDB:8F1T`
- `PDB:8F0A`
- `PDB:3STI`
- `PDB:3STJ`

## Notes

12*protein.P0C0V0
