---
entity_id: "complex.ecocyc.CPLX0-8231"
entity_type: "complex"
name: "16S rRNA 2'-O-ribose C1402 methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8231"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 16S rRNA 2'-O-ribose C1402 methyltransferase

`complex.ecocyc.CPLX0-8231`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8231`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P67087|protein.P67087]]

## Enriched Summary

RsmI is the methyltransferase responsible for methylation of 16S rRNA at the 2'-O position of the ribose at the C1402 nucleotide within the P site of the ribosome. In vitro, the enzyme is active on the assembled 30S ribosomal subunit, but not naked 16S rRNA or 70S ribosomes . Dimethylation of the C1402 nucleotide is involved in decoding fidelity and translation initiation at non-AUG start codons . The crystal structure of a truncated form of RsmI has been solved at 2.2Å resolution . RsmI is a member of the class III methyltranferase family and consists of an N-terminal potential RNA-binding domain and a C-terminal methyltransferase domain. S-adenosylmethionine (AdoMet) binds in a pocket between the two domains; key residues for binding were confirmed by site-directed mutagenesis . An rsmI null mutant was reported to have no growth defect or a slightly reduced growth rate . An rsmI rsmH double mutant has a more pronounced growth defect . ArmA, the most prevalent methyltransferase responsible for aminoglycoside resistance, impairs methylation at C1402 by RsmI . RsmI: "rRNA small subunit methyltransferase I" RsmI is the methyltransferase responsible for methylation of 16S rRNA at the 2'-O position of the ribose at the C1402 nucleotide within the P site of the ribosome. In vitro, the enzyme is active on the assembled 30S ribosomal subunit, but not naked 16S rRNA or 70S ribosomes...

## Biological Role

Catalyzes RXN-11637 (reaction.ecocyc.RXN-11637).

## Annotation

RsmI is the methyltransferase responsible for methylation of 16S rRNA at the 2'-O position of the ribose at the C1402 nucleotide within the P site of the ribosome. In vitro, the enzyme is active on the assembled 30S ribosomal subunit, but not naked 16S rRNA or 70S ribosomes . Dimethylation of the C1402 nucleotide is involved in decoding fidelity and translation initiation at non-AUG start codons . The crystal structure of a truncated form of RsmI has been solved at 2.2Å resolution . RsmI is a member of the class III methyltranferase family and consists of an N-terminal potential RNA-binding domain and a C-terminal methyltransferase domain. S-adenosylmethionine (AdoMet) binds in a pocket between the two domains; key residues for binding were confirmed by site-directed mutagenesis . An rsmI null mutant was reported to have no growth defect or a slightly reduced growth rate . An rsmI rsmH double mutant has a more pronounced growth defect . ArmA, the most prevalent methyltransferase responsible for aminoglycoside resistance, impairs methylation at C1402 by RsmI . RsmI: "rRNA small subunit methyltransferase I"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11637|reaction.ecocyc.RXN-11637]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P67087|protein.P67087]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8231`
- `QSPROTEOME:QS00150675`

## Notes

2*protein.P67087
