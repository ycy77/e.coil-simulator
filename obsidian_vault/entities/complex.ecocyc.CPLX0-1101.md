---
entity_id: "complex.ecocyc.CPLX0-1101"
entity_type: "complex"
name: "tRNA-guanine transglycosylase"
source_database: "EcoCyc"
source_id: "CPLX0-1101"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA-guanine transglycosylase

`complex.ecocyc.CPLX0-1101`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1101`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A847|protein.P0A847]]

## Enriched Summary

tRNA-guanine transglycosylase catalyzes the post-transcriptional base exchange reaction involved in the incorporation of the modified base queuine at the wobble position 34 of tRNAs with GUN anticodons (Asp, Asn, His and Tyr). The enzyme can form a homohexamer, a dimer of Tgt homotrimers . Homotrimerization exhibits concentration dependence . The catalytic mechanism of the enzyme has been investigated. The enzyme most likely follows a ping-pong mechanism . The reaction proceeds via a covalent Tgt-tRNA intermediate; dissociation of the product RNA is the overall rate-limiting step . Asp264 appears to be involved in protonation of the leaving guanine and deprotonation of the incoming preQ1 . Asp143 is involved in recognition of guanine in the tRNA substrate . Other residues shown to be involved in catalytic activity by site-directed mutagenesis are S90 , C265 , and D89 . C145 may have evolved in the eubacterial enzyme to specifically recognize preQ1 rather than the eukaryotic substrate queuine . Reports have addressed recognition of the tRNA substrate by the enzyme . Residues C302, C304, C307, and H317 coordinate a zinc, which is important for homotrimerization and substrate recognition . Additional tRNA modifications are not required for recognition of the tRNA by the enzyme...

## Biological Role

Catalyzes RXN0-1321 (reaction.ecocyc.RXN0-1321). Bound by Zinc cation (molecule.C00038).

## Annotation

tRNA-guanine transglycosylase catalyzes the post-transcriptional base exchange reaction involved in the incorporation of the modified base queuine at the wobble position 34 of tRNAs with GUN anticodons (Asp, Asn, His and Tyr). The enzyme can form a homohexamer, a dimer of Tgt homotrimers . Homotrimerization exhibits concentration dependence . The catalytic mechanism of the enzyme has been investigated. The enzyme most likely follows a ping-pong mechanism . The reaction proceeds via a covalent Tgt-tRNA intermediate; dissociation of the product RNA is the overall rate-limiting step . Asp264 appears to be involved in protonation of the leaving guanine and deprotonation of the incoming preQ1 . Asp143 is involved in recognition of guanine in the tRNA substrate . Other residues shown to be involved in catalytic activity by site-directed mutagenesis are S90 , C265 , and D89 . C145 may have evolved in the eubacterial enzyme to specifically recognize preQ1 rather than the eukaryotic substrate queuine . Reports have addressed recognition of the tRNA substrate by the enzyme . Residues C302, C304, C307, and H317 coordinate a zinc, which is important for homotrimerization and substrate recognition . Additional tRNA modifications are not required for recognition of the tRNA by the enzyme . The enzyme recognized the anticodon arm region of the tRNA substrate, and is active toward either tRNA monomers or dimers . Tgt and QueA each recognize the anticodon region of the tRNA substrate . The minimum recognition sequence for the enzyme is a short 17-nucleotides hairpin containing the target G nucleobase in a "UGU" loop motif . The enzyme shows activity toward 2'-deoxyuridine-containing DNA substrates . Structural requirements of the preQ1 substrate and implications with respect to the cata

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1321|reaction.ecocyc.RXN0-1321]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A847|protein.P0A847]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-1101`
- `QSPROTEOME:QS00049592`

## Notes

3*protein.P0A847
