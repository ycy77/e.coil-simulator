---
entity_id: "complex.ecocyc.CPLX0-8122"
entity_type: "complex"
name: "aminopeptidase B"
source_database: "EcoCyc"
source_id: "CPLX0-8122"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aminopeptidase B

`complex.ecocyc.CPLX0-8122`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8122`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37095|protein.P37095]]

## Enriched Summary

Aminopeptidase B (PepB) belongs to the M17 family of metallopeptidases. PepB is one of four cysteinylglycinases in E. coli, along with EG10694-MONOMER aminopeptidase A, EG10696-MONOMER, and CPLX0-3001 . PepA, PepB or PepN can process the heptapeptide-nucleotide CPD0-1129 after removal of the formyl group from fMet, thereby releasing the nonhydrolyzable aspartyl-adenylate that inhibits aspartyl-tRNA synthetase . Aminopeptidase B cleaves Cys-Gly, Leu-Gly, and Leu-Gly-Gly in vitro . A panel of 11 aminopeptidase substrates has been tested; the cleavage profile of PepB is Lys/Leu/Met/Gly > Pro/Tyr > Thr/Gln/Trp . Divalent cations, including some that are not effective stimulators of activity, stabilize aminopeptidase B against heat inactivation . Reports disagree on whether or not EDTA inhibits enzyme activity. Overexpression of pepB partially rescues the growth defect of a pepN mutant in minimal media . Aminopeptidase B (PepB) belongs to the M17 family of metallopeptidases. PepB is one of four cysteinylglycinases in E. coli, along with EG10694-MONOMER aminopeptidase A, EG10696-MONOMER, and CPLX0-3001 . PepA, PepB or PepN can process the heptapeptide-nucleotide CPD0-1129 after removal of the formyl group from fMet, thereby releasing the nonhydrolyzable aspartyl-adenylate that inhibits aspartyl-tRNA synthetase . Aminopeptidase B cleaves Cys-Gly, Leu-Gly, and Leu-Gly-Gly in vitro...

## Biological Role

Catalyzes RXN-6622 (reaction.ecocyc.RXN-6622), RXN0-5204 (reaction.ecocyc.RXN0-5204).

## Annotation

Aminopeptidase B (PepB) belongs to the M17 family of metallopeptidases. PepB is one of four cysteinylglycinases in E. coli, along with EG10694-MONOMER aminopeptidase A, EG10696-MONOMER, and CPLX0-3001 . PepA, PepB or PepN can process the heptapeptide-nucleotide CPD0-1129 after removal of the formyl group from fMet, thereby releasing the nonhydrolyzable aspartyl-adenylate that inhibits aspartyl-tRNA synthetase . Aminopeptidase B cleaves Cys-Gly, Leu-Gly, and Leu-Gly-Gly in vitro . A panel of 11 aminopeptidase substrates has been tested; the cleavage profile of PepB is Lys/Leu/Met/Gly > Pro/Tyr > Thr/Gln/Trp . Divalent cations, including some that are not effective stimulators of activity, stabilize aminopeptidase B against heat inactivation . Reports disagree on whether or not EDTA inhibits enzyme activity. Overexpression of pepB partially rescues the growth defect of a pepN mutant in minimal media .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-6622|reaction.ecocyc.RXN-6622]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5204|reaction.ecocyc.RXN0-5204]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P37095|protein.P37095]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-8122`
- `QSPROTEOME:QS00188435`

## Notes

6*protein.P37095
