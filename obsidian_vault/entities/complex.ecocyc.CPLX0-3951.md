---
entity_id: "complex.ecocyc.CPLX0-3951"
entity_type: "complex"
name: "peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcB"
source_database: "EcoCyc"
source_id: "CPLX0-3951"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcB

`complex.ecocyc.CPLX0-3951`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3951`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P02919|protein.P02919]]

## Enriched Summary

Penicillin binding protein 1B (PBP1B), the product of the mrcB gene, is a bifunctional peptidoglycan synthase with transglycosylase and transpeptidase activity. PBP1B has been detected as three isoforms, termed α, β, and γ, each of which has both transglycosylation and transpeptidation activities in vitro . mrcB contains major and minor translation start sites which are predicted to produce proteins containing 844 (α) and 799 (γ) amino acids . The β isoform results from cleavage of the amino-terminal 24 amino acids of the α protein; it is primarily present after cell disruption and may be incidental to the preparation of membrane fractions . PBP1Bβ is an artifact that results from contact with OmpT, an outer membrane protease, during purification procedures . PBP1B is localized in the membranes of the cell envelope; it is often concentrated at adhesion sites where the inner and outer membranes contact . PBP1B contains a short cytoplasmic NH2 domain (residues 1-63) and a single hydrophobic transmembrane segment (residues 64-87) which anchors the protein to the inner membrane; the remainder of the protein consists of a transglycosylase domain followed by a transpeptidase domain and is located in the periplasm . PBP1B has an additional membrane association site located within the first 163 amino acids of the periplasmic domain...

## Biological Role

Catalyzes RXN-16649 (reaction.ecocyc.RXN-16649), RXN-16650 (reaction.ecocyc.RXN-16650), peptidoglycan transpeptidase (Gram-negative bacteria) (reaction.ecocyc.RXN-16659).

## Annotation

Penicillin binding protein 1B (PBP1B), the product of the mrcB gene, is a bifunctional peptidoglycan synthase with transglycosylase and transpeptidase activity. PBP1B has been detected as three isoforms, termed α, β, and γ, each of which has both transglycosylation and transpeptidation activities in vitro . mrcB contains major and minor translation start sites which are predicted to produce proteins containing 844 (α) and 799 (γ) amino acids . The β isoform results from cleavage of the amino-terminal 24 amino acids of the α protein; it is primarily present after cell disruption and may be incidental to the preparation of membrane fractions . PBP1Bβ is an artifact that results from contact with OmpT, an outer membrane protease, during purification procedures . PBP1B is localized in the membranes of the cell envelope; it is often concentrated at adhesion sites where the inner and outer membranes contact . PBP1B contains a short cytoplasmic NH2 domain (residues 1-63) and a single hydrophobic transmembrane segment (residues 64-87) which anchors the protein to the inner membrane; the remainder of the protein consists of a transglycosylase domain followed by a transpeptidase domain and is located in the periplasm . PBP1B has an additional membrane association site located within the first 163 amino acids of the periplasmic domain . When it is cleaved directly c-terminal to the transmembrane segment, the protein continues to associate with the inner membrane . PBP1B forms homodimers (α-α, γ-γ) which appear to be more strongly associated with the peptidoglycan and/or outer membrane; the dimeric proteins are able to bind penicillin G . Dimer formation does not involve disulfide bridges , nor is the cytoplasmic domain of PBP1B necessary for dimer formation . PBP1B does not form a

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16659|reaction.ecocyc.RXN-16659]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P02919|protein.P02919]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3951`
- `QSPROTEOME:QS00049618`

## Notes

2*protein.P02919
