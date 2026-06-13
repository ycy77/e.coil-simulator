---
entity_id: "complex.ecocyc.CPLX0-8556"
entity_type: "complex"
name: "diguanylate cyclase DgcC"
source_database: "EcoCyc"
source_id: "CPLX0-8556"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# diguanylate cyclase DgcC

`complex.ecocyc.CPLX0-8556`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8556`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AAP1|protein.P0AAP1]]

## Enriched Summary

DgcC is an EC-2.7.7.65, that is involved in the regulation of cellulose biosynthesis. Cellulose production is a common trait in wild isolates of E. coli, but not in K-12 strains due to a mutation in EG12261, which encodes a protein that is required for cellulose production . The physical interactions between DgcC, the EG12256-MONOMER "c-di-GMP phosphodiesterase PdeK", and the EG12259-MONOMER "BcsB subunit" of CPLX0-8125 create a local microenvironment where the C-DI-GMP (c-di-GMP) signal is produced and degraded in proximity to its regulatory target, the EG12260-MONOMER "BcsA catalytic subunit" of cellulose synthase, resulting in local c-di-GMP signaling . DgcC has an N-terminal MASE2 (Membrane-Associated SEnsor) domain, which includes six putative membrane segments and is found in proteins associated with signal transduction. The MASE2 domain is followed by the diguanylate cyclase (GGDEF) domain . DgcC interacts with BcsB and PdeK via its MASE2 integral membrane domain . The E. coli K12 genome encodes 12 GGDEF-containing diguanylate cyclases and 13 EAL domain-containing c-di-GMP-specific phosphodiesterases (PDEs). DgcC belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains...

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

DgcC is an EC-2.7.7.65, that is involved in the regulation of cellulose biosynthesis. Cellulose production is a common trait in wild isolates of E. coli, but not in K-12 strains due to a mutation in EG12261, which encodes a protein that is required for cellulose production . The physical interactions between DgcC, the EG12256-MONOMER "c-di-GMP phosphodiesterase PdeK", and the EG12259-MONOMER "BcsB subunit" of CPLX0-8125 create a local microenvironment where the C-DI-GMP (c-di-GMP) signal is produced and degraded in proximity to its regulatory target, the EG12260-MONOMER "BcsA catalytic subunit" of cellulose synthase, resulting in local c-di-GMP signaling . DgcC has an N-terminal MASE2 (Membrane-Associated SEnsor) domain, which includes six putative membrane segments and is found in proteins associated with signal transduction. The MASE2 domain is followed by the diguanylate cyclase (GGDEF) domain . DgcC interacts with BcsB and PdeK via its MASE2 integral membrane domain . The E. coli K12 genome encodes 12 GGDEF-containing diguanylate cyclases and 13 EAL domain-containing c-di-GMP-specific phosphodiesterases (PDEs). DgcC belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . Dimerization via the MASE2 domain appears to be required for catalytic activity of DgcC. To assay diguanylate cyclase activity, the full-length protein was reconstituted in membrane nanodisks . Increased expression of G6546, which encodes a transcriptional activator of curli production, stimulates expression of dgcC . Expression of dgcC is dependent on RPOS-MONOMER and is induced in stationary phase at lower temperatures (28 or 23°C) , although different effects of growth in LB med

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AAP1|protein.P0AAP1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8556`
- `QSPROTEOME:QS00195959`

## Notes

2*protein.P0AAP1
