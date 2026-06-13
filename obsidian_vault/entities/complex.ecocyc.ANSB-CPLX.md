---
entity_id: "complex.ecocyc.ANSB-CPLX"
entity_type: "complex"
name: "L-asparaginase 2"
source_database: "EcoCyc"
source_id: "ANSB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-asparaginase 2

`complex.ecocyc.ANSB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ANSB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00805|protein.P00805]]

## Enriched Summary

E. coli encodes three enzymes with L-asparaginase activity, ANSA-CPLX, L-asparaginase 2, and CPLX0-263 . L-asparaginase 2 (AnsB) is periplasmic and has a comparatively high affinity for its substrate . The physiological role of L-asparaginase 2 may be to provide a source for the generation of FUM, which serves as an anaerobic electron acceptor during growth on non-fermentable carbon sources, since AnsB's product, L-ASPARTATE, can be transported to the cytoplasm by DCUB-MONOMER and catabolized to fumarate by ASPARTASE-CPLX . In pathogenic E. coli strains, L-asparaginase 2 may play a role in virulence . Unlike L-asparaginase 1, L-asparaginase 2 has therapeutic activity as a treatment for acute lymphoblastic leukemia, and is an FDA-approved protein drug for the treatment of childhood leukemia (reviewed in e.g. ). Multiple crystal structures of the enzyme have been solved . Only recently, a structure of the apo enzyme in the open conformation with a resolved active site flexible loop has been solved . Site-directed mutants in various amino acid residues have been generated, and their enzymatic activity has been analyzed; the residues Thr12, Tyr25, Thr89, Asp90, and Lys162 (numbering for the mature polypeptide) are critical for catalysis...

## Biological Role

Catalyzes ASPARAGHYD-RXN (reaction.ecocyc.ASPARAGHYD-RXN).

## Annotation

E. coli encodes three enzymes with L-asparaginase activity, ANSA-CPLX, L-asparaginase 2, and CPLX0-263 . L-asparaginase 2 (AnsB) is periplasmic and has a comparatively high affinity for its substrate . The physiological role of L-asparaginase 2 may be to provide a source for the generation of FUM, which serves as an anaerobic electron acceptor during growth on non-fermentable carbon sources, since AnsB's product, L-ASPARTATE, can be transported to the cytoplasm by DCUB-MONOMER and catabolized to fumarate by ASPARTASE-CPLX . In pathogenic E. coli strains, L-asparaginase 2 may play a role in virulence . Unlike L-asparaginase 1, L-asparaginase 2 has therapeutic activity as a treatment for acute lymphoblastic leukemia, and is an FDA-approved protein drug for the treatment of childhood leukemia (reviewed in e.g. ). Multiple crystal structures of the enzyme have been solved . Only recently, a structure of the apo enzyme in the open conformation with a resolved active site flexible loop has been solved . Site-directed mutants in various amino acid residues have been generated, and their enzymatic activity has been analyzed; the residues Thr12, Tyr25, Thr89, Asp90, and Lys162 (numbering for the mature polypeptide) are critical for catalysis . In a computational study, a catalytic mechanism involving three sequential steps with two catalytic triads that play different roles in the reaction was proposed . The interactions with substrates and the product aspartate have been characterized by molecular dynamics simulations; the proposed catalytic mechanism involves the α-carboxyl group of L-asparagine as the proton acceptor that activates the catalytic threonine during the nucleophilic attack on the amide carbon . A detailed model of the double-displacement (ping-pong) catalytic mec

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ASPARAGHYD-RXN|reaction.ecocyc.ASPARAGHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P00805|protein.P00805]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ANSB-CPLX`
- `QSPROTEOME:QS00182765`

## Notes

4*protein.P00805
