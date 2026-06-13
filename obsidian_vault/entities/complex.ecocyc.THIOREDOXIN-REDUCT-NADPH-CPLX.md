---
entity_id: "complex.ecocyc.THIOREDOXIN-REDUCT-NADPH-CPLX"
entity_type: "complex"
name: "thioredoxin reductase"
source_database: "EcoCyc"
source_id: "THIOREDOXIN-REDUCT-NADPH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# thioredoxin reductase

`complex.ecocyc.THIOREDOXIN-REDUCT-NADPH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:THIOREDOXIN-REDUCT-NADPH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9P4|protein.P0A9P4]]

## Enriched Summary

Thioredoxin reductase is a member of the flavin-containing NADPH:disulfide oxidoreductases (DSOR) family of enzymes. Other members of this family include GLUTATHIONE-REDUCT-NADPH-CPLX, MONOMER-12931, CPLX-4822, CPLX-2803 and CPLX-7455 (in ). Thioredoxin reductase of E. coli K-12 is a homodimer (as determined for the E. coli B enzyme ) with each subunit containing one molecule of FAD in a globular FAD domain, and one redox-active disulfide in a globular NADPH binding domain. The domains are connected by a two-stranded β sheet (in ). Thioredoxin reductase catalyzes the transfer of electrons from NADPH to thioredoxin. Electrons flow from NADPH to FAD, from the reduced FAD to the redox active disulfide of thioredoxin reductase, and then from the newly formed enzyme dithiol to the disulfide of thioredoxin. The reaction may proceed via a ternary complex mechanism (in ). The native enzyme has been purified from E. coli B and E. coli strain 011' . The recombinant E. coli K-12 enzyme has also been purified . Site-directed mutagenesis studies of thioredoxin reductase demonstrated the function of the active site disulfide , and the role of Asp-139 as an active site acid-base catalyst . The catalytic mechanism of the wild-type enzyme was also studied using enzyme-monitored turnover experiments . The crystal structures of wild-type and mutant enzymes have also been determined...

## Biological Role

Catalyzes THIOREDOXIN-REDUCT-NADPH-RXN (reaction.ecocyc.THIOREDOXIN-REDUCT-NADPH-RXN). Bound by FAD (molecule.C00016).

## Annotation

Thioredoxin reductase is a member of the flavin-containing NADPH:disulfide oxidoreductases (DSOR) family of enzymes. Other members of this family include GLUTATHIONE-REDUCT-NADPH-CPLX, MONOMER-12931, CPLX-4822, CPLX-2803 and CPLX-7455 (in ). Thioredoxin reductase of E. coli K-12 is a homodimer (as determined for the E. coli B enzyme ) with each subunit containing one molecule of FAD in a globular FAD domain, and one redox-active disulfide in a globular NADPH binding domain. The domains are connected by a two-stranded β sheet (in ). Thioredoxin reductase catalyzes the transfer of electrons from NADPH to thioredoxin. Electrons flow from NADPH to FAD, from the reduced FAD to the redox active disulfide of thioredoxin reductase, and then from the newly formed enzyme dithiol to the disulfide of thioredoxin. The reaction may proceed via a ternary complex mechanism (in ). The native enzyme has been purified from E. coli B and E. coli strain 011' . The recombinant E. coli K-12 enzyme has also been purified . Site-directed mutagenesis studies of thioredoxin reductase demonstrated the function of the active site disulfide , and the role of Asp-139 as an active site acid-base catalyst . The catalytic mechanism of the wild-type enzyme was also studied using enzyme-monitored turnover experiments . The crystal structures of wild-type and mutant enzymes have also been determined. These data suggested a model involving an FO conformation for flavin oxidation (transferring electrons to the enzyme disulfide) and a rotated FR conformation to allow flavin and thioredoxin reduction. In this mechanism the two domains rotate relative to each other twice in each catalytic cycle (reviewed in and in ). Ultrafast fluorescence spectroscopy studies of wild-type and mutant enzymes also suggested FO a

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.THIOREDOXIN-REDUCT-NADPH-RXN|reaction.ecocyc.THIOREDOXIN-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9P4|protein.P0A9P4]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:THIOREDOXIN-REDUCT-NADPH-CPLX`
- `QSPROTEOME:QS00185245`

## Notes

2*protein.P0A9P4
