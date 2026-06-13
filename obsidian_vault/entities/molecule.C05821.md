---
entity_id: "molecule.C05821"
entity_type: "small_molecule"
name: "Enterochelin"
source_database: "KEGG"
source_id: "C05821"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Enterochelin"
  - "Enterobactin"
  - "Tri-(2,3-dihydroxy-N-benzoyl-L-serine)-ester"
  - "Tri-(N-(2,3-dihydroxybenzoyl)-L-serine)-ester"
---

# Enterochelin

`molecule.C05821`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05821`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Enterochelin; Enterobactin; Tri-(2,3-dihydroxy-N-benzoyl-L-serine)-ester; Tri-(N-(2,3-dihydroxybenzoyl)-L-serine)-ester EcoCyc common name: enterobactin. ENTEROBACTIN Enterobactin is a catecholate siderophore produced almost exclusively by enterobacteria , although it has been reported in some Streptomyces species . It is a cyclic compound made of three units of 2,3-dihydroxybenzoylserine joined in a cyclic structure by lactone linkages (only the δ-cis isomer of the ferric chelate is biologically active). ENTEROBACTIN Enterobactin binds Fe3+ with a estimated Kd of 10-49 M (10-35 M at physiological pH) . ENTEROBACTIN Enterobactin not only is used by the organisms that produce it but also serves as an exosiderophore for many bacteria that are unable to synthesize it, such as TAX-287, in a strategy of siderophore piracy .

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Annotation

KEGG compound: Enterochelin; Enterobactin; Tri-(2,3-dihydroxy-N-benzoyl-L-serine)-ester; Tri-(N-(2,3-dihydroxybenzoyl)-L-serine)-ester

## Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.ENTG-RXN|reaction.ecocyc.ENTG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ENTMULTI-RXN|reaction.ecocyc.ENTMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-357|reaction.ecocyc.TRANS-RXN-357]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-496|reaction.ecocyc.TRANS-RXN0-496]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14477|reaction.ecocyc.RXN-14477]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20002|reaction.ecocyc.RXN-20002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1661|reaction.ecocyc.RXN0-1661]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-357|reaction.ecocyc.TRANS-RXN-357]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-496|reaction.ecocyc.TRANS-RXN0-496]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P24077|protein.P24077]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C05821`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
