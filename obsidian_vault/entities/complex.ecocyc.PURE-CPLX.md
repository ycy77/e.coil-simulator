---
entity_id: "complex.ecocyc.PURE-CPLX"
entity_type: "complex"
name: "N5-carboxyaminoimidazole ribonucleotide mutase"
source_database: "EcoCyc"
source_id: "PURE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# N5-carboxyaminoimidazole ribonucleotide mutase

`complex.ecocyc.PURE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PURE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AG18|protein.P0AG18]]

## Enriched Summary

PurE and PurK were previously thought to be two subunits of AIR carboxylase , although later studies showed the enzymes to be subunits of a distinct mutase and carboxylase, respectively . PurE catalyzes an unusual transformation, the reversible interconversion of N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) and 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylate (CAIR). Direct transfer of the carboxylate group of the carbamate of N5-CAIR produces CAIR . A crystal structure of PurE determined at 1.5Å resolution with and without the substrate CAIR revealed an octameric quaternary structure. The mononucleotide binding site is located in a a cleft at the interface of two subunits . Subsequent crystal structures of the wild-type enzyme co-crystallized with a CAIR analog, and structures of His45Asn and His45Gln mutant enzymes crystallized with CAIR or an analog, provided insight into substrate binding. A reaction mechanism involving the essential His45 residue, and an enzyme-bound aminoimidazole ribonucleotide and carbon dioxide intermediate was proposed . A high concentration of bicarbonate partially rescues the defect of a purK mutant during growth in the absence of purines, probably by perturbing the balance of AIR toward N5-CAIR. An overproduction of PurE further increases rescue in the presence of bicarbonate...

## Biological Role

Catalyzes RXN0-743 (reaction.ecocyc.RXN0-743).

## Annotation

PurE and PurK were previously thought to be two subunits of AIR carboxylase , although later studies showed the enzymes to be subunits of a distinct mutase and carboxylase, respectively . PurE catalyzes an unusual transformation, the reversible interconversion of N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) and 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylate (CAIR). Direct transfer of the carboxylate group of the carbamate of N5-CAIR produces CAIR . A crystal structure of PurE determined at 1.5Å resolution with and without the substrate CAIR revealed an octameric quaternary structure. The mononucleotide binding site is located in a a cleft at the interface of two subunits . Subsequent crystal structures of the wild-type enzyme co-crystallized with a CAIR analog, and structures of His45Asn and His45Gln mutant enzymes crystallized with CAIR or an analog, provided insight into substrate binding. A reaction mechanism involving the essential His45 residue, and an enzyme-bound aminoimidazole ribonucleotide and carbon dioxide intermediate was proposed . A high concentration of bicarbonate partially rescues the defect of a purK mutant during growth in the absence of purines, probably by perturbing the balance of AIR toward N5-CAIR. An overproduction of PurE further increases rescue in the presence of bicarbonate . The overproduction and purification of PurE has been reported . Analysis of the purE locus at the nucleotide sequence level revealed that the purE1 and purE2 cistrons correspond to two distinct, overlapping genes, purE and purK . Two classes of PurE exist. Class I enzymes require N5-CAIR, the product of PurK, as substrate. Class II enzymes found in higher eukaryotes catalyze the direct carboxylation of 5-amino-1-(5-phospho-D-ribosyl)imidazole (AIR) to prod

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-743|reaction.ecocyc.RXN0-743]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AG18|protein.P0AG18]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:PURE-CPLX`
- `QSPROTEOME:QS00195415`

## Notes

8*protein.P0AG18
