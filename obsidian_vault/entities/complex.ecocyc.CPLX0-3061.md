---
entity_id: "complex.ecocyc.CPLX0-3061"
entity_type: "complex"
name: "aminopeptidase A/I and DNA-binding transcriptional repressor PepA"
source_database: "EcoCyc"
source_id: "CPLX0-3061"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "cytosol aminopeptidase"
  - "leucine aminopeptidase"
---

# aminopeptidase A/I and DNA-binding transcriptional repressor PepA

`complex.ecocyc.CPLX0-3061`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3061`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P68767|protein.P68767]]

## Enriched Summary

Aminopeptidase A/I is a Peptidase that binds DNA and controls the transcription of the operon involved in the synthesis of carbamoyl phosphate, which is an intermediate related to the pyrimidine nucleotide pathway . This protein also is required for maintenance of plasmid monomers, which is critical for proper plasmid segregation . Aminopeptidase A/I is a part of the site-specific recombination system required to decatenate the plasmids ColE1 and pSC101, maintaining them as monomers . Aminopeptidase A/I is responsible for coordinating DNA strands during recombination, pairing cer sites in ColE1 plasmids and allowing the formation of Holliday junctions . Aminopeptidase A/I, along with ArgR, may be involved in blocking trans-recombination, thus preventing the formation of new catenated plasmids during recombination . This overall role in site-specific recombination is independent of Aminopeptidase A/I's peptidase activity . Aminopeptidase A/I binds specifically to several DNA regions, including the the regulatory region before the carAp promoter . This regulatory region wraps around the aminopeptidase A/I hexamer, effectively cutting the distance between the upstream IHF binding site and the transcriptional start site by 235 base pairs, as well as presumably blocking the intervening transcription factor binding sites...

## Biological Role

Catalyzes 3.4.11.1-RXN (reaction.ecocyc.3.4.11.1-RXN), RXN-6622 (reaction.ecocyc.RXN-6622). Bound by Zinc cation (molecule.C00038).

## Annotation

Aminopeptidase A/I is a Peptidase that binds DNA and controls the transcription of the operon involved in the synthesis of carbamoyl phosphate, which is an intermediate related to the pyrimidine nucleotide pathway . This protein also is required for maintenance of plasmid monomers, which is critical for proper plasmid segregation . Aminopeptidase A/I is a part of the site-specific recombination system required to decatenate the plasmids ColE1 and pSC101, maintaining them as monomers . Aminopeptidase A/I is responsible for coordinating DNA strands during recombination, pairing cer sites in ColE1 plasmids and allowing the formation of Holliday junctions . Aminopeptidase A/I, along with ArgR, may be involved in blocking trans-recombination, thus preventing the formation of new catenated plasmids during recombination . This overall role in site-specific recombination is independent of Aminopeptidase A/I's peptidase activity . Aminopeptidase A/I binds specifically to several DNA regions, including the the regulatory region before the carAp promoter . This regulatory region wraps around the aminopeptidase A/I hexamer, effectively cutting the distance between the upstream IHF binding site and the transcriptional start site by 235 base pairs, as well as presumably blocking the intervening transcription factor binding sites . If Aminopeptidase A/I is not present to bind to the carAB control region, pyrimidine regulation of that promoter is impaired . This transcriptional repression requires additional protein factors apart from Aminopeptidase A/I binding to DNA . Based on Genomic SELEX screening, the intergenic region of the bidirectional genes nfeF and nfeR was identified as a target of PepA . This protein was classified as a single-target transcription factor . Aminopeptidase

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.3.4.11.1-RXN|reaction.ecocyc.3.4.11.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-6622|reaction.ecocyc.RXN-6622]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P68767|protein.P68767]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-3061`
- `QSPROTEOME:QS00188613`

## Notes

6*protein.P68767
